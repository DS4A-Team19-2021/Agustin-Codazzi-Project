
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
            dbc.Row([html.Hr()]),
            dbc.Row([
                dbc.Col([
                    dbc.Container([
            dbc.Spinner(children=[
                dbc.Row([

                    dbc.Col([

                        dbc.Container([
                            utils_filters.make_filters(df)
                        ],fluid=True)
                    ],width=9),
                    dbc.Col([
                        dbc.Row([
                        dbc.Container([
                            utils_filters.Card_for_obs(df)
                        ],fluid=True)]),
                        dbc.Row([
                        dbc.Container([
                            dcc.Upload(
                                id='upload-data',
                                children=html.Div([
                                    'Inserte ',
                                    html.A('el archivo')
                                ]),
                                style={
                                    'width': '96%',
                                    'height': '50px',
                                    'lineHeight': '50px',
                                    'borderWidth': '1px',
                                    'borderStyle': 'dashed',
                                    'borderRadius': '5px',
                                    'textAlign': 'center',
                                    'margin': '10px',
                                },
                                # Allow multiple files to be uploaded
                                multiple=False
                            )
                        ],fluid=False,style={"left-padding": "10px"})]),

                    ],width=3)
                ]),
                #dbc.Row([html.Hr()]),

                            #offset espacio que se deja desde la izquierda
                dbc.Row([
                    dbc.Col([
                        dbc.Container([
                            dbc.Tabs(
                            [
                                dbc.Tab(label="Georeferenciación", tab_id="tab_map",active_tab_style={"border-color":"#f39c12"}),
                                dbc.Tab(label="Proporción Taxonómica", tab_id="tab_tree"),
                            ],
                            id="tabs",
                            active_tab="tab_map",
                        ),],fluid=True),
                        dbc.Container([
                            dbc.Card([
                                #dbc.CardHeader([
                                #    dbc.Tabs(
                                #        [
                                #            dbc.Tab(label="Georeferenciación", tab_id="tab_map"),
                                #            dbc.Tab(label="Proporción Taxonómica", tab_id="tab_tree"),
                                #        ],
                                #        id="tabs",
                                #        active_tab="tab_map",card=True
                                #    ),
                                #]),
                                dbc.CardBody([
                                    dbc.Col([
                                        dcc.Graph(figure=utils_plots.Make_map(df),
                                                id="Mapa",
                                                config={
                                                    'mapboxAccessToken': open(".mapbox_token").read(),
                                                    'displayModeBar': False,
                                                    'staticPlot': False,
                                                    'fillFrame': False,
                                                    'frameMargins': 0,
                                                    'responsive': False,
                                                    'showTips': True
                                                })
                                    ], lg=12,align="center")
                                ]),
                            ],color="secondary",inverse=False,style={'borderRadius': '0px',"border-color":"#f39c12"})
                        ],fluid=True)
                    ],width=12),

                ],justify="center"),
                    dbc.Row([
                        dbc.Col([

                            html.H2("Desglose Taxonómico", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
            
                        dbc.Row([
                            dbc.Col([
                                dbc.Container([
                                    dcc.Graph(figure=utils_tree_map.Make_tree_map(df),
                                              id="tree_map",
                                              config={
                                                     'displayModeBar': False,
                                                     'fillFrame':False,
                                                     'frameMargins': 0,
                                                     'staticPlot': False,
                                                     'responsive': False,
                                                    'showTips':True
                                                 },style={'height': '700px'}),
                                ],fluid=True,)
                                ], width=12),
                            ],no_gutters=True)
                    ],lg=11)
                        ]),

                #dbc.Row([html.Hr()]),
                #dbc.Row([
                #    dbc.Col([
                #    dbc.Container([
                #        html.H2("Tabla Dinamica", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),

                #        utils_pivot_table.make_pivot_table(df)],id="Table_data",fluid=True)],width={'size': 12, 'offset': 0},align="center")
                #],no_gutters=True),
                dbc.Row([html.Hr()]),
                ], color="primary", type="border",fullscreen=True,fullscreen_style={"background-color": "#444444"}),
                ],fluid=True)
                ],width=12,align="end")
                ])
                ]) 
