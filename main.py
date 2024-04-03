from flet import *
from flet_route import *

from views.login import Login
from views.registro import Registro
from apps.home import Home


def main(page: Page):
    page.padding = 0
    page.spacing = 0
    page.window_width = 390
    page.window_height = 844
    page.window_max_width = 800
    page.window_max_height = 844
    page.window_left = 1500

    page.fonts = {
        "Poppins": "https://fonts.google.com/share?selection.family=Onest:wght@100..900"
    }
    page.theme = Theme(font_family="Poppins")
    page.theme_mode = ThemeMode.DARK

    app_routes = [
        path('/', clear=True, view=Login),
        path('/registro', clear=True, view=Registro),
        path('/home', clear=True, view=Home),

    ]

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)


if __name__ == '__main__':
    app(target=main)
