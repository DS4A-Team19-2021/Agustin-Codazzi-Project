import dash_bootstrap_components as dbc

def Card_total(datos):
    lista_observaciones = [
                        dbc.ListGroupItemHeading("Numero de Observaciones",style={"font-size":"1.3em"}),
                        dbc.ListGroupItemText(datos, style={"font-size":"2.5em","align":"right"})
    ]
    return lista_observaciones
