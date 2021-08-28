
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
from apps.utils import utils_plots
from apps.utils import utils_filters
from apps.utils import utils_tree_map
from apps.utils import utils_pivot_table
from apps.utils.utils_getdata import get_data

df=get_data(["CLIMA_AMBIENTAL", "PAISAJE",
                         'TIPO_RELIEVE', 'FORMA_TERRENO',
                         'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN',
                         "LATITUD","LONGITUD","ALTITUD","CODIGO"]).dropna()



layout= html.Div([
            #dbc.Row(dbc.Col(
            #    dbc.Spinner(children=[dcc.Graph(id="loading-output")], size="lg", color="primary", type="border", fullscreen=True,),
                # spinner_style={"width": "10rem", "height": "10rem"}),
                # spinnerClassName="spinner"),
                # dcc.Loading(children=[dcc.Graph(id="loading-output")], color="#119DFF", type="dot", fullscreen=True,),

            #    width={'size': 12, 'offset': 0}),
            #),
            dbc.Row([html.Hr()]), # primera fila se deja vacia
            dbc.Row([

                dbc.Col([

                    dbc.Container([
                        utils_filters.make_filters(df)
                    ],fluid=True)
                ],width=12)
            ]),
           dbc.Row([
               dbc.Col([
                   dbc.Container([
                       dbc.ListGroup([
                           dbc.ListGroupItem([
                               dbc.ListGroupItemHeading("Numero de Observaciones",
                                                        style={"font-size": "1.3em"}),
                               dbc.ListGroupItemText(len(df), style={"font-size": "2.5em","align": "right"},
                                                     id="carta_datos")],
                                                        id="carta_totales",color="#375A7F")
                                                ])
                    ])
               ],width=12)
           ]),
                        #offset espacio que se deja desde la izquierda
            dbc.Row([
                dbc.Col([

                    html.H1("Resumen de clasificación Taxonómica", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    dbc.Row([
                        dbc.Col([dbc.Container([
                            dbc.Spinner(children=[
                                dcc.Graph(figure=utils_plots.Make_map(df),
                                id="Mapa",
                                config={
                                        'mapboxAccessToken':open(".mapbox_token").read(),
                                        'displayModeBar': False,
                                        'staticPlot': False,
                                        'fillFrame':False,
                                        'frameMargins': 0,
                                        'responsive': False,
                                        'showTips':True
                                    })], color="primary", type="border",
                                fullscreen=True)
                        ],fluid=True)
                        ],width=12),
                    ],no_gutters=True),
                    dbc.Row([html.Hr()]),
                    ],lg=12),
                ]),
                dbc.Row([
                    dbc.Container([
                            html.H2("Desglose Taxonómico", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                        ],fluid=True),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(figure=utils_tree_map.Make_tree_map(df),
                                      id="tree_map",
                                      config={
                                             'displayModeBar': False,
                                             'fillFrame':False,
                                             'responsive': False,
                                            'showTips':True
                                         }),
                            ], width=12),
                        ],no_gutters=True)
                ]),

            dbc.Row([html.Hr()]),
            dbc.Row([
                dbc.Col([
                dbc.Container([
                    html.H2("Tabla Dinamica", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),

                    utils_pivot_table.make_pivot_table(df)],id="Table_data",fluid=True)],width={'size': 12, 'offset': 0},align="center")
            ],no_gutters=True),
            dbc.Row([html.Hr()]),

                ]) 
