from flet import *


class MyUserBar(UserControl):
    def __init__(self, page, fusuario):
        super().__init__()
        self.page = page
        self.usuario = fusuario

    def build(self):
        my_user_bar = Container(
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.bottom_right,
                colors=["#ec008c", "#fc6767"]
            ),
            width=self.page.window_max_width,
            height=56,
            content=Row(
                [
                    Column(
                        [
                            Container(
                                width=50,
                                height=56,
                                margin=margin.only(left=-5),
                                content=Icon(icons.PEOPLE_ALT,
                                             color=colors.WHITE,
                                             size=20)
                            )
                        ]

                    ),
                    Column(
                        [
                            Container(
                                width=200,
                                padding=5,
                                content=Text(
                                    f"{self.usuario}",
                                    style=TextStyle(
                                        size=16,
                                        color=colors.WHITE,
                                        weight=FontWeight.W_600)
                                )
                            )
                        ], alignment=MainAxisAlignment.CENTER,
                    ),
                    Column(
                        [
                            Container(
                                width=60,
                                height=56,
                                margin=margin.only(left=55),
                                content=IconButton(
                                    content=Icon(
                                        icons.QR_CODE,
                                        color=colors.WHITE,
                                        size=40
                                    )
                                ),
                            )
                        ], alignment=MainAxisAlignment.END

                    ),
                ], alignment=MainAxisAlignment.SPACE_AROUND
            ),
        )

        return my_user_bar
