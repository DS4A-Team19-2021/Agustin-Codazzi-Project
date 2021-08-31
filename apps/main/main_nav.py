
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
IGAC_LOGO = "https://www.igac.gov.co/sites/igac.gov.co/files/igac-logo.png"
Logo_grupo="https://raw.githubusercontent.com/DS4A-Team19-2021/Agustin-Codazzi-Project/main/Images/logo_igac.png"
github_logo="https://github.com/jamontanac/Tesis_Master/raw/master/GitHub_logo.png"
correlation_one_logo="https://www.correlation-one.com/hubfs/c1logo_color.png"
menu_bar = [
    dbc.NavItem(
        dbc.NavLink("Inicio", active = True, id = "page-1-link",href="/apps/home/layout_inicio")
    ),
    dbc.NavItem(
        dbc.NavLink("Visualización", active = "exact", href = "/apps/home/layout_home", id = "page-2-link")
    ),
    dbc.NavItem(
        dbc.NavLink("Tabla", active = "exact", href = "/apps/pivot_table/layout_pivot", id = "page-3-link")
    ),
    dbc.NavItem(
        dbc.NavLink("About", active = False, href = "#", id = "page-4-link",disabled=True)
    ),
    ##375A7F;
    dbc.Row([

        dbc.Col([
            html.A(html.Img(src=correlation_one_logo, height="20px"),
                   href="https://www.correlation-one.com/")
        ],width="auto"),
        dbc.Col([
            html.A(html.Img(src=github_logo, height="25px")
                ,href="https://github.com/DS4A-Team19-2021")]),
    ],
    no_gutters=False,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
]

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=Logo_grupo, height="40px")),

                    dbc.Col(dbc.NavbarBrand("CATS", className="ml-2"))

                ],
                align="center",
                no_gutters=True,

            ),
            href="#",
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            menu_bar,
             id="navbar-collapse", navbar=True, is_open=False
        ),
    ],
    color="primary",
    dark=True,sticky="top",
)

layout = html.Div(
    [
            navbar
    ],
    id="menu",
)


