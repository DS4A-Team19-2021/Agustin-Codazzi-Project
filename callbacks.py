import base64
import datetime
import io
import pandas as pd
import numpy as np
#basic libraries
from dash.dependencies import Input, Output, State
from flask_caching import Cache
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from apps.utils.utils_getdata import get_data, standarised_string
from apps.utils.ETL import ETL, extract_data_to_predict
from apps.utils.utils_pivot_table import make_pivot_table
from apps.utils.utils_plots import Make_map
from apps.utils.utils_tree_map import Make_tree_map
from apps.utils.utils_filters import make_filters, make_options_filters
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
#main dash instance
from app import app



# #call modules needed for callbacks
from apps.home import layout_home
from apps.pivot_table import layout_pivot
from apps.home import layout_inicio
from apps.about import about_layout

#cache configuration
TIMEOUT = 240
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 20
})

#Entire callbacks definition
def register_callbacks(app):

    #callback for navigation, look for url and respond with the right layout
    @cache.memoize(timeout=TIMEOUT)
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname in ["/apps/home/layout_home"]:
            return layout_home.layout
        elif pathname in ["/","/apps/home/layout_inicio"]:
            return layout_inicio.layout
        elif pathname in ["/apps/pivot_table/layout_pivot"]:
            return layout_pivot.layout_pivot_table
        elif pathname in ["/apps/about/about_layout"]:
            return about_layout.layout
        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
                html.Br(),
                html.P(f"Check again what you are requesting")
            ],fluid=False
        )

    @app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    #Callbacks definidos para la carga de un archivo
    @cache.memoize(timeout=TIMEOUT)
    def parse_contents(contents, filename, date):
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        #columns_to_consider=["CLIMA_AMBIENTAL", "PAISAJE",
        #                 "TIPO_RELIEVE", "FORMA_TERRENO",
        #                 "MATERIAL_PARENTAL_LITOLOGIA", "ORDEN",
        #                 "LATITUD","LONGITUD","ALTITUD","CODIGO"]
        try:
            if 'csv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
            # put df in ETL
            try:
                clean_df= ETL(df)
                #check if the dataframe has ORDEN
                if "ORDEN" in clean_df.columns:
                    return clean_df, filename, date
                else:
                    return pd.DataFrame([]), filename, date

            except CustomError as e:
                print("problema en el ETL")
                return pd.DataFrame([]), filename, date


            return df, filename, date
        except Exception as e:
            return pd.DataFrame([]), filename, date
    def get_conditions_dropdown(df,dropdown):
        filtros = ["CLIMA_AMBIENTAL", "PAISAJE", "FORMA_TERRENO", "MATERIAL_PARENTAL_LITOLOGIA"]
        condition = pd.Series(np.ones(len(df), dtype=bool))
        for i, j in zip(dropdown, filtros):
            if i == "" or i==None:
                continue
            else:
                condition = condition & (df[j] == i)
        return condition


    @app.callback(Output('Table_data','children'),Output('main_alert_tabla','children'),
                  Input('upload-data_table', 'contents'),
                  State('upload-data_table', 'filename'),State('upload-data_table', 'last_modified'))
    def update_table(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            df, filename, date = parse_contents(list_of_contents, list_of_names, list_of_dates)
            if len(df) == 0:
                error_section = html.Div([
                    html.H2('Un error ocurrió al procesar el archivo {}, subido en la fecha {}'.format(filename,
                                                                                                       datetime.datetime.fromtimestamp(date))),
                    html.Br(),
                    html.H2('Verifique que su archivo tiene el formato adeacuado y que contiene las columnas necesarias para renderizar la tabla')],
                    className="text-danger", style={"align-text": "center"})
                alert = dbc.Alert([html.H4("Un Error ha ocurrido al procesar el archivo {}".format(filename)),
                                    html.Hr(),
                                    html.P(
                                        "Porfavor verifique que el archivo que usted está cargando un archivo que sea compitble para la aplicación"
                                        "Recuerde que sólo los formatos (csv, xls, xlsx, xlsm) son formatos aceptados por esta aplicación. "
                                        "En caso de que esté subiendo un archivo en este formato y encuentra este error por favor revise que su archivo contiene las "
                                        "columnas necesarias para que la aplicación funcione.", className="mb-0")
                                    ],
                                   color="danger", dismissable=True,
                                   duration=7000)
                return error_section,alert

            else:
                table_children = html.Div([
                    html.H4("Archivo Cargado: {}".format(filename), className='title ml-2',
                            style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    html.H5("Fecha de Carga: {}".format(datetime.datetime.fromtimestamp(date)),
                            className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    make_pivot_table(df)
                ])
                return table_children,dash.no_update
        else:
            return dash.no_update,dash.no_update

    @app.callback(Output('Mapa', 'figure'), Output('tree_map', 'figure'),
                  Output("carta_datos","children"), Output("filtro_clima","options"),
                  Output("filtro_paisaje","options"), Output("filtro_forma_terreno", "options"),
                  Output("filtro_material_parental","options"),
                  Output("main_alert", "children"), Output("data_alert","children"),
                  Input("filtro_clima", "value"), Input("filtro_paisaje", "value"),
                  Input("filtro_forma_terreno", "value"), Input("filtro_material_parental", "value"),
                  Input('upload-data', 'contents'),
                  State('upload-data', 'filename'),State('upload-data', 'last_modified'))
    def update_maps(filtro_clima,filtro_paisaje,filtro_forma_terreno,filtro_material_parental,list_of_contents, list_of_names, list_of_dates):
        dropdown = [filtro_clima, filtro_paisaje, filtro_forma_terreno, filtro_material_parental]
        if list_of_contents is not None:
            df, filename, date = parse_contents(list_of_contents, list_of_names, list_of_dates)
            if len(df) == 0:
                #alert1 = dbc.Alert("There was an error processing this file.",
                #                  color="danger",dismissable=True,
                #                  duration=5000)
                alert2 = dbc.Alert([html.H4("Un Error ha ocurrido al procesar el archivo {}".format(filename)),
                                    html.Hr(),
                                    html.P("Porfavor verifique que el archivo que usted está cargando un archivo que sea compitble para la aplicación"
                                           "Recuerde que sólo los formatos (csv, xls, xlsx, xlsm) son formatos aceptados por esta aplicación. "
                                           "En caso de que esté subiendo un archivo en este formato y encuentra este error por favor revise que su archivo contiene las "
                                           "columnas necesarias para que la aplicación funcione.",className="mb-0")
                                    ],
                                   color="danger",dismissable=True,
                                   duration=7000)

                #dash.callback_context.inputs['upload-data.contents']=None
                #print(dash.callback_context.inputs['upload-data.contents'])
                return dash.no_update, dash.no_update, dash.no_update,\
                       dash.no_update, dash.no_update,\
                       dash.no_update, dash.no_update,\
                       alert2,dash.no_update
            else:
                conditions = get_conditions_dropdown(df, dropdown)
                data_alert = dbc.Alert(html.H2(
                    "La combinación de filtros solicitada no contiene datos, porfavor eliga una nueva combinación o deseleccione un filtro"),
                                       color="warning", dismissable=True, duration=5000)
                if conditions.sum() == 0:

                    return dash.no_update, dash.no_update, dash.no_update, dash.no_update,\
                           dash.no_update, dash.no_update, dash.no_update,dash.no_update,\
                           data_alert
                else:
                    use = df[conditions]

                    #good_alarm = dbc.Alert([html.H4("El archivo {} fue procesado exitosamente".format(filename)), ],
                    #                       color="success", dismissable=True,
                    #                       duration=5000)

                    return Make_map(use),Make_tree_map(use), len(use), \
                           make_options_filters(df["CLIMA_AMBIENTAL"].dropna().unique()), \
                           make_options_filters(df["PAISAJE"].dropna().unique()), \
                           make_options_filters(df["FORMA_TERRENO"].dropna().unique()), \
                           make_options_filters(df["MATERIAL_PARENTAL_LITOLOGIA"].dropna().unique()),\
                           dash.no_update,dash.no_update
        else:
            df = get_data(["CLIMA_AMBIENTAL", "PAISAJE",
                           "TIPO_RELIEVE", "FORMA_TERRENO",
                           "MATERIAL_PARENTAL_LITOLOGIA", "ORDEN",
                           "LATITUD", "LONGITUD", "ALTITUD", "CODIGO"]).dropna().reset_index(drop=True)
            conditions = get_conditions_dropdown(df, dropdown)
            data_alert = dbc.Alert(html.H2(
                "La combinación de filtros solicitada no contiene datos, porfavor eliga una nueva combinación o deseleccione un filtro"),
                color="warning", dismissable=True, duration=5000)
            if conditions.sum() == 0:
                return dash.no_update, dash.no_update, dash.no_update, dash.no_update,\
                       dash.no_update, dash.no_update, dash.no_update, dash.no_update,\
                       data_alert
            else:
                use = df[conditions]
                return Make_map(use), Make_tree_map(use), len(use), \
                       dash.no_update, dash.no_update, \
                       dash.no_update, dash.no_update, \
                       dash.no_update, dash.no_update





    