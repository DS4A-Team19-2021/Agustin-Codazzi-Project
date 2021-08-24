import dash
import dash_pivottable
import pandas as pd
from apps.utils.utils_getdata import get_data
import dash_html_components as html


def make_pivot_table(df):
    columns_in_table=["CLIMA_AMBIENTAL", "PAISAJE", "CODIGO", 'TIPO_RELIEVE', 'FORMA_TERRENO', 'MATERIAL_PARENTAL_LITOLOGIA',
                  'ORDEN',]
    new_df=df[columns_in_table]
    Data_to_use = [list(new_df)] + new_df.to_numpy().tolist()
    layout_pivot_table = html.Div(
        dash_pivottable.PivotTable(
            data=Data_to_use,
            cols=[],
            rows=["CLIMA_AMBIENTAL", "PAISAJE", 'TIPO_RELIEVE', 'FORMA_TERRENO', 'MATERIAL_PARENTAL_LITOLOGIA',
                  'ORDEN'],
            vals=["CODIGO"],
        ), style={'height': '700px', 'overflow': 'scroll', 'resize': 'both'},
    )
    return layout_pivot_table

