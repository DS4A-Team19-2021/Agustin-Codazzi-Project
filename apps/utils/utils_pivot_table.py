import dash
import dash_pivottable
import pandas as pd
from apps.utils.utils_getdata import get_data
import dash_html_components as html

df=get_data(['CLIMA_AMBIENTAL', 'PAISAJE', 'TIPO_RELIEVE', 'FORMA_TERRENO', 'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN', 'CODIGO']).dropna()

my_data=[list(df)]
for i in range(len(df)):
    my_data.append(list(df.iloc[i].values))

layout_pivot_table = html.Div(
    dash_pivottable.PivotTable(
        data=my_data,
        cols=[],
        rows=["CLIMA_AMBIENTAL", "PAISAJE", 'TIPO_RELIEVE', 'FORMA_TERRENO', 'MATERIAL_PARENTAL_LITOLOGIA', 'ORDEN'],
        vals=["CODIGO"],
    ), style={'height':'500px', 'overflow':'scroll', 'resize':'both'},
)