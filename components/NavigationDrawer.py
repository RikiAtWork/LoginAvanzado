from flet import *


class MyDrawer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        drawer = NavigationDrawer(
            controls=[
                Container(height=25),
                Image(
                    src="./assets/logo_color.png",
                    width=80
                ),
                Container(height=25),
                Divider(thickness=1, color="#2a68f7", height=0.2),
                Container(height=10),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.MEDICAL_SERVICES_OUTLINED, color=colors.BLACK),
                    label="Citas",
                    selected_icon_content=Icon(icons.MEDICAL_SERVICES, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.QUESTION_MARK_OUTLINED, color=colors.BLACK),
                    label="Cómo hacer auto entrada",
                    selected_icon_content=Icon(icons.QUESTION_MARK, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.PEOPLE_OUTLINED, color=colors.BLACK),
                    label="Paciente",
                    selected_icon_content=Icon(icons.PEOPLE, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.LOCAL_LIBRARY_OUTLINED, color=colors.BLACK),
                    label="Mis datos",
                    selected_icon_content=Icon(icons.LOCAL_LIBRARY, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.NEWSPAPER_OUTLINED, color=colors.BLACK),
                    label="Noticias",
                    selected_icon_content=Icon(icons.NEWSPAPER, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.ADD_CARD_OUTLINED, color=colors.BLACK),
                    label="Tarjeta Atenea",
                    selected_icon_content=Icon(icons.ADD_CARD, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.APARTMENT_OUTLINED, color=colors.BLACK),
                    label="Centros",
                    selected_icon_content=Icon(icons.APARTMENT, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.SETTINGS_OUTLINED, color=colors.BLACK),
                    label="Ajustes",
                    selected_icon_content=Icon(icons.SETTINGS, color=colors.WHITE),
                ),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.DELETE_OUTLINE, color=colors.BLACK),
                    label="Borrar registro de app",
                    selected_icon_content=Icon(icons.DELETE, color=colors.WHITE),
                ),
                Container(height=20),
                Divider(thickness=0.5, color=colors.BLACK54),
                NavigationDrawerDestination(
                    icon_content=Icon(icons.LOGOUT_OUTLINED, color=colors.BLACK),
                    label="Cerrar sesión",
                    selected_icon_content=Icon(icons.LOGOUT, color=colors.WHITE),
                ),
            ], bgcolor='white', indicator_color="#1f65f1", elevation=40
        )

        return drawer
