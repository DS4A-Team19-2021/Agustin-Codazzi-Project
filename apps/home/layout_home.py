
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
                         "TIPO_RELIEVE", "FORMA_TERRENO",
                         "MATERIAL_PARENTAL_LITOLOGIA", "ORDEN",
                         "LATITUD","LONGITUD","ALTITUD","CODIGO"]).dropna()


carta_mapa=dbc.Card([
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
                                                },style={'height': '500px'})
                                    ], lg=12,align="center")
                                ]),
                            ],style={'borderRadius': '0px'},color="#ffffff00")

carta_tree_map=dbc.Card([
                    dbc.CardBody([
                            dbc.Col([
                                    dcc.Graph(figure=utils_tree_map.Make_tree_map(df),
                                              id="tree_map",
                                              config={
                                                     'displayModeBar': False,
                                                     'fillFrame':False,
                                                     'frameMargins': 0,
                                                     'staticPlot': False,
                                                     'responsive': False,
                                                    'showTips':True
                                                 },style={'height': '500px'}),
                                ],  lg=12,align="center"),
                            ]),
                    ],style={'borderRadius': '0px',},color="#ffffff00",)

upload_component=dcc.Upload(
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
    multiple=False
                                # Allow multiple files to be uploaded
)

layout= html.Div([
            dbc.Row([html.Hr()]),
            dbc.Row([
                dbc.Col([
                    dbc.Container([
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
                            upload_component,

                        ],fluid=False,style={"left-padding": "10px"})]),

                    ],width=3)
                ]),
                #dbc.Row([html.Hr()]),

                           #offset espacio que se deja desde la izquierda
                dbc.Row([
                    dbc.Col([
                        dbc.Container([
                        dbc.Spinner(children=[
                        #dcc.Loading(children=[
                            dbc.Tabs(
                            [
                                dbc.Tab(label="Georeferenciación", tab_id="tab_map",children=[carta_mapa]),


                                dbc.Tab(label="Proporción de Taxonomía", tab_id="tab_tree",children=[carta_tree_map]),

                            ],
                            id="tabs",
                            active_tab="tab_map",
                        ),
                        #],type="circle",color="primary",style={"background-color": "#444444"})
                        ], color="primary", type="border",fullscreen=False,fullscreen_style={"background-color": "#444444"}),

                        ],fluid=True),

                    ],width=12),

                ],justify="center"),

                dbc.Row([html.Hr()]),

                ],fluid=True)
                ],width=12,align="end")
                ])
                ]) 


#dbc.Container([
                        #    dbc.Card([
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
                        #        dbc.CardBody([
                        #            dbc.Col([
                        #                dcc.Graph(figure=utils_plots.Make_map(df),
                        #                        id="Mapa",
                        #                        config={
                        #                            'mapboxAccessToken': open(".mapbox_token").read(),
                        #                            'displayModeBar': False,
                        #                            'staticPlot': False,
                        #                            'fillFrame': False,
                        #                            'frameMargins': 0,
                        #                            'responsive': False,
                        #                            'showTips': True
                        #                        })
                        #            ], lg=12,align="center")
                        #        ]),
                        #    ],color="secondary",inverse=False,style={'borderRadius': '0px',"border-color":"#f39c12"})
                        #],fluid=True)