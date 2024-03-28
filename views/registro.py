import datetime
from flet import *
from flet_route import Params, Basket


def Registro(page: Page, params: Params, basket: Basket):
    def cambia_fecha(e):
        print(f"La fecha ha cambiado, su valor es {date_picker.value}")

    def fallo_data_picker(e):
        print(f"No ha seleccionado fecha, valor es {date_picker.value}")

    date_picker = DatePicker(
        on_change=cambia_fecha,
        on_dismiss=fallo_data_picker,
        first_date=datetime.datetime(2023, 10, 1),
        last_date=datetime.datetime(2024, 10, 1),

    )

    fecha_formateada = datetime.datetime.now().strftime("%d/%m/%Y")

    page.overlay.append(date_picker)

    date_button = ElevatedButton(
        f"{fecha_formateada}",
        icon=icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
        width=page.window_width * 0.7,
    )

    registro = Container(
        width=page.window_width,
        height=page.window_height,
        gradient=LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=["#7961ed", "#428aed", "#f0f2fc"],
        ),
        content=Column(
            controls=[
                Row(
                    controls=[
                        Container(
                            width=260,
                            margin=margin.only(top=50, bottom=50),
                            content=Text("Registro",
                                         style=TextStyle(
                                             color=colors.WHITE,
                                             size=60,
                                             weight=FontWeight.W_900,
                                         ),
                                         )
                        ),

                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            TextField(
                                width=page.window_width * 0.7,
                                hint_text="DNI / NIF / Pasaporte",
                                hint_style=TextStyle(color=colors.WHITE, weight=FontWeight.NORMAL),
                                height=50,
                                border_color=colors.WHITE,
                                border_radius=10,
                                prefix_icon=icons.PERSON,
                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            TextField(
                                width=page.window_width * 0.7,
                                hint_text="Teléfono móvil (9 digitos)",
                                hint_style=TextStyle(color=colors.WHITE, weight=FontWeight.NORMAL),
                                height=50,
                                border_color=colors.WHITE,

                                border_radius=10,
                                prefix_icon=icons.PHONE,
                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            TextField(
                                width=page.window_width * 0.7,
                                hint_text="Contraseña",
                                hint_style=TextStyle(color=colors.WHITE, weight=FontWeight.NORMAL),
                                height=50,
                                border_color=colors.WHITE,
                                border_radius=10,
                                prefix_icon=icons.LOCK,
                                password=True,
                                can_reveal_password=True
                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            TextField(
                                width=page.window_width * 0.7,
                                hint_text="Repita contraseña",
                                hint_style=TextStyle(color=colors.WHITE, weight=FontWeight.NORMAL),
                                height=50,
                                border_color=colors.WHITE,
                                border_radius=10,
                                prefix_icon=icons.LOCK,
                                password=True,
                                can_reveal_password=True
                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            date_button,
                            margin=margin.only(bottom=5)
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            Text(
                                "App sólo para pacientes de Clínica Atenea",
                                size=12,
                                style=TextStyle(color=colors.BLACK,
                                                italic=True,
                                                ),

                            )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER

                ),
                Row(
                    controls=[
                        Container(
                            margin=margin.only(top=50),
                            content=ElevatedButton("SOLICITAR REGISTRO",
                                                   width=page.window_width * 0.7,
                                                   on_click=lambda _: page.go('/'),
                                                   bgcolor=colors.RED_600,
                                                   color=colors.WHITE,
                                                   ),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Container(
                            margin=margin.only(top=10),
                            content=Checkbox("He leído ",
                                             value=False,
                                             active_color=colors.BLUE,
                                             label_style=TextStyle(color=colors.BLACK)
                                             )
                                             
                        ), Container(
                            margin=margin.only(left=-10, top=10),
                            content=Text("las condiciones legales",
                                         color=colors.BLUE_ACCENT_400,
                                         style=TextStyle(weight=FontWeight.W_600)
                                         )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
            ],
        )
    )

    page.title = "Registrarse"
    page.theme = Theme(color_scheme_seed="blue")
    print("Ruta login:", page.route)

    return View(
        '/registro',
        [registro]
    )
