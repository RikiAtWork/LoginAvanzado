from flet import *
from flet_route import Params, Basket
from components.AppBar import MyAppBar
from components.UserBar import MyUserBar


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
        return datos['Data']

    def obtenerCitas():
        citas = obtenerDatos()['Citas']
        lista_citas = citas[0]
        print(lista_citas)
        return lista_citas

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
        height=125,
        bgcolor=colors.WHITE70,
        border_radius=10,
        border=border.all(2, "#FFFFFF"),
        content=Column(
            [
                Row(
                    [
                        Text(f"{obtenerCitas()['Especialidad']}",
                             color=colors.BLACK,
                             weight=FontWeight.W_700,
                             style=TextStyle(
                                 decoration=TextDecoration.UNDERLINE,
                                 decoration_color=colors.BLACK,
                                 decoration_thickness=1,
                             )
                             ),
                        Text(f"(Clínica de L'Eliana)",
                             color=colors.BLACK,
                             weight=FontWeight.W_700,
                             ),

                    ], alignment=MainAxisAlignment.SPACE_EVENLY,
                    spacing=0,
                ),
                Row(
                    [
                        Text(f"{obtenerCitas()['Especialista']}",
                             color=colors.BLACK,
                             italic=True,
                             size=11)

                    ], alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                ),
                Row(
                    [
                        Text(
                            f"{obtenerCitas()['Fecha']} - {obtenerCitas()['hora']}:{obtenerCitas()['minuto']} h. ",
                            color=colors.BLACK,
                            size=12),
                        Text(
                            f"- {obtenerCitas()['VisitTypeName']}",
                            color=colors.GREY_600,
                            size=12
                        ),
                    ], alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                ),
                Row(
                    [
                        TextButton(
                            width=90,
                            height=30,
                            style=ButtonStyle(
                                padding=5,
                                bgcolor=colors.RED_600,
                                shape={
                                    MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                    MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                },
                            ),
                            content=Row(
                                [
                                    Icon(name=icons.EDIT_OUTLINED, color=colors.WHITE, size=14),
                                    Text("CAMBIAR", size=12, color=colors.WHITE)
                                ]
                            )
                        ),
                        TextButton(
                            width=90,
                            height=30,
                            style=ButtonStyle(
                                padding=5,
                                bgcolor=colors.RED_600,
                                shape={
                                    MaterialState.DEFAULT: RoundedRectangleBorder(radius=10),
                                    MaterialState.HOVERED: RoundedRectangleBorder(radius=15),
                                },
                            ),
                            content=Row(
                                [
                                    Icon(name=icons.DELETE, color=colors.WHITE, size=14),
                                    Text("ANULAR", size=12, color=colors.WHITE)
                                ]
                            )
                        )
                    ], alignment=MainAxisAlignment.CENTER
                )
            ]
        )
    )

    background = Container(
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
        width=page.window_max_width,
        height=page.window_max_height,
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

    stack = Stack(
        [
            background,
            imagen,
            home,
        ],
        width=page.window_max_width,
        height=page.window_max_height,

    )

    page.title = "Home"
    print("Ruta login:", page.route)

    header = MyAppBar("PRÓXIMAS CITAS", icons.MENU, "")
    user_bar = MyUserBar(page, f"{obtenerDatos()['Nomb']} {obtenerDatos()['Apel1']} {obtenerDatos()['Apel2']}")

    return View(
        '/home',
        [
            header.build(),
            user_bar.build(),
            stack,
            navigation_bar
        ],
        padding=0,
        spacing=0

    )
