import base64
import datetime
import io
import pandas as pd
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


    @app.callback(Output('Mapa', 'figure'), Output('tree_map', 'figure'),
                  Output("carta_datos","children"),
                  Output("filtro_clima","options"), Output("filtro_paisaje","options"),
                  Output("filtro_forma_terreno", "options"), Output("filtro_material_parental","options"),
                  Output('Table_data', 'children'), Output("the_alert", "children"),
                  Output("main_alert", "children"),
                  Input('upload-data', 'contents'),
                  State('upload-data', 'filename'),
                  State('upload-data', 'last_modified'))
    def update_maps(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            df, filename, date = parse_contents(list_of_contents, list_of_names, list_of_dates)
            if len(df) == 0:
                alert1 = dbc.Alert("There was an error processing this file.",
                                  color="danger",dismissable=True,
                                  duration=5000)
                alert2 = dbc.Alert([html.H4("An error was encountered when parsing the file {}".format(filename)),
                                    html.Hr(),
                                    html.P("Please double check that your file is compatible with the formats (csv,xls,xlsx,xlsm)"
                                           "these formats are only supported at the moment so make sure you are using the right format."
                                           "In case you are using the right format make sure your file has the required columns.",className="mb-0")
                                    ],
                                   color="danger",dismissable=True,
                                   duration=7000)
                error_section=html.Div([
                                html.H2('There was an error processing this file. File {}, uploaded {}'.format(filename,date)),
                                html.Br(),
                                html.H2('Double check that you have the right format or your file has the needed Columns')]
                                ,className="text-danger",style={"align-text":"center"})
                return dash.no_update, dash.no_update, dash.no_update,\
                       dash.no_update, dash.no_update,\
                       dash.no_update, dash.no_update,\
                       error_section, alert1,alert2
            else:
                table_children=html.Div([
                    html.H2("Tabla Dinamica", className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    html.H4("Archivo Cargado: {}".format(filename),  className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    html.H5("Fecha de Carga: {}".format(datetime.datetime.fromtimestamp(date)),  className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    make_pivot_table(df)
                ])
                good_alarm=dbc.Alert([html.H4("The file {} was successfully processed".format(filename)),],
                                   color="success",dismissable=True,
                                   duration=5000)
                mini_alarm= dbc.Alert("File proccesed",
                                  color="success",dismissable=True,
                                  duration=5000)
                return Make_map(df),Make_tree_map(df), len(df), \
                       make_options_filters(df["CLIMA_AMBIENTAL"].dropna().unique()), \
                       make_options_filters(df["PAISAJE"].dropna().unique()), \
                       make_options_filters(df["FORMA_TERRENO"].dropna().unique()), \
                       make_options_filters(df["MATERIAL_PARENTAL_LITOLOGIA"].dropna().unique()),\
                       table_children, mini_alarm, good_alarm
        else:
            raise PreventUpdate





    #@app.callback(Output("Download_file", "data"),
    #"Table_data"
    #              [Input("Boton_download", "n_clicks")],
    #              prevent_initial_call=True)
    #def generate_csv(n_nlicks):
    #    return dcc.send_data_frame(df.to_csv, filename="prueba.csv")

    #return {"color":"primary", }
    