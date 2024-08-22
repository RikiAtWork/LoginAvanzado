from flet import *
from components.Colors import Colors
import datetime


class ButtonAction(ElevatedButton):
    def __init__(self, text, height, function):
        super().__init__(
            text=text,
            height=height,
            on_click=function,
            color=Colors.WHITE,
            bgcolor=Colors.PINKRED,
            style=ButtonStyle(
                shape={
                    MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
                    MaterialState.HOVERED: RoundedRectangleBorder(radius=10),
                },
            )

        )


class TextButtonContainer(Container):
    def __init__(self, text, on_click, size, color, decoration, margin_left):
        super().__init__(
            content=TextButton(
                content=Text(
                    text,
                    size=size,
                    weight="w600",
                    color=color,
                    style=TextStyle(
                        decoration=decoration,
                        decoration_style=TextDecorationStyle.SOLID,
                        decoration_color=Colors.PINKRED
                    )
                ),
                on_click=on_click,
            ),
            margin=margin.only(left=margin_left)
        )


class FormTextField(TextField):
    def __init__(self, label, hint_text, prefix_icon, isPassword, can_reveal):
        super().__init__(
            height=50,
            label_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL, size=14),
            hint_style=TextStyle(color=Colors.WHITE, weight=FontWeight.NORMAL, size=14),
            label=label,
            hint_text=hint_text,
            color=Colors.WHITE,
            content_padding=10,
            border_color=Colors.WHITE,
            border_radius=5,
            prefix_icon=prefix_icon,
            password=isPassword,
            can_reveal_password=can_reveal
        )


class DateButton(ElevatedButton):
    def __init__(self, page: Page, height):
        self.page = page
        self.selected_date = None  # Almacena la fecha seleccionada
        self.date_button_text = Text(self.fecha_formateada(datetime.datetime.now()))

        self.date_picker = DatePicker(
            on_change=self.cambia_fecha,
            on_dismiss=self.fallo_data_picker,
            first_date=datetime.datetime(1950, 10, 1),
            last_date=datetime.datetime(2024, 10, 1),
        )

        super().__init__(
            content=Row(
                [
                    Icon(icons.CALENDAR_MONTH),
                    self.date_button_text
                ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
            ),
            on_click=self.open_date_picker,
            height=height,
            style=ButtonStyle(
                bgcolor=colors.WHITE,
                color=colors.BLACK,
                side={
                    MaterialState.DEFAULT: BorderSide(1, colors.WHITE),
                },
                shape={
                    MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
                }
            )
        )

    def fecha_formateada(self, fecha):
        if fecha is None:
            return "Seleccione una fecha"  # Texto por defecto cuando no hay fecha seleccionada
        return fecha.strftime("%d/%m/%Y")

    def open_date_picker(self, e):
        self.page.overlay.append(self.date_picker)
        self.page.update()
        self.date_picker.open = True
        self.page.update()

    def cambia_fecha(self, e):
        print(f"La fecha ha cambiado, su valor es {self.date_picker.value}")
        if self.date_picker.value:
            self.selected_date = self.date_picker.value
            self.date_button_text.value = self.fecha_formateada(self.selected_date)
        else:
            self.selected_date = None
            self.date_button_text.value = "Seleccione una fecha"
        self.page.update()

    def fallo_data_picker(self):
        print(f"No ha seleccionado fecha, valor es {self.selected_date}")

    @property
    def value(self):
        return self.selected_date
    

class CheckBox(Checkbox):
    def __init__(self, label, color, weight, value):
        super().__init__(
            label=label,
            label_style=TextStyle(color=color, weight=weight, size=14),
            value=value,
            active_color=Colors.AFFIDEA,
            check_color="white",
            hover_color=colors.BLUE_ACCENT_700,
            border_side=BorderSide(2, "white")
            
        )


class Spacer(Container):
    def __init__(self, height):
        super().__init__(
            height=height
        )

class Alert(AlertDialog):
    def __init__(self, page: Page, message, text):
        self.page = page
        super().__init__(
            title=Row(
                [
                    Icon(icons.ERROR, Colors.BLACK),
                    Text("Error", color=Colors.BLACK)
                ]
            ),
            content=Text(message, color=Colors.BLACK),
            bgcolor=Colors.WHITE_BLUE,
            surface_tint_color="blue",
            actions=[
                TextButton(content=Text(text, color=Colors.AFFIDEA), on_click=self.close_dialog)
            ],
            on_dismiss=self.close_dialog
        )
    
    def close_dialog(self, e):
        self.open = False  # Esto cierra el diálogo
        self.page.update()  # Actualiza la página para reflejar los cambios