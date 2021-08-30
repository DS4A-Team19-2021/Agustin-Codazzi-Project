
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps.utils.utils_getdata import standarised_string

def make_options_filters(data):
    return [{"label":x,"value":x} for x in data]
montana="https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/mountain.png"
pencil="https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/pencil.png"
river="https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/river.png"
sun="https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/sun.png"
volcan="https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/volcan.png"
lupa="https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/lupa.png"
def make_filters(df):
    card_of_filters = dbc.Card([
        #dbc.CardHeader([

        #    dbc.Row([
        #        dbc.Col([html.H3("Filtros")],width=12),
                    #html.H2("Filtros2","font-size":"2.5em")
        #        ])
        #]),
        dbc.CardBody([
                #html.H5("Filtre la información que desea ver", className="card-title"),
            dbc.Row([
                dbc.Col([
                    html.Div(id="main_alert", children=[])
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div(id="data_alert", children=[])
                ]),
            ]),
            dbc.Row([

                    dbc.Col([
                        dbc.Row(html.Img(src=sun, height="80px"),style={"text-align":"center"},justify="center",align="center"),
                        #dbc.FormGroup([
                            #dbc.Label("Clima"),
                        dbc.Row([html.Hr()]),
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    id="filtro_clima",
                                    options=make_options_filters(df["CLIMA_AMBIENTAL"].dropna().unique()),
                                    value="",style={'color': 'black'},placeholder="Clima"),
                            ],width=12)
                        ])
                        #]),
                    ],width=3),
                    dbc.Col([
                        dbc.Row(html.Img(src=river, height="80px"), style={"text-align": "center"}, justify="center",
                                align="center"),
                        dbc.Row([html.Hr()]),
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    id="filtro_paisaje",
                                    options=make_options_filters(df["PAISAJE"].dropna().unique()),
                                    value="", style={'color': 'black'}, placeholder="Paisaje"),
                            ], width=12)
                        ]),
                        #dbc.FormGroup([
                        #        dbc.Label("Paisaje"),
                        #        dcc.Dropdown(
                        #            id="filtro_paisaje",
                        #            options=make_options_filters(df["PAISAJE"].dropna().unique()),
                        #            value="",style={'color': 'black'}),
                        #]),
                    ],width=3),
                    dbc.Col([
                        dbc.Row(html.Img(src=montana, height="80px"), style={"text-align": "center"}, justify="center",
                                align="center"),
                        #dbc.FormGroup([
                        #    dbc.Label("Forma de Terreno"),
                        dbc.Row([html.Hr()]),
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    id="filtro_forma_terreno",
                                    options=make_options_filters(df["FORMA_TERRENO"].dropna().unique()),
                                    value="",style={'color': 'black'},placeholder="Forma de Terreno"),
                            ], width=12)
                        ]),
                        #]),
                    ],width=3),
                    dbc.Col([
                        dbc.Row(html.Img(src=volcan, height="80px"), style={"text-align": "center"}, justify="center",
                                align="center"),
                        dbc.Row([html.Hr()]),
                        dbc.Row([
                            dbc.Col([
                        #dbc.FormGroup([
                        #    dbc.Label("Material parental"),
                            dcc.Dropdown(
                                id="filtro_material_parental",
                                options=make_options_filters(df["MATERIAL_PARENTAL_LITOLOGIA"].dropna().unique()),
                                value="",style={'color': 'black'},placeholder="Material Parental"),
                            ], width=12)
                        ]),
                        #]),
                    ],width=3),
                ]),
                #dbc.Row([
                #    html.Div(id="the_alert", children=[]),]
                #),
                #dbc.Row([
                #    dbc.Col([
                #        dbc.FormGroup([
                #        dcc.Upload(
                #            id='upload-data',
                #            children=html.Div([
                #                'Drag Here or ',
                #                    html.A('Select Files')
                #                     ]),
                #            style={
                #                'width': '100%',
                #                'height': '60px',
                #                'lineHeight': '60px',
                #                'borderWidth': '1px',
                #                'borderStyle': 'dashed',
                #                'borderRadius': '5px',
                #                'textAlign': 'center',
                #                'margin': '10px',
                #                },
                #    # Allow multiple files to be uploaded
                #            multiple=False
                #            )]),
                #    ],width=2)
                #])
        ]),
    ],color="secondary",style={'borderRadius': '15px'})
    return card_of_filters
def Card_for_obs(df):
    card=dbc.Card([
            #dbc.CardHeader([
            #    html.H3("Observaciones", style={"padding": "5px", "text-align": "right"}),

                    # id="carta_datos")],

            #]),

            dbc.CardBody([
                #dbc.Row(html.Img(src=lupa, height="70px"), style={"text-align": "center"}, justify="center",
                #        align="center"),
                dbc.Row([
                    dbc.Col([
                        dbc.Col([html.Img(src=lupa, height="70px")], width=5),
                    ],width=4,align="center"),
                    dbc.Col([
                        dbc.Row([

                            dbc.Col([
                                html.H4("Observaciones", style={"padding": "5px", "text-align": "right"}),
                            ],align="end")
                        ]),

                        dbc.Row([
                            dbc.Col([
                                    html.H3(len(df), style={"text-align": "right", "font-size": "2.5em"}, id="carta_datos")
                                ],align="end")
                        ])
                    ], width=8),
                ])
            ])
    ],color="secondary",style={'borderRadius': '15px'})
    return card

#"/Users/jamontanac/Desktop/Screen Shot 2021-07-23 at 10.11.21 AM.png"






