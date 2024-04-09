from flet import *


class MyCardClinica(UserControl):
    def __init__(self, page, fnomclinica, fdireccion, fpoblacion, furl):
        super().__init__()
        self.page = page
        self.nomclinica = fnomclinica
        self.direccion = fdireccion
        self.poblacion = fpoblacion
        self.url = furl

    def build(self):
        mycardclinica = TextButton(
            content=Container(
                width=self.page.window_width - 80,
                height=120,
                padding=20,
                bgcolor=colors.WHITE60,
                border_radius=10,
                border=border.all(2, "#FFFFFF"),
                content=Row(
                    [
                        Column(
                            [
                                Image(
                                    src=f"{self.url}",
                                    width=120,
                                    height=80,
                                    fit=ImageFit.COVER,
                                    color_blend_mode=BlendMode.COLOR_BURN
                                ),

                            ],
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=0, height=120
                        ),
                        Column(
                            [
                                Text(f"{self.nomclinica}", size=14, color=colors.BLACK,
                                     style=TextStyle(letter_spacing=0)),
                                Text(f"{self.direccion}", size=14, color=colors.BLACK,
                                     style=TextStyle(letter_spacing=0)),
                                Text(f"{self.poblacion}", size=14, color=colors.BLACK, weight=FontWeight.W_700,
                                     style=TextStyle(letter_spacing=0))

                            ],
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.START,
                            height=80
                        )
                    ]
                )
            )
        )

        return mycardclinica
