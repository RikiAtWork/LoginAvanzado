from flet import *
from flet_route import Params, Basket

class Colors:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED_600 = "#E53935"
    BLUE_LIGHT = "#428aed"
    BLUE_DARK = "#7961ed"
    GRAY_LIGHT = "#f0f2fc"

class Styles:
    TEXT_COLOR = Colors.WHITE
    TEXT_SIZE = 16
    BUTTON_COLOR = Colors.BLACK

def Login(page: Page, params: Params, basket: Basket):
# Define constantes para colores y estilos


    # Función para crear un contenedor de texto
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

    # Función para crear un contenedor de botón de texto
    def text_button_container(text, on_click):
        return Container(
            content=TextButton(
                text,
                style=ButtonStyle(color=Styles.BUTTON_COLOR),
                on_click=on_click,
            )
        )

    # Calcula el ancho de un elemento como un porcentaje del ancho de la ventana
    def calculate_width(percentage):
        return page.window_width * percentage

    # Contenedor de login mejorado
    login = Container(
        width=page.window_width,
        height=page.window_height,
        margin=0,
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
                                label_style=TextStyle(color=Colors.WHITE, size=Styles.TEXT_SIZE),
                                hint_style=TextStyle(color=Colors.WHITE, size=Styles.TEXT_SIZE),
                                label="Usuario",
                                hint_text='DNI / NIF / Pasaporte',
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
                                label_style=TextStyle(color=Colors.WHITE, size=Styles.TEXT_SIZE),
                                label="Contraseña",
                                height=50,
                                border_color=Colors.WHITE,
                                border_radius=10,
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
    print("Ruta login:", page.route)

    return View(
        '/',
        [login]
    )
