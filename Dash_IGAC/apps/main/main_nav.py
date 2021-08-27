
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

IGAC_LOGO = "https://www.igac.gov.co/sites/igac.gov.co/files/igac-logo.png"
github_logo="https://github.com/jamontanac/Tesis_Master/raw/master/GitHub_logo.png"
correlation_one_logo="https://www.correlation-one.com/hubfs/c1logo_color.png"
menu_bar = [
    dbc.NavItem(
        dbc.NavLink("Home", active = True, id = "page-1-link",href="/apps/home/layout_home")
    ),
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

