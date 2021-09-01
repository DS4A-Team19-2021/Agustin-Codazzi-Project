
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd

from apps.utils import utils_pivot_table

from apps.utils.utils_getdata import get_data

df=get_data(["CLIMA_AMBIENTAL", "PAISAJE",
                         'TIPO_RELIEVE', 'FORMA_TERRENO',
                         'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN',
                         "LATITUD","LONGITUD","ALTITUD","CODIGO"]).dropna()

layout_pivot_table=html.Div([
    dbc.Row([html.Hr()]),

            dbc.Row([
                dbc.Col([
                    dbc.Container([
                        html.H3("Desgloce de la taxonomía", className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'}),

                        utils_pivot_table.make_pivot_table(df)], id="Table_data", fluid=True)], width={'size': 12, 'offset': 0},
                    align="center")
            ], no_gutters=True),


    dbc.Row([html.Hr()]),
])