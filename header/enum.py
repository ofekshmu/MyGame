from enum import Enum, unique

@unique
class UI(Enum):
    button = 1
    label = 2
    textBox = 3
    
class Sizes(Enum):
    small = (100, 25)
    medium = (100, 40)
    large = (150, 60)

    