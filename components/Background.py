from flet import *
import math

class Colors:
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    RED_600 = "#E53935"
    PURPLE = "#613dc1"
    # BLUE_DARK = "#5d7ae5"
    AFFIDEA = "#0082d4"
    WHITE_BLUE = "#f0f2fc"

    DARK_BLUE = "#0024ed"
    PINKRED = "#d1105a"



class MyBackground(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        background = Container(
            margin=0,
            padding=20,
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=Alignment(0.8, 1),
                colors=[
                    "#FFFFFF",
                    "#6e91f3",

                ],
                tile_mode=GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            ),

        )

        return background
