import plotly.express as px
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
from apps.utils.utils_getdata import get_data

df=get_data(['PAISAJE','CLIMA_AMBIENTAL','FORMA_TERRENO', 'CLASIFICACION_TAXONOMICA','ORDEN']).dropna()
df['conteo_orden'] = 1

fig = px.treemap(df[['PAISAJE','CLIMA_AMBIENTAL','FORMA_TERRENO', 'CLASIFICACION_TAXONOMICA','ORDEN','conteo_orden']].dropna(), path=['PAISAJE','CLIMA_AMBIENTAL','FORMA_TERRENO', 'CLASIFICACION_TAXONOMICA'], values='conteo_orden',
                  color= 'ORDEN', hover_data=[], color_discrete_map={
                "Andisol": '#e74C3C',
                "Entisol": '#3498DB',
                "Histosol": '#00BC8C',
                "Inceptisol": '#375A7F',
                "Molisol": '#F39C12',
                })
fig.update_layout(
    plot_bgcolor="black",
    paper_bgcolor="#222222",
    font_color="#FFFFFF",
    title_font_color="#FFFFFF",
    #font=dict(size=18),
    margin=dict(l=0, r=15, t=0, b=0)
    )


grafica = dcc.Graph(figure=fig,
     config={
            'displayModeBar': False,
            'fillFrame':False,
            'frameMargins': 0,
            'responsive': True
        })