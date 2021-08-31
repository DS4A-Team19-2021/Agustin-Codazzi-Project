import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


layout= html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Container([
                html.Video(src="https://github.com/jamontanac/Tesis_Master/blob/master/Introduccio%CC%81n.mp4?raw=true",
                           style={"height": "500", "width": "100%"},autoPlay=True,controls=True,preload="parts",
                           loop=True,title="Video de prueba",accessKey="spacer",poster="https://raw.githubusercontent.com/jamontanac/Tesis_Master/master/Github_logo_black.png"),
            ])
        ],width=12,align="center")
    ],justify="center")
])