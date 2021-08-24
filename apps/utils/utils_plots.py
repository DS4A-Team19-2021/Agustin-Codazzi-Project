import plotly.express as px
import dash_core_components as dcc
import pandas as pd
from apps.utils.utils_getdata import get_data


#df=get_data(["LATITUD","LONGITUD","ORDEN","ALTITUD"]).dropna()
def Make_map(df):
    new_df=df[["LATITUD","LONGITUD","ORDEN","ALTITUD"]].dropna()

    fig=px.scatter_mapbox(new_df, lat="LATITUD", lon="LONGITUD", color= "ORDEN", size_max=15, zoom=6
                      ,labels={"ORDEN": "ORDEN", "ALTITUD": "medal"},custom_data=["ORDEN","ALTITUD"])
    fig.update_layout(
        plot_bgcolor="black",
        mapbox_style="satellite-streets",
        paper_bgcolor="#222222",
        font_color="#FFFFFF",
        margin=dict(l=0, r=2, t=0, b=0),

    )
    fig.update_traces(
        hovertemplate='Orden: %{customdata[0]}' + '<br> Altitud: %{customdata[1]} '
    )

    grafica = dcc.Graph(figure=fig,
                        id="Mapa",
                        config={
                                'mapboxAccessToken':"pk.eyJ1IjoiamFtb250YW5hYyIsImEiOiJja3M5cTdqNjQweDJsMnZwZWhya3doZGhxIn0.wzXfA9bXf2nwKH1lbkLSPA",
                                'displayModeBar': False,
                                'staticPlot': False,
                                'fillFrame':False,
                                'frameMargins': 0,
                                'responsive': True
                            })
    return grafica


