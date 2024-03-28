from flet import *
from flet_route import *

from views.login import Login
from views.registro import Registro


def main(page: Page):
    page.padding = 0
    page.spacing = 0
    page.window_width = 390
    page.window_height = 844
    page.fonts = {
        "Poppins": "https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,"
                   "200..1000&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,"
                   "200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap'"
    }
    page.theme = Theme(font_family="Poppins")

    app_routes = [
        path('/', clear=True, view=Login),
        path('/registro', clear=True, view=Registro),
    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)


app(target=main)
