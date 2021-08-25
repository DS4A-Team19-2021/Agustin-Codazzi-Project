import base64
import datetime
import io
import pandas as pd
#basic libraries
from dash.dependencies import Input, Output, State
from flask_caching import Cache
import dash_html_components as html
import dash_bootstrap_components as dbc
from apps.utils.utils_getdata import get_data
from apps.utils.utils_pivot_table import make_pivot_table
from apps.utils.utils_plots import Make_map
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

    @app.callback(Output('Table_data', 'children'),
                  Input('upload-data', 'contents'),
                  State('upload-data', 'filename'),
                  State('upload-data', 'last_modified'))
    def update_table_upload(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            df, filename, date = parse_contents(list_of_contents, list_of_names, list_of_dates)
            if len(df)==0:
                return html.Div([
                html.H2('There was an error processing this file. File {}, uploaded {}'.format(filename,date)),
                html.Br(),
                html.H2('Double check that you have the right format or your file has the needed Columns')]
                ,className="text-danger",style={"align-text":"center"})
            else:
                return html.Div([
                    html.H2("Tabla Dinamica", className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    html.H4("Archivo Cargado: {}".format(filename),  className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    html.H5("Fecha de Carga: {}".format(datetime.datetime.fromtimestamp(date)),  className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    make_pivot_table(df),
                ])


        else:
            raise PreventUpdate

    @app.callback(Output('Mapa', 'figure'),
                  Input('upload-data', 'contents'),
                  State('upload-data', 'filename'),
                  State('upload-data', 'last_modified'))
    def update_map_upload(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            df, filename, date = parse_contents(list_of_contents, list_of_names, list_of_dates)
            if len(df) == 0:
                raise PreventUpdate
            else:
                return Make_map(df)
        else:
            raise PreventUpdate


    #@app.callback(Output("Download_file", "data"),
    #"Table_data"
    #              [Input("Boton_download", "n_clicks")],
    #              prevent_initial_call=True)
    #def generate_csv(n_nlicks):
    #    return dcc.send_data_frame(df.to_csv, filename="prueba.csv")

    #return {"color":"primary", }
    