import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

github_logo="https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png"
correlation_one_logo="https://www.correlation-one.com/hubfs/c1logo_color.png"
#dash_logo="https://dash.plotly.com/docs/assets/images/light_plotly_dash_logo.png"

dash_logo="https://plotly-marketing-website.cdn.prismic.io/plotly-marketing-website/948b6663-9429-4bd6-a4cc-cb33231d4532_logo-plotly.svg"
info_general = html.Div([
        dcc.Markdown('''
##### Agradecimientos a los integrantes del equipo 19:
---
Diana Vélez, Juan Sebastian Serrano, Jaime Muñoz,

Fransisco Lara, Sebastian Orozco, Endwyr,

Jose Alejandro Montaña
''')
    ],style={"font-size":"12px","align-text":"right"})


layout= html.Div([
      dbc.Row([
        dbc.Col([
            dbc.Row([html.H4("Agradecimientos:")]),
            dbc.Row([
                dbc.Col([
                    html.A(
                        html.Img(src=correlation_one_logo, height="20px"),href="https://github.com/DS4A-Team19-2021")
                    ]),
                dbc.Col([
                    html.A(
                        html.Img(src=github_logo, height="25px"),href="https://github.com/DS4A-Team19-2021")
                    ])
                ,
                dbc.Col([
                    html.A(
                        html.Img(src=dash_logo, height="30px")
                        ,href="https://dash.plotly.com/")
                    ])
                ],no_gutters=False)
            ],lg=5),
        dbc.Col([
            info_general
            ],align="right",lg=3)
        ],justify="between")
], className="footer")
  
   
