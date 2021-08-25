import plotly.express as px
import dash_core_components as dcc
import pandas as pd
from apps.utils.utils_getdata import get_data


#df=get_data(["LATITUD","LONGITUD","ORDEN","ALTITUD"]).dropna()
def Make_map(df):
    new_df=df[["LATITUD","LONGITUD","ORDEN","ALTITUD"]].dropna()

    fig=px.scatter_mapbox(new_df, lat="LATITUD", lon="LONGITUD", color= "ORDEN", size_max=15, zoom=7
                      ,labels={"ORDEN": "ORDEN", "ALTITUD": "medal"},custom_data=["ORDEN","ALTITUD"],
                          color_discrete_map={
                              "Andisol": '#e74C3C',
                              "Entisol": '#3498DB',
                              "Histosol": '#00BC8C',
                              "Inceptisol": '#375A7F',
                              "Molisol": '#F39C12',
                          }
                          )
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


    return fig


