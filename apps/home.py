from flet import *
from flet_route import Params, Basket


# import hashlib


class Colors:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED_600 = "#E53935"
    BLUE_LIGHT = "#428aed"
    BLUE_DARK = "#5d7ae5"
    DARK_BLUE = "#0024ed"
    GRAY_LIGHT = "#f0f2fc"


class Styles:
    TEXT_COLOR = Colors.WHITE
    TEXT_SIZE = 16
    BUTTON_COLOR = Colors.BLACK


def Home(page: Page, params: Params, basket: Basket):
    def calcular_ancho(percentage):
        return page.window_width * percentage

    home = Container(
        width=page.window_width,
        height=page.window_height,
        margin=0,
        padding=20,
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=[Colors.DARK_BLUE, Colors.WHITE],
        ),
        content=Text(
            "Home",
            style=TextStyle(
                color=Styles.TEXT_COLOR,
                size=50,
                weight=FontWeight.BOLD,
            ),
        )
    )
    page.title = "Home"
    print("Ruta login:", page.route)

    return View(
        '/home',
        [
            home
        ],
        padding=0

    )
