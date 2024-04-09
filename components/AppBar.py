from flet import *


class MyAppBar(UserControl):

    def __init__(self, ftexto, ficono, fsrc, page):
        super().__init__()
        self.texto = ftexto
        self.icono = ficono
        self.src = fsrc
        self.page = page

    def open_drawer(self, e):
        if not self.page.drawer.open:
            print("Abriendo el drawer")
            self.page.drawer.open = True
        else:
            print("El drawer ya está abierto")
        self.page.update()
        self.page.drawer.update()

    def build(self):
        my_app_bar = AppBar(
            leading=IconButton(
                icon=self.icono,
                on_click=self.open_drawer),
            leading_width=40,
            title=Text(f"{self.texto}",
                       style=TextStyle(
                           size=16
                       )),
            color=colors.WHITE,
            bgcolor="#2a68f7",

            actions=[
                IconButton(
                    content=Image(
                        src="./assets/logo.png",
                        width=80
                    ),
                ),

            ]
        )

        return my_app_bar
