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
from apps.utils.utils_getdata import get_data
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

#df=get_data(["CLIMA_AMBIENTAL","FORMA_TERRENO","MATERIAL_PARENTAL_LITOLOGIA","ORDEN","PAISAJE"]).dropna()

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
        if pathname in ["/", "/apps/home/layout_home"]:
            return layout_home.layout
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
    #Callbacks definidos para la carga de un archivo
    def parse_contents(contents, filename, date):
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        columns_to_consider=["CLIMA_AMBIENTAL", "PAISAJE",
                         'TIPO_RELIEVE', 'FORMA_TERRENO',
                         'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN',
                         "LATITUD","LONGITUD","ALTITUD","CODIGO"]
        try:
            if 'csv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
                df = df[columns_to_consider]

            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
                df = df[columns_to_consider]

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

    #@app.callback(Output('Mapa', 'figure'),
    #              Input("filtro_clima","value"),Input("filtro_paisaje","value"),
    #              Input("filtro_forma_terreno", "value"), Input("filtro_material_parental","value"),
    #              Input('upload-data', 'contents'),State('upload-data', 'filename'),
    #              State('upload-data', 'last_modified'))
    #def update_map_dropdown(filtro_clima,filtro_paisaje,filtro_forma_terreno,filtro_material_parental,list_of_contents, list_of_names, list_of_dates):
    #    dropdown=[filtro_clima,filtro_paisaje,filtro_forma_terreno,filtro_material_parental]
    #    if list_of_contents is None:
    #        df= get_data(["CLIMA_AMBIENTAL", "PAISAJE",
    #                     'TIPO_RELIEVE', 'FORMA_TERRENO',
    #                     'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN',
    #                     "LATITUD","LONGITUD","ALTITUD","CODIGO"]).dropna()
    #        conditions=get_conditions_dropdown(df,dropdown)
    #        if conditions.sum()==0:
    #            return dash.no_update
    #        else:
    #            use = df[conditions]
    #            return Make_map(use)
    #    else:
    #        df, filename, date = parse_contents(list_of_contents, list_of_names, list_of_dates)
    #        if len(df)==0:
    #            return dash.no_update
    #        else:
    #            conditions = get_conditions_dropdown(df, dropdown)
    #            if conditions.sum() == 0:
    #                return dash.no_update
    #            else:
    #                use = df[conditions]
    #                return Make_map(use)




    @app.callback(Output('Mapa', 'figure'), Output('tree_map', 'figure'),
                  Output("carta_datos","children"),Output("filtro_clima","options"),
                  Output("filtro_paisaje","options"),Output("filtro_forma_terreno", "options"),
                  Output("filtro_material_parental","options"),Output('Table_data', 'children'),
                  Output("main_alert", "children"),
                  Input("filtro_clima", "value"), Input("filtro_paisaje", "value"),
                  Input("filtro_forma_terreno", "value"), Input("filtro_material_parental", "value"),
                  Input('upload-data', 'contents'),
                  State('upload-data', 'filename'),State('upload-data', 'last_modified'))
    def update_maps(filtro_clima,filtro_paisaje,filtro_forma_terreno,filtro_material_parental,list_of_contents, list_of_names, list_of_dates):
        dropdown = [filtro_clima, filtro_paisaje, filtro_forma_terreno, filtro_material_parental]
        #print(dropdown)
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
                error_section=html.Div([
                                html.H2('There was an error processing this file. File {}, uploaded {}'.format(filename,datetime.datetime.fromtimestamp(date))),
                                html.Br(),
                                html.H2('Double check that you have the right format or your file has the needed Columns')]
                                ,className="text-danger",style={"align-text":"center"})
                return dash.no_update, dash.no_update, dash.no_update,\
                       dash.no_update, dash.no_update,\
                       dash.no_update, dash.no_update,\
                       error_section, alert2
            else:
                conditions = get_conditions_dropdown(df, dropdown)
                if conditions.sum() == 0:
                    return dash.no_update, dash.no_update, dash.no_update, dash.no_update,\
                           dash.no_update, dash.no_update, dash.no_update, dash.no_update,\
                           dash.no_update,
                else:
                    use = df[conditions]
                    table_children = html.Div([
                        html.H2("Tabla Dinamica", className='title ml-2',
                                style={'textAlign': 'left', 'color': '#FFFFFF'}),
                        html.H4("Archivo Cargado: {}".format(filename), className='title ml-2',
                                style={'textAlign': 'left', 'color': '#FFFFFF'}),
                        html.H5("Fecha de Carga: {}".format(datetime.datetime.fromtimestamp(date)),
                                className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'}),
                        make_pivot_table(use)
                    ])
                    good_alarm = dbc.Alert([html.H4("The file {} was successfully processed".format(filename)), ],
                                           color="success", dismissable=True,
                                           duration=5000)

                    return Make_map(use),Make_tree_map(use), len(use), \
                           make_options_filters(df["CLIMA_AMBIENTAL"].dropna().unique()), \
                           make_options_filters(df["PAISAJE"].dropna().unique()), \
                           make_options_filters(df["FORMA_TERRENO"].dropna().unique()), \
                           make_options_filters(df["MATERIAL_PARENTAL_LITOLOGIA"].dropna().unique()),\
                           table_children, good_alarm
        else:
            raise PreventUpdate





    #@app.callback(Output("Download_file", "data"),
    #"Table_data"
    #              [Input("Boton_download", "n_clicks")],
    #              prevent_initial_call=True)
    #def generate_csv(n_nlicks):
    #    return dcc.send_data_frame(df.to_csv, filename="prueba.csv")

    #return {"color":"primary", }
    