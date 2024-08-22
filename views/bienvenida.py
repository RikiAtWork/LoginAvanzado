from threading import Timer
from flet import *
from flet_route import Params, Basket

class BienvenidaPage:
    def __init__(self, page: Page):
        self.page = page
        self.create_bienvenida_content()
        self.setup_page()

    def create_bienvenida_content(self):
        self.logo_container = Container(
            content=Image(src='./assets/logo.png'),
            scale=transform.Scale(0.0),  # Escala inicial (sin zoom)
            animate_scale=animation.Animation(
                duration=1000,  # Duración en milisegundos
                curve=AnimationCurve.BOUNCE_IN,  # Curva de animación suave
            ),
            col={"sm": 12, "md": 12, "lg": 6}
        )

        self.bienvenida_content = Container(
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[self.logo_container],
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER
                    ),
                ],
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            padding=padding.all(20),
            expand=True,
            image_src='./assets/welcome_background.png',
            image_fit=ImageFit.COVER,
        )

    def setup_page(self):
        self.main = SafeArea(
            content=self.bienvenida_content,
            expand=True
        )
        
        self.page.title = "Bienvenido"
        self.page.theme = Theme(color_scheme_seed="blue")

        # Configurar el manejador del ciclo de vida de la aplicación
        Timer(0.1, self.start_zoom_animation).start()  # Ejecutar después de un breve retraso

    def get_view(self):
        return View(
            '/',
            [self.main],
            padding=0
        )

    def start_zoom_animation(self):
        self.logo_container.scale = transform.Scale(1.0)  # Zoom completo
        self.page.update()  # Actualizo la página para aplicar la animación

        Timer(2.0, self.redirect_to_login).start()

    def redirect_to_login(self):
        self.page.go('/login') 


def Bienvenida(page: Page, params: Params, basket: Basket):
    bienvenida_page = BienvenidaPage(page)
    return bienvenida_page.get_view()
