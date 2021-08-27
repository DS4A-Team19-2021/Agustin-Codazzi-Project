import plotly.express as px

def Make_tree_map(df):
    columns_in_map = ["CLIMA_AMBIENTAL", "PAISAJE", "CODIGO", 'TIPO_RELIEVE', 'FORMA_TERRENO',
                        'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN', ]
    new_df=df[columns_in_map].copy()
    new_df['conteo_orden'] = 1

    fig = px.treemap(new_df.dropna(), path=[px.Constant("Total"),'ORDEN','PAISAJE','CLIMA_AMBIENTAL','FORMA_TERRENO'], values='conteo_orden',
                 color="ORDEN",hover_data=[],maxdepth=3, color_discrete_map={
                '(?)': '#A0BBD1',
                "Andisol": '#e74C3C',
                "Entisol": '#3498DB',
                "Histosol": '#00BC8C',
                "Inceptisol": '#375A7F',
                "Molisol": '#F39C12',
                })

    fig.update_traces(name='categories',
                      root_color='#9CC1EF',
                      #texttemplate="%{label}<br>%{value}<br>",
                      selector=dict(type='treemap'))
    fig.update_layout(
        plot_bgcolor="black",
        paper_bgcolor="#222222",
        font_color="#FFFFFF",
        title_font_color="#FFFFFF",
        #font=dict(size=18),
        margin = dict(t=50, l=25, r=25, b=25)
        )

    return fig