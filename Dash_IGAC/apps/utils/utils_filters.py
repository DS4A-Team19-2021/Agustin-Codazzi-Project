
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from Dash_IGAC.apps.utils.utils_getdata import standarised_string

def make_options_filters(data):
    return [{"label":x,"value":x} for x in data]

def make_filters(df):
    card_of_filters = dbc.Card([
        dbc.CardHeader("Filtros"),
        dbc.CardBody([
                html.H5("Filtre la información que desea ver", className="card-title"),
                dbc.FormGroup([
                    dbc.Label("Clima"),
                    dcc.Dropdown(
                        id="filtro_clima",
                        options=make_options_filters(df["CLIMA_AMBIENTAL"].dropna().unique()),
                        value="",style={'color': 'black'}),
                ]),
                dbc.FormGroup([
                        dbc.Label("Paisaje"),
                        dcc.Dropdown(
                            id="filtro_paisaje",
                            options=make_options_filters(df["PAISAJE"].dropna().unique()),
                            value="",style={'color': 'black'}),
                ]),
                dbc.FormGroup([
                    dbc.Label("Forma de Terreno"),
                    dcc.Dropdown(
                        id="filtro_forma_terreno",
                        options=make_options_filters(df["FORMA_TERRENO"].dropna().unique()),
                        value="",style={'color': 'black'}),
                ]),
                dbc.FormGroup([
                    dbc.Label("Material parental"),
                    dcc.Dropdown(
                        id="filtro_material_parental",
                        options=make_options_filters(df["MATERIAL_PARENTAL_LITOLOGIA"].dropna().unique()),
                        value="",style={'color': 'black'}),
                ]),
                html.Div(id="the_alert", children=[]),
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
        ]),
    ],color="secondary")
    return card_of_filters

#"/Users/jamontanac/Desktop/Screen Shot 2021-07-23 at 10.11.21 AM.png"






