from flet import *
from flet_route import Params, Basket
from components.AppBar import MyAppBar
from components.UserBar import MyUserBar
from components.Background import MyBackground
from components.citas.ButtonHistorico import MyButtonHistorico
from components.base_view import BaseView
from components.NavigationDrawer import MyDrawer


class Colors:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED_600 = "#E53935"
    BLUE_LIGHT = "#428aed"
    BLUE_DARK = "#5d7ae5"
    DARK_BLUE = "#0024ed"
    GRAY_LIGHT = "#f0f2fc"
    SOFT_BLUE = "#6f8dde"


class Styles:
    TEXT_COLOR = Colors.WHITE
    TEXT_SIZE = 16
    BUTTON_COLOR = Colors.BLACK


def HistoricoCita(page: Page, params: Params, basket: Basket):
    def obtenerDatos():
        datos = page.client_storage.get("data")
        return datos['Data']

    barCitasTexto = Container(
        width=page.window_max_width,
        padding=0,
        margin=0,
        height=40,
        bgcolor="#b8c9f8",
        content=Column(
            [
                Row(
                    [
                        Text("CITAS DE TODAS LAS FECHAS\nTODAS LAS ESPECIALIDADES - TODOS LOS CENTROS", size=10,
                             color=colors.BLACK, text_align=TextAlign.CENTER, style=TextStyle(letter_spacing=0))
                    ], alignment=MainAxisAlignment.CENTER, vertical_alignment=CrossAxisAlignment.CENTER
                ),
            ], alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    filtroButton = MyButtonHistorico("FILTRAR CITAS", icons.FILTER_ALT)
    verButton = MyButtonHistorico("VER TODAS", icons.REMOVE_RED_EYE)

    historico = Container(
        width=page.window_max_width,
        height=page.window_max_height,
        margin=0,
        content=Column(
            [
                barCitasTexto,
                Container(
                    margin=margin.only(top=page.window_max_height - 400),
                    content=Row(
                        [
                            filtroButton,
                            verButton
                        ], alignment=MainAxisAlignment.CENTER,
                    ),
                )
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )
    )

    imagen = Container(
        width=page.window_max_width,
        height=page.window_height / 1.5,
        padding=0,
        margin=0,
        content=Column(
            [
                Image(
                    src="./assets/atenea.png",
                    width=300,
                    height=300,
                    fit=ImageFit.CONTAIN,
                    opacity=0.1,
                ),
            ], alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    background = MyBackground()

    stack = Stack(
        [
            background.build(),
            imagen,
            historico
        ],
        width=page.window_max_width,
        height=page.window_max_height,
    )

    header = MyAppBar("HISTÓRICO DE CITAS", icons.MENU, "", page)
    user_bar = MyUserBar(page, f"{obtenerDatos()['Nomb']} {obtenerDatos()['Apel1']} {obtenerDatos()['Apel2']}")
    # navigation_bar = MyNavigationBar(page, 2)

    page.title = "Histórico de citas"
    theme = Theme()
    theme.page_transitions.android = PageTransitionTheme.NONE
    theme.page_transitions.ios = PageTransitionTheme.NONE
    theme.page_transitions.macos = PageTransitionTheme.NONE
    theme.page_transitions.linux = PageTransitionTheme.NONE
    theme.page_transitions.windows = PageTransitionTheme.NONE
    page.theme = theme
    print("Ruta login:", page.route)

    return BaseView(page, [header.build(), user_bar.build(), stack], '/historico', 2)
