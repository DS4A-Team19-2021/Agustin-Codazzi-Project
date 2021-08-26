
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
from apps.utils import utils_cardskpi
from apps.utils import utils_plots
from apps.utils import utils_filters
from apps.utils import utils_tree_map
from apps.utils import utils_cardskpi
from apps.utils import utils_pivot_table
from apps.utils.utils_getdata import get_data

df=get_data(["CLIMA_AMBIENTAL", "PAISAJE",
                         'TIPO_RELIEVE', 'FORMA_TERRENO',
                         'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN',
                         "LATITUD","LONGITUD","ALTITUD","CODIGO"]).dropna()



layout= html.Div([
            dbc.Row([html.Hr()]), # primera fila se deja vacia
            dbc.Row([
                dbc.Col([
                    utils_filters.make_filters(df)

                    ],lg=2,id="Filter_section"),
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
                                    })])
                        ],lg='10'),

                        dbc.Col([
                            dbc.ListGroup([
                                            dbc.ListGroupItem(
                                                children=utils_cardskpi.Card_total(len(df)),
                                                id="carta_totales",color="#375A7F")
                                        ])
                        ],width={"size": 2, "offset": 0})
                        #offset espacio que se deja desde la izquierda
                    ],no_gutters=True),
                    dbc.Row([html.Hr()]),

                    dbc.Row([
                        dbc.Container([
                                html.H2("Desglose Taxonómico", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                        ],fluid=True),
                        dbc.Col([
                            dbc.Container([
                            dcc.Graph(figure=utils_tree_map.Make_tree_map(df),
                                      id="tree_map",
                                      config={
                                             'displayModeBar': False,
                                             'fillFrame':False,
                                             'frameMargins': 0,
                                             'responsive': False
                                         })]),], width={"size": 9, "offset": 0,})
                        ],no_gutters=True)
                    ],lg=10),
                ]),
            dbc.Row([html.Hr()]),
            dbc.Row([

                dbc.Container([
                    html.H2("Tabla Dinamica", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    utils_pivot_table.make_pivot_table(df)],id="Table_data")
            ]),
            dbc.Row([html.Hr()])

                ]) 
