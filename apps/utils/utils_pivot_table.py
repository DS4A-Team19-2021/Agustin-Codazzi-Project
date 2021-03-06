import dash_pivottable
import dash_html_components as html


def make_pivot_table(df):
    columns_in_table=["CLIMA_AMBIENTAL", "PAISAJE", "CODIGO", 'TIPO_RELIEVE', 'FORMA_TERRENO', 'MATERIAL_PARENTAL_LITOLOGIA',
                  'ORDEN',]
    new_df=df[columns_in_table].dropna()
    Data_to_use = [list(new_df)] + new_df.to_numpy().tolist()
    layout_pivot_table = html.Div(
        dash_pivottable.PivotTable(
            data=Data_to_use,
            cols=[],
            rows=["CLIMA_AMBIENTAL", "PAISAJE", 'TIPO_RELIEVE', 'FORMA_TERRENO', 'MATERIAL_PARENTAL_LITOLOGIA',
                  'ORDEN'],
            vals=["CODIGO"],
        ), style={'height': '700px','width': '99%', 'overflow': 'scroll', 'resize': 'both','align':'center'},
    )
    return layout_pivot_table

