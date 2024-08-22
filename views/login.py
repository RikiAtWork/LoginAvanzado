
import asyncio
import aiohttp
import requests
from flet import *
from flet_route import Params, Basket

# Mis recursos
from views.encryption import Encrypt
from components.Colors import Colors
from components.FormFields import FormTextField, TextButtonContainer, Spacer, ButtonAction, Alert


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.usuario_field = FormTextField("Usuario", "DNI / NIF / Pasaporte", icons.PERSON, False, False)
        self.password_field = FormTextField("Contraseña", "", icons.LOCK, True, True)
        self.login_button = ButtonAction("INICIAR SESIÓN", 50, self.button_clicked)

        self.create_login_content()
        self.setup_page()

    async def login_api(self, usuario, password):
        url = "https://integraciones.clinica-atenea.com:58000/api/v1/app/Login"

        auth = aiohttp.FormData()
        auth.add_field('DNI', usuario)
        auth.add_field('Pwd', password)

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=auth) as response:
                return await response.json(), response.status
            
    async def button_clicked(self, e):
        usuario = self.usuario_field.value
        password = self.password_field.value

        encrypted = Encrypt.my_encrypt(password)
        print("Pass encriptado:", encrypted)

        if usuario and password:
            self.login_button.disabled = True
            self.page.update()

            try:
                data, status = await self.login_api(usuario, encrypted)
                print("Datos de respuesta:", data, status)
                await self.handle_response(data, status)    
            except Exception as error:
                print("Ha ocurrido un error: ", error)
                self.show_error_message("Ha ocurrido un error inesperado.")
            finally:
                self.login_button.disabled = False
                self.page.update()
    
    async def handle_response(self, data, status):
        error = data['Error']
        if error == False:
            try:
                await self.page.client_storage.set_async("data", data)
                print("Se ha almacenado correctamente")
                self.page.go('/home')
            except Exception as e:
                print(f"Error al almacenar en clientStorage: {e}")
                self.show_error_message("No se pudo almacenar la información. Inténtelo de nuevo.")
        elif error == True:
            self.show_error_message("Usuario o contraseña incorrectos.")
        else:
            self.show_error_message("Error desconocido. Inténtelo de nuevo más tarde.")

    def show_error_message(self, message):
        alert_dialog = Alert(self.page, message, "Cerrar")

        self.page.open(alert_dialog)
        self.page.update()

    def create_login_content(self):
        self.login_content = Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            Container(
                                margin=margin.only(bottom=20),
                                content=Image(src='./assets/logo.png'),
                                col={"sm": 8, "md": 10, "lg": 4}
                            ),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Container(
                                content=self.usuario_field,
                                col={"sm": 8, "md": 10, "lg": 4}
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Container(
                                content=self.password_field,
                                col={"sm": 8, "md": 10, "lg": 4}
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Spacer(25),
                    ResponsiveRow(
                        controls=[
                            Container(
                                content=self.login_button,
                                col={"sm": 8, "md": 10, "lg": 4}
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    ResponsiveRow(
                        controls=[
                            Container(
                                content=TextButtonContainer(
                                    '¿RECUPERAR CONTRASEÑA?',
                                    lambda _: self.page.go('/'),
                                    14,
                                    Colors.WHITE,
                                    TextDecoration.NONE,
                                    0
                                ),
                                col={"sm": 8, "md": 10, "lg": 4}
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    Spacer(20),
                    ResponsiveRow(
                        controls=[
                            Container(
                                content=Row(
                                    controls=[
                                        Text(
                                            "¿No tienes una cuenta?",
                                            size=14,
                                            weight="w600",
                                            color=Colors.BLACK,
                                        ),
                                        TextButtonContainer(
                                            'Créala',
                                            lambda _: self.page.go('/registro'),
                                            14,
                                            Colors.PINKRED,
                                            TextDecoration.UNDERLINE,
                                            -10
                                        )
                                    ],
                                    alignment=MainAxisAlignment.CENTER
                                ),
                                col={"sm": 8, "md": 10, "lg": 4}
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=20
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
            content=self.login_content,
            expand=True
        )

        self.page.title = "Iniciar sesión"
        self.page.theme = Theme(color_scheme_seed="blue")

        print("Ruta login:", self.page.route)

    def get_view(self):
        return View(
            '/login',
            [self.main],
            padding=0
        )


def Login(page: Page, params: Params, basket: Basket):
    login_page = LoginPage(page)
    return login_page.get_view()
