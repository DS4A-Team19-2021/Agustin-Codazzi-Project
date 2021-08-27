#Dash basic libraries
import dash_core_components as dcc
import dash_html_components as html
#Best practice libraries
import dash_auth

#callbacks import
from callbacks import register_callbacks

#dash instance
from app import app
from app import server

#Dash custom modules
from apps.main import main_nav, main_content, main_footer

#Basic auth definition
USERNAMEINFO = [['user','12345']]
auth = dash_auth.BasicAuth(app,USERNAMEINFO)

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


# Main server 
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)

