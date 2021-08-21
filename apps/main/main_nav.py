
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
IGAC_LOGO = "https://www.igac.gov.co/sites/igac.gov.co/files/igac-logo.png"

menu_bar = [
    dbc.NavItem(
        dbc.NavLink("Home", active = True,disabled=True, id = "page-1-link")
    ), dbc.Row(
    [
        dbc.Col(dbc.Input(type="buscar", placeholder="Search")),
        dbc.Col(html.Img(src=IGAC_LOGO, height="30px")
            ,
            width="auto",
        ),
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
                    dbc.Col(html.Img(src=IGAC_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("DS4A/IGAC", className="ml-2"))

                ],
                align="center",
                no_gutters=True,

            ),
            href="https://www.igac.gov.co/",
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
        dbc.Collapse(
            menu_bar,
             id="navbar-collapse", navbar=True, is_open=False
        ),
    ],
    color="primary",
    dark=False,
)

layout = html.Div(
    [
            navbar
    ],
    id="menu",
)

