
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
            dbc.Spinner(children=[
                dbc.Row([

                    dbc.Col([

                        dbc.Container([
                            utils_filters.make_filters(df)
                        ],fluid=True)
                    ],width=9),
                    dbc.Col([
                        dbc.Container([
                            utils_filters.Card_for_obs(df)
                        ],fluid=True)
                    ],width=3)
                ]),
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
                                'margin': '10px',
                                },
                    # Allow multiple files to be uploaded
                            multiple=False
                            )]),
                    ],width=2),
                ]),
                #dbc.Row([html.Hr()]),

                            #offset espacio que se deja desde la izquierda
                dbc.Row([
                    dbc.Col([

                        html.H1("Resumen de clasificación Taxonómica", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                        dbc.Row([
                            dbc.Col([dbc.Container([
                                
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
                                        })
                            ],fluid=True)
                            ],width=12),
                        ],no_gutters=True),
                        dbc.Row([html.Hr()]),
                        ],lg=12),
                    ]),
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

                ]) 
