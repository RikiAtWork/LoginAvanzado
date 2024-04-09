from flet import *


class MyNavigationBar(UserControl):

    def __init__(self, page, index):
        super().__init__()
        self.page = page
        self.selected_index = index

    def change_page(self, index):
        print(index)

        if index == 0:
            self.page.go("/home")
        if index == 1:
            self.page.go("/nueva_cita")
        if index == 2:
            self.page.go("/historico")

        # page.update()

    def build(self):
        # print(f"Indice del Nav Bottom: {self.selected_index}")
        navigation_bar = NavigationBar(
            bgcolor="#2a68f7",
            shadow_color=colors.DEEP_PURPLE,
            selected_index=self.selected_index,
            indicator_color="#2251bf",
            on_change=lambda e: self.change_page(e.control.selected_index),
            destinations=[
                NavigationDestination(icon_content=Icon(icons.CALENDAR_MONTH, color=colors.WHITE), label="Citas pendientes"),
                NavigationDestination(icon_content=Icon(icons.ADD, color=colors.WHITE), label="Nueva cita"),
                NavigationDestination(icon_content=Icon(icons.LIST, color=colors.WHITE), label="Histórico de citas"),

            ]
        )

        return navigation_bar
