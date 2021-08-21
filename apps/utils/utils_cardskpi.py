import dash_bootstrap_components as dbc

def Card_total(datos):
    lista_observaciones = dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        dbc.ListGroupItemHeading("Numero de Observaciones",style={"font-size":"1.5em"}),
                        dbc.ListGroupItemText(datos,style={"font-size":"2.5em","align":"right"}),
                    ],color="#375A7F"
                ),
            ]
    )
    return lista_observaciones
