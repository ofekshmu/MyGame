from enum import Enum, auto, unique

class Windows(Enum):
    MainMenu = auto()
    Settings = auto()
    # TODO add more here

class MainMenu(Enum):
    Exit = auto()
    LogIn = auto()
    
class Size(Enum):
    Small = (100, 25)
    Medium = (100, 40)
    Large = (150, 60)

    