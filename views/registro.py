from flet import *
from flet_route import Params, Basket
from components.Colors import Colors
from components.FormFields import FormTextField, TextButtonContainer, Spacer, DateButton, CheckBox, ButtonAction


class RegistroPage:
    def __init__(self, page: Page):
        self.page = page

        self.dni_field = FormTextField("DNI / NIF / Pasaporte", "", icons.PERSON, False, False)
        self.telefono_field = FormTextField("Teléfono móvil (9 dígitos)", "", icons.PHONE, False, False)
        self.password_field = FormTextField("Contraseña", "", icons.LOCK, True, True)
        self.repeat_password_field = FormTextField("Repita contraseña", "", icons.LOCK, True, True)
        self.date_picker_field = DateButton(self.page, 50)
        self.condiciones_field = CheckBox("He leído", Colors.BLACK, "w600", False)

        self.register_button = ButtonAction("SOLICITAR REGISTRO", 50, self.on_registro_click)

        self.create_register_content()
        self.setup_page()
    
    # Se implementará en adelante
    def register_api(self, dni, telefono, password):
        pass

    def on_registro_click(self, e):
        print("DNI / NIF / Pasaporte:", self.dni_field.value)
        print("Teléfono móvil:", self.telefono_field.value)
        print("Contraseña:", self.password_field.value)
        print("Repita contraseña:", self.repeat_password_field.value)
        print("Fecha de nacimiento:", self.date_picker_field.value)
        print("¿Ha aceptado condiciones legales?", self.condiciones_field.value)

        # Navegar a otra ruta (por ejemplo, '/')
        self.page.go('/')

    def create_register_content(self):
        self.register_content = Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            Container(
                                margin=margin.only(bottom=20),
                                content=Image(src='./assets/logo.png'),
                                col={"sm": 10, "md": 10, "lg": 4}
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[Container(content=self.dni_field, col={"sm": 10, "md": 10, "lg": 4})],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[Container(content=self.telefono_field, col={"sm": 10, "md": 10, "lg": 4})],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[Container(content=self.password_field, col={"sm": 10, "md": 10, "lg": 4})],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[Container(content=self.repeat_password_field, col={"sm": 10, "md": 10, "lg": 4})],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[Container(content=self.date_picker_field, col={"sm": 10, "md": 10, "lg": 4})],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    Spacer(10),
                    ResponsiveRow(
                        controls=[Container(
                                    content=Text(
                                        "App sólo para pacientes de Clínica Atenea",
                                        size=12,
                                        style=TextStyle(color=colors.BLACK,
                                                        italic=True,
                                                        ),
                                    ),
                                    alignment=alignment.center,
                                    col={"sm": 10, "md": 10, "lg": 4} 
                                )
                                ],
                                alignment=MainAxisAlignment.CENTER
                    ),
                    Spacer(10),
                    ResponsiveRow(
                        controls=[Container(
                                content=self.register_button,
                                col={"sm": 10, "md": 10, "lg": 4}
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Container(
                                content=Row(
                                    controls=[
                                        self.condiciones_field,
                                        TextButtonContainer(
                                            'las condiciones legales',
                                            lambda _: self.page.go('/registro'),
                                            14,
                                            colors.BLUE_ACCENT_400,
                                            TextDecoration.NONE,
                                            -15
                                        )
                                    ],
                                    alignment=MainAxisAlignment.CENTER
                                ),
                                col={"sm": 10, "md": 10, "lg": 4}
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            padding=padding.all(20),
            expand=True,
            image_src='./assets/background.png',
            image_fit=ImageFit.COVER,
            # gradient=LinearGradient(
            #     begin=alignment.top_center,
            #     end=alignment.bottom_center,
            #     colors=[Colors.PURPLE, Colors.AFFIDEA, Colors.WHITE_BLUE],
            #     stops=[0.2, 0.6, 1.0]
            # ),
        )

    def setup_page(self):
        self.main = SafeArea(
            content=self.register_content,
            expand=True
        )

        self.page.title = "Registrarse"
        self.page.theme = Theme(color_scheme_seed="blue")

        print("Ruta:", self.page.route)

    def get_view(self):
        return View(
            '/registro',
            [self.main],
            padding=0
        )


def Registro(page: Page, params: Params, basket: Basket):
    register_page = RegistroPage(page)
    return register_page.get_view()
