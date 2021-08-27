import dash_bootstrap_components as dbc
import dash

# external JavaScript files
external_scripts = [
     {'src': 'https://kit.fontawesome.com/44d65a8b68.js'},
     {'crossorigin':"anonymous"}  
]

#Change dbc.themes, more themes in 
#https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
               title='IGAC Taxonomía', external_scripts=external_scripts, suppress_callback_exceptions=True,
               meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'},
                 ]
)

