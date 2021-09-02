import plotly.express as px

def Make_map(df):
    new_df=df[["LATITUD","LONGITUD","ALTITUD","CLIMA_AMBIENTAL", "PAISAJE", "CODIGO", 'TIPO_RELIEVE', 'FORMA_TERRENO',
                        'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN']].dropna()

    fig=px.scatter_mapbox(new_df, lat="LATITUD", lon="LONGITUD", color= "ORDEN", size_max=6, zoom=7
                      ,labels={"ORDEN": ""},custom_data=["ORDEN","ALTITUD","PAISAJE","CLIMA_AMBIENTAL","TIPO_RELIEVE"],
                          color_discrete_map={
                              "Andisol": '#e74C3C',
                              "Entisol": '#3498DB',
                              "Histosol": '#00BC8C',
                              "Inceptisol": '#375A7F',
                              "Molisol": '#F39C12',
                          },size=[2]*len(new_df)
                          )
    fig.update_layout(
        plot_bgcolor="black",
        mapbox_style="satellite-streets",
        paper_bgcolor="#222222",
        font_color="#FFFFFF",
        font=dict(
            size=12,
            family="Lato",
            color="#FFFFFF"),
        margin=dict(l=0, r=2, t=0, b=0),
        height=500,
        legend= dict(
                #yanchor="top",
                y=0.06,
                xanchor="right",
                x=0.97,
                orientation="h",
                bordercolor="#222222",borderwidth=2,bgcolor="#222222"),


    )
    fig.update_traces(
        hovertemplate='Orden: %{customdata[0]}' + '<br> Altitud: %{customdata[1]} ' + '<br> Paisaje: %{customdata[2]} ' + '<br> Clima: %{customdata[3]} ' + '<br> Relieve: %{customdata[4]} ',

    )


    return fig


