import dash_bootstrap_components as dbc
import dash
import flask

# external JavaScript files
external_scripts = [
     {'src': 'https://kit.fontawesome.com/44d65a8b68.js'},
     {'crossorigin':"anonymous"}  
]

#Change dbc.themes, more themes in 
#https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
server = flask.Flask(__name__)
app = dash.Dash(__name__,server=server, external_stylesheets=[dbc.themes.DARKLY],
               title='Clasificación Taxonómica IGAC', external_scripts=external_scripts, suppress_callback_exceptions=True,
               meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'},
                 ]
)
