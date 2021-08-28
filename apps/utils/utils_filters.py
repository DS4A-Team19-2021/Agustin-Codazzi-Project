
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps.utils.utils_getdata import standarised_string

def make_options_filters(data):
    return [{"label":x,"value":x} for x in data]

def make_filters(df):
    card_of_filters = dbc.Card([
        dbc.CardHeader([
            dbc.Row([
                dbc.Col([
                    html.Div(id="main_alert", children=[])
                ]),dbc.Col([
                    html.Div(id="data_alert", children=[])
                ])
            ]),
            dbc.Row([
                dbc.Col([html.H2("Filtros")],width=10),
                dbc.Col([
                            dbc.Row(
                                dbc.Col([html.H4("Numero de Observaciones",style={"padding": "5px","text-align":"center"})
                                            ]),justify="end",align="end"),
                            dbc.Row([
                                dbc.Col([
                                    html.H2(len(df),style={"text-align":"right","font-size":"2.8em"},id="carta_datos")
                                ])
                                ],justify="end",align="end"),
                                                  #id="carta_datos")],

                    ],width=2,align="end"),
                    #html.H2("Filtros2","font-size":"2.5em")
                ])
        ]),
        dbc.CardBody([
                html.H5("Filtre la información que desea ver", className="card-title"),
            dbc.Row([
                    dbc.Col([
                        dbc.FormGroup([
                            dbc.Label("Clima"),
                            dcc.Dropdown(
                                id="filtro_clima",
                                options=make_options_filters(df["CLIMA_AMBIENTAL"].dropna().unique()),
                                value="",style={'color': 'black'}),
                        ]),
                    ],width=3),
                    dbc.Col([
                        dbc.FormGroup([
                                dbc.Label("Paisaje"),
                                dcc.Dropdown(
                                    id="filtro_paisaje",
                                    options=make_options_filters(df["PAISAJE"].dropna().unique()),
                                    value="",style={'color': 'black'}),
                        ]),
                    ],width=3),
                    dbc.Col([
                        dbc.FormGroup([
                            dbc.Label("Forma de Terreno"),
                            dcc.Dropdown(
                                id="filtro_forma_terreno",
                                options=make_options_filters(df["FORMA_TERRENO"].dropna().unique()),
                                value="",style={'color': 'black'}),
                        ]),
                    ],width=3),
                    dbc.Col([
                        dbc.FormGroup([
                            dbc.Label("Material parental"),
                            dcc.Dropdown(
                                id="filtro_material_parental",
                                options=make_options_filters(df["MATERIAL_PARENTAL_LITOLOGIA"].dropna().unique()),
                                value="",style={'color': 'black'}),
                        ]),
                    ],width=3)
                ]),
                #dbc.Row([
                #    html.Div(id="the_alert", children=[]),]
                #),
                dbc.Row([
                    dbc.Col([
                        dbc.FormGroup([
                        dcc.Upload(
                            id='upload-data',
                            children=html.Div([
                                'Drag Here or ',
                                    html.A('Select Files')
                                     ]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                                },
                    # Allow multiple files to be uploaded
                            multiple=False
                            )]),
                    ],width=12)
                ])
        ]),
    ],color="secondary")
    return card_of_filters

#"/Users/jamontanac/Desktop/Screen Shot 2021-07-23 at 10.11.21 AM.png"






