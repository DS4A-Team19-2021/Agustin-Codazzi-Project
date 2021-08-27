#Dash basic libraries
import dash_core_components as dcc
import dash_html_components as html
#Best practice libraries
import dash_auth
import pathlib
#callbacks import
from Dash_IGAC.callbacks import register_callbacks
from dash.dependencies import Input, Output, State
#dash instance
from Dash_IGAC.app import app
import dash
#Dash custom modules
from Dash_IGAC.apps.main import main_nav, main_content, main_footer
from Dash_IGAC.apps.home import layout_home
def create_dash_app(routes_pathname_prefix: str = None) -> dash.Dash:
    #Basic auth definition
    USERNAMEINFO = [['user','12345']]
    auth = dash_auth.BasicAuth(app,USERNAMEINFO)
    # Path
    BASE_PATH = pathlib.Path(__file__).parent.resolve()
    server = app.server
    #main layout
    app.layout = html.Div(className='wrapper',
        children=[
            dcc.Location(id='url', refresh=False),
            main_nav.layout,
            main_content.layout,
            main_footer.layout
        ]
    )

    #Callbacks register
    register_callbacks(app)

    return app


