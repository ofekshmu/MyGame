from MyGame import MyGame
from enum import Enum

from header.enum import UI
from UI.button import Button
from header.enum import Size

Windows = Enum("Windows",['menu','settings'])

gui = MyGame(['main','logged','settings'])


gui.window(Windows.main).UI(UI.Button) \
                        .location((100,100)) \
                        .size(Size.medium) \
                        .text("button caption")

Button().location((10,10)) \
    .text