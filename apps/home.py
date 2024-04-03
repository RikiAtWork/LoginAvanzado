from flet import *
from flet_route import Params, Basket
import math


# import hashlib

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


def Home(page: Page, params: Params, basket: Basket):
    def obtenerDatos():
        datos = page.client_storage.get("data")
        print("Vista Home:")
        print(datos)
        return datos['Data']

    especialidad = obtenerDatos()['Citas'][14]
    print(especialidad)
    appbar = AppBar(
        leading=Icon(icons.HOME),
        leading_width=40,
        title=Text("PRÓXIMAS CITAS",
                   style=TextStyle(
                       size=16
                   )),
        color=colors.WHITE,
        bgcolor="#2a68f7",
        actions=[
            IconButton(
                content=Image(
                    src="./assets/logo.png",
                    width=80
                ),
            ),

        ]
    )

    usuario_bar = Container(
        width=page.window_width,
        height=56,
        bgcolor="#ffadc0",
        content=Row(
            [
                Column(
                    [
                        Container(
                            width=50,
                            height=56,
                            margin=margin.only(left=-5),
                            content=Icon(icons.PEOPLE_ALT,
                                         color=colors.BLACK,
                                         size=20)
                        )
                    ]

                ),
                Column(
                    [
                        Container(
                            width=200,
                            content=Text(
                                f"{obtenerDatos()['Nomb']} {obtenerDatos()['Apel1']} {obtenerDatos()['Apel2']}",
                                style=TextStyle(
                                    size=16,
                                    color=colors.BLACK,
                                    weight=FontWeight.BOLD)
                            )
                        )
                    ], alignment=MainAxisAlignment.CENTER,
                ),
                Column(
                    [
                        Container(
                            width=50,
                            height=56,
                            margin=margin.only(left=40),
                            content=IconButton(
                                content=Image(
                                    src="./assets/qr.png",
                                    width=30
                                ),
                            ),
                        )
                    ]

                ),
            ],
        )
    )

    nueva_cita = Container(
        margin=margin.only(top=50),
        content=ElevatedButton(icon=icons.ADD,
                               text=" NUEVA CITA",
                               color=Colors.WHITE,
                               bgcolor=colors.RED_600,
                               style=ButtonStyle(
                                   shadow_color=colors.BLACK,
                                   padding=10,
                                   shape={
                                       MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                       MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                   },
                               )
                               ),
    )

    navigation_bar = NavigationBar(
        bgcolor="#2a68f7",
        shadow_color=colors.DEEP_PURPLE,
        indicator_color="#2251bf",
        destinations=[
            NavigationDestination(icon=icons.CALENDAR_MONTH, label="Citas pendientes"),
            NavigationDestination(icon=icons.ADD, label="Nueva cita"),
            NavigationDestination(icon=icons.LIST, label="Histórico de citas"),

        ]
    )

    card = Container(
        width=page.window_width - 100,
        height=100,
        bgcolor=colors.GREY_50,
        border_radius=10,
        border=border.all(1.5, "#ffffff"),
        # content=Column(
        #     [
        #         Row(
        #             [
        #                 Text(f"{especialidad}")
        #             ]
        #         )
        #     ]
        # )
    )

    background = Container(
        width=page.window_width,
        height=page.window_height,
        margin=0,
        padding=20,
        gradient=LinearGradient(
            begin=alignment.top_left,
            end=Alignment(0.8, 1),
            colors=[
                "#FFFFFF",
                "#6e91f3",
            ],
            tile_mode=GradientTileMode.MIRROR,
            rotation=math.pi / 3,
        ),

    )

    home = Container(
        width=page.window_width,
        height=page.window_height,
        margin=0,
        padding=20,
        content=Column(
            [
                card,
                nueva_cita
            ],
            horizontal_alignment=CrossAxisAlignment.CENTER,

        )
    )

    imagen = Container(
        width=page.window_width,
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

    stack = Stack(
        [
            background,
            imagen,
            home
        ],
        width=page.window_width,
        height=page.window_height,

    )

    page.title = "Home"
    print("Ruta login:", page.route)

    return View(
        '/home',
        [
            appbar,
            usuario_bar,
            stack,
            navigation_bar
        ],
        padding=0,
        spacing=0

    )
