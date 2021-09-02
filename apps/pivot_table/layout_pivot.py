
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd

from apps.utils import utils_pivot_table

from apps.utils.utils_getdata import get_data

df=get_data(["CLIMA_AMBIENTAL", "PAISAJE",
                         "TIPO_RELIEVE", "FORMA_TERRENO",
                         "MATERIAL_PARENTAL_LITOLOGIA", "ORDEN",
                         "LATITUD","LONGITUD","ALTITUD","CODIGO"]).dropna()



upload_component=dcc.Upload(
                                id='upload-data_table',
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

layout_pivot_table=html.Div([
    dbc.Row([html.Hr()]),
    dbc.Row([
                            dbc.Col([
                                html.Div(id="main_alert_tabla", children=[])
                            ],width=9,align="center"),],justify="center"),
    dbc.Row([
        dbc.Col([
            dbc.Container([html.H2("Desgloce de la taxonomía", className='title ml-2', style={'textAlign': 'left', 'color': '#FFFFFF'})],fluid=True)],width=9),
        dbc.Col([
            dbc.Container([upload_component],fluid=True)],width=3)
    ]),
    dbc.Row([html.Hr()]),
            dbc.Row([
                dbc.Col([
                    dbc.Spinner(children=[
                        dbc.Container([
                            utils_pivot_table.make_pivot_table(df)], id="Table_data", fluid=True)
                    ], color="primary", type="border",fullscreen=False,fullscreen_style={"background-color": "#444444"}),
                ], width={'size': 12, 'offset': 0},
                    align="center")

            ], no_gutters=True,justify="center"),


    dbc.Row([html.Hr()]),
])