from apps.utils.utils_getdata import standarised_string
import pandas as pd
import unidecode
import numpy as np

#def standarised_string(x):
#    no_accents = unidecode.unidecode(x)
#    return no_accents.replace("_"," ").lower().capitalize()



def ETL(x):
    x_df=x.copy()
    uso = ['CLIMA_AMBIENTAL', 'PAISAJE', 'TIPO_RELIEVE', 'FORMA_TERRENO', 'MATERIAL_PARENTAL_LITOLOGIA', 'LATITUD',
           'LONGITUD', 'ALTITUD', 'CODIGO',
           'DRENAJE_NATURAL', 'H1_ESPESOR', 'H1_RESULTADO_ph', 'H2_ESPESOR', 'EPIPEDON', 'FAMILIA_TEXTURAL',
           'PROFUNDIDAD_MAXIMA']
    if not set(uso).issubset(x_df.columns):
        #print("no encontro algo")
        raise CustomError("No se encontraron todas las columnas requeridas")


      # TIPO_RELIEVE

    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Aa]banico.*', value='Abanico', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Ll]oma.*', value='Loma', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Dd]omo.*', value='Domo', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Gg]lacis.*|.*[Gg]lacís.*|.*[Gg]lac.*', value='Glacis', regex=True,
                                 inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Cc]ampo.*', value='Campo', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Tt]erraza.*', value='Terraza', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Pp]lano.*', value='Plano', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Dd]ep.*', value='Deposito', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Cc]rest.*', value='Cresta', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Dd]eposito.*', value='Vega', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Cc]ono.*', value='Cono', regex=True, inplace=True)
    x_df["TIPO_RELIEVE"].replace(to_replace=r'.*[Cc]oluv.*', value='Coluvio', regex=True, inplace=True)

    # FORMA_TERRENO

    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Rr]ev.*", value="Reves", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Ll]adera.*", value="Ladera", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Cc]uerpo.*", value="Cuerpo", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Nn]apa.*|.*[Gg]las.*", value="Napa", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Cc]ubeta.*", value="Cubeta", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Tt]erraza.*", value="Terraza", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Aa]p.*|.*[Aa]p.*", value="Apice", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Mm]orr.*", value="Morrena", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Dd]ep.*", value="Depresion", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Vv]ega.*", value="Vega", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Pp]lano.*", value="Plano", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Oo]ril.*", value="Orillar", regex=True, inplace=True)
    x_df["FORMA_TERRENO"].replace(to_replace=r".*[Cc]auce.*", value="Cauce", regex=True, inplace=True)

    # LATITUD

    x_df['LATITUD'] = x_df['LATITUD'].astype(float)

    # LONGITUD

    x_df['LONGITUD'] = x_df['LONGITUD'].astype(float)

    # ALTITUD

    x_df['ALTITUD'] = x_df['ALTITUD'].astype(float)

    # H1_ESPESOR

    x_df['H1_ESPESOR'] = x_df['H1_ESPESOR'].astype(float)

    # H1_RESULTADO_ph

    x_df['H1_RESULTADO_ph'] = x_df['H1_RESULTADO_ph'].astype(str).str.replace(",", ".")
    x_df['H1_RESULTADO_ph'] = x_df['H1_RESULTADO_ph'].astype(str).str.replace("_", " ").astype(float)

    # EPIPEDON
    for i in ["Melánico", "Hístico", "Úmbrico", "Ócrico", "Mólico", "úmbrico", "Arenosa", "Cámbico", "Folístico",
              "Histico", "Sáprico", 'Mólico']:
        sub_str = ".*[" + i[0].upper() + i[0].lower() + "]" + i[1:] + ".*"
        x_df["EPIPEDON"].replace(to_replace=sub_str, value=standarised_string(i), regex=True, inplace=True)

    # H2_ESPESOR

    x_df['H2_ESPESOR'] = x_df['H2_ESPESOR'].astype(float)

    # FAMILIA_TEXTURAL

    for i in ["Hidrosa", "Arcillosa", "Medial", "Cenizal", "Franca", "Arenoso", "Arenosa", "Euica", "Limosa",
              "Esquelética", "Limosa", 'Dísica', 'Euíca', 'Fina', 'FIna']:
        sub_str = ".*[" + i[0].upper() + i[0].lower() + "]" + i[1:] + ".*"
        x_df["FAMILIA_TEXTURAL"].replace(to_replace=sub_str, value=standarised_string(i), regex=True, inplace=True)

    # PROFUNDIDAD_MAXIMA

    x_df["PROFUNDIDAD_MAXIMA"] = x_df["PROFUNDIDAD_MAXIMA"].astype(float)

    # CONTENIDO_CENIZA_VOLCANICA
    x_df["CONTENIDO_CENIZA_VOLCANICA"] = x_df['MATERIAL_PARENTAL_LITOLOGIA'].str.lower().str.contains('volc')
    x_df["CONTENIDO_CENIZA_VOLCANICA"] = x_df["CONTENIDO_CENIZA_VOLCANICA"].astype(str)

    # MATERIAL_PARENTAL_LITOLOGIA

    x_df['MATERIAL_PARENTAL_LITOLOGIA'].replace(to_replace=r".*[Oo]rg.*", value="Organica", regex=True, inplace=True)
    x_df['MATERIAL_PARENTAL_LITOLOGIA'].replace(
        to_replace=r".*Depositos_superficiales\nDepositos_superficiales.*|.*[Dd]ep.*|.*[Aa]luv.*|.*[Mm]aterial.*|.*[Cc]oluv.*|.*[Ss]edimento.*|.*[Gg]lac.*|.*[Aa]rcillas.*",
        value="Depositos_superficiales", regex=True, inplace=True)
    x_df['MATERIAL_PARENTAL_LITOLOGIA'].replace(to_replace=r".*[Ee]sq.*", value="Metamorficas", regex=True,
                                                inplace=True)
    x_df['MATERIAL_PARENTAL_LITOLOGIA'].replace(
        to_replace=r".*[Aa]renisc.*|.*[Ss]hale.*|.*[Ll]ut.*|.*[Ll]im.*|.*[Ll]od.*|.*[Aa]rcillol.*|.*[Cc]alc.*|.*[Cc]l.*|.*[Dd]inamo.*",
        value="Sedimentarias", regex=True, inplace=True)
    x_df['MATERIAL_PARENTAL_LITOLOGIA'].replace(to_replace=r".*[Tt]ob.*", value="Igneas", regex=True, inplace=True)
    x_df["MATERIAL_PARENTAL_LITOLOGIA"].replace(to_replace='Quigua_Arriba_quebrada_Quigua', value=np.NaN, inplace=True)
    for i in x_df[uso].select_dtypes("object").columns:
        x_df[i] = x_df[i].astype("category")
    for i in x_df[uso].select_dtypes("category").columns:
        x_df[i] = x_df[i].apply(standarised_string)

    return x_df
#df_otro=pd.read_csv("/Users/jamontanac/Documents/DS4A/Learning Dash/Data3.csv")
#print(ETL(df_otro),)
#print("ORDEN" in ETL(df_otro).columns)
def extract_data_to_predict(x):
    uso = [ 'ALTITUD','CONTENIDO_CENIZA_VOLCANICA','DRENAJE_NATURAL','EPIPEDON',  'FAMILIA_TEXTURAL', 'H1_ESPESOR', 'H1_RESULTADO_ph','H2_ESPESOR',
           'PROFUNDIDAD_MAXIMA']
    return 0
