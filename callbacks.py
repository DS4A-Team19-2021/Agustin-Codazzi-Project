#basic libraries
from dash.dependencies import Input, Output, State
from flask_caching import Cache
import dash_html_components as html
import dash_bootstrap_components as dbc
from apps.utils.utils_getdata import get_data
import dash_core_components as dcc
#main dash instance
from app import app

# #call modules needed for callbacks
from apps.home import layout_home

df=get_data(["CLIMA_AMBIENTAL","FORMA_TERRENO","MATERIAL_PARENTAL_LITOLOGIA","ORDEN","PAISAJE"]).dropna()

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


    @app.callback(Output("Download_file", "data"),
                  [Input("Boton_download", "n_clicks")],
                  prevent_initial_call=True)
    def generate_csv(n_nlicks):
        return dcc.send_data_frame(df.to_csv, filename="prueba.csv")
    #return {"color":"primary", }
    