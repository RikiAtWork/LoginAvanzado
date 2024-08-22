from flet import *
from flet_route import *

from views.bienvenida import Bienvenida
from views.login import Login
from views.registro import Registro
from apps.home import Home
from apps.nuevaCita import NuevaCita
from apps.historico import HistoricoCita
from components.AppBar import MyAppBar


def main(page: Page):
    page.padding = 0
    page.spacing = 0

    page.window.always_on_top = True
    # page.window.width = 390
    # page.window.height = 844
    # page.window.max_width = 800
    # page.window.max_height = 844

    # Configuración de la localización
    page.locale_configuration = LocaleConfiguration(
        supported_locales=[
            Locale("de", "DE"),  # German, Germany
            Locale("fr", "FR"),  # French, France
            Locale("en", "US"),   # English
            Locale("es"),        # Spanish
        ],
        current_locale=Locale("es"),
    )

    

    page.fonts = {
        "Poppins": "https://fonts.google.com/share?selection.family=Onest:wght@100..900"
    }
    page.theme = Theme(font_family="Poppins")

    # Configuración del tema y transiciones
    theme = Theme()
    theme.page_transitions.android = PageTransitionTheme.ZOOM
    theme.page_transitions.ios = PageTransitionTheme.ZOOM
    theme.page_transitions.macos = PageTransitionTheme.ZOOM
    theme.page_transitions.linux = PageTransitionTheme.ZOOM
    theme.page_transitions.windows = PageTransitionTheme.ZOOM
    page.theme = theme

    # Configuración del drawer (navegación lateral)
    page.drawer = NavigationDrawer()

    # Definimos rutas de la app
    app_routes = [
        path('/', clear=True, view=Bienvenida),
        path('/login', clear=True, view=Login),
        path('/registro', clear=True, view=Registro),
        path('/home', clear=True, view=Home, ),
        path('/nueva_cita', clear=True, view=NuevaCita),
        path('/historico', clear=True, view=HistoricoCita),
    ]

    # Definir breakpoints responsivos
    # page.responsive_breakpoints = {
    #     "small": 480,    # Móvil pequeño
    #     "medium": 768,   # Tablet
    #     "large": 1024,   # Laptop pequeño o tablet grande
    #     "xlarge": 1440   # Laptop grande o monitor
    # }

    Routing(page=page, app_routes=app_routes)
    page.go(page.route)


if __name__ == '__main__':
    app(target=main, assets_dir="assets")
