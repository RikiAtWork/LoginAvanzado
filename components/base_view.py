from typing import List

from flet import *
from components.NavigationBar import MyNavigationBar
from components.NavigationDrawer import MyDrawer


def BaseView(page: Page, content: List[Control], ruta, index):
    navigation_bar = MyNavigationBar(page, index)
    navigation_drawer = MyDrawer()
    page.drawer = navigation_drawer.build()
    # Mirar a ver si lo puedo hacer como contenedor o intentar resolverlo
    return View(
        ruta,
        [
            *content,
            page.drawer,
            navigation_bar.build(),
        ],
        padding=0,
        spacing=0
    )
