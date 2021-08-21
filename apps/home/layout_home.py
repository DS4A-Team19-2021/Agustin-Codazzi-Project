
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from apps.utils import utils_cardskpi
from apps.utils import utils_plots
from apps.utils import utils_filters
from apps.utils import utils_tree_map
from apps.utils import utils_cardskpi




layout= html.Div([
            dbc.Row([html.Hr()]), # primera fila se deja vacia
            dbc.Row([
                dbc.Col([
                    utils_filters.card_of_filters
                    ],lg=2),
                dbc.Col([
                    html.H1("Resumen de clasificación Taxonómica", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    dbc.Row([
                        dbc.Col([

                          utils_plots.grafica],lg='9'),

                        dbc.Col([utils_cardskpi.Card_total(12110)],width={"size": 3, "offset": 0})
                        #offset espacio que se deja desde la izquierda
                    ]),
                    dbc.Row([html.Hr()]),
                    html.H1("Desglose Taxonómico", className='title ml-2',style={'textAlign': 'left', 'color': '#FFFFFF'}),
                    dbc.Row([
                        dbc.Col([utils_tree_map.grafica,], lg='8')
                        ])
                    ],lg=10),
                ])

                ]) 
