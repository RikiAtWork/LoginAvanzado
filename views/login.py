from flet import *
from flet_route import Params, Basket

class Colors:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED_600 = "#E53935"
    BLUE_LIGHT = "#428aed"
    BLUE_DARK = "#7961ed"
    DARK_BLUE = "#0024ed"
    GRAY_LIGHT = "#f0f2fc"

class Styles:
    TEXT_COLOR = Colors.WHITE
    TEXT_SIZE = 16
    BUTTON_COLOR = Colors.BLACK

def Login(page: Page, params: Params, basket: Basket):


    def text_container(text, size=60, weight=FontWeight.W_900, margin_top=0, margin_bottom=0):
        return Container(
            width=170,
            margin=margin.only(top=margin_top, bottom=margin_bottom),
            content=Text(text,
                        style=TextStyle(
                            color=Colors.WHITE,
                            size=size,
                            weight=weight,
                        ),
                        )
        )

    def text_button_container(text, on_click):
        return Container(
            content=TextButton(
                text,
                style=ButtonStyle(color=Styles.BUTTON_COLOR),
                on_click=on_click,
            )
        )

    def calculate_width(percentage):
        return page.window_width * percentage

    login = Container(
        width=page.window_width,
        height=page.window_height,
        margin=0,
        padding=0,
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=[Colors.BLUE_DARK, Colors.BLUE_LIGHT, Colors.GRAY_LIGHT],
        ),
        content=Column(
            controls=[
                Row(
                    controls=[
                        text_container("Login", margin_top=50, margin_bottom=50),
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            margin=margin.only(bottom=10),
                            content=TextField(
                                width=calculate_width(0.7),
                                label_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL),
                                hint_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL),
                                label="Usuario",
                                hint_text='DNI / NIF / Pasaporte',
                                color= Colors.WHITE,
                                height=50,
                                border_color=Colors.WHITE,
                                border_radius=10,
                                prefix_icon=icons.PERSON,
                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            content=TextField(
                                width=calculate_width(0.7),
                                label_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL),
                                label="Contraseña",
                                height=50,
                                border_color=Colors.WHITE,
                                border_radius=10,
                                color=Colors.WHITE,
                                prefix_icon=icons.LOCK,
                                password=True,
                                can_reveal_password=True
                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            margin=margin.only(top=50),
                            content=ElevatedButton("INICIAR SESIÓN",
                                                width=calculate_width(0.7),
                                                on_click=lambda _: page.go('/'),
                                                bgcolor=Colors.RED_600,
                                                color=Colors.WHITE,
                                                ),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            width=220,
                            margin=margin.only(top=50),
                            content=text_button_container('¿RECUPERAR CONTRASEÑA?', lambda _: page.go('/')),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            content=text_button_container('REGISTRARSE', lambda _: page.go('/registro')),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                )
            ],
        )
    )
    page.title = "Iniciar sesión"
    page.theme = Theme(color_scheme_seed="blue")
    print("Ruta login:", page.route)

    return View(
        '/',
        [login]
    )
