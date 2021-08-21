
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from apps.utils.utils_getdata import get_data,standarised_string
df=get_data(["CLIMA_AMBIENTAL","FORMA_TERRENO","MATERIAL_PARENTAL_LITOLOGIA","ORDEN","PAISAJE"])
Clima=df["CLIMA_AMBIENTAL"]
Forma_terreno=df["FORMA_TERRENO"]
Material_parental=df["MATERIAL_PARENTAL_LITOLOGIA"]
Orden=df["ORDEN"]
Paisaje=df["PAISAJE"]

card_of_filters = dbc.Card([
    dbc.CardHeader("Filtros"),
    dbc.CardBody([
            html.H5("Filtre la información que desea ver", className="card-title"),
            dbc.FormGroup([
                dbc.Label("Clima"),
                dcc.Dropdown(
                    id="filtro_clima",
                    options=[{"label":standarised_string(x),"value":x} for x in Clima.dropna().unique()],
                    value="",style={'color': 'black'}),
            ]),
            dbc.FormGroup([
                    dbc.Label("Paisaje"),
                    dcc.Dropdown(
                        id="filtro_paisaje",
                        options=[{"label":standarised_string(x),"value":x} for x in Paisaje.dropna().unique()],
                        value="",style={'color': 'black'}),
            ]),
            dbc.FormGroup([
                dbc.Label("Forma de Terreno"),
                dcc.Dropdown(
                    id="filtro_forma_terreno",
                    options=[{"label":standarised_string(x),"value":x} for x in Forma_terreno.dropna().unique()],
                    value="",style={'color': 'black'}),
            ]),
            dbc.FormGroup([
                dbc.Label("Material parental"),
                dcc.Dropdown(
                    id="filtro_material_parental",
                    options=[{"label":standarised_string(x),"value":x} for x in Material_parental.dropna().unique()],
                    value="",style={'color': 'black'}),
            ]),
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
            dbc.FormGroup([
                dbc.Button("Descargar",id="Boton_download", outline=True,color='primary'
                          ,active=False,disabled=True,
                           style={
                            'width': '100%',
                            'height': '60px',
                            'lineHeight': '10px',
                            'borderWidth': '1px',
                            'borderStyle': 'dashed',
                            'borderRadius': '5px',
                            'textAlign': 'center',
                            'margin': '10px',
                            'font-size': 'large'
                           }),
                dcc.Download(id="Download_file")
                ])
    ]),
],color="secondary")	

#"/Users/jamontanac/Desktop/Screen Shot 2021-07-23 at 10.11.21 AM.png"






