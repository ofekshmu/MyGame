from enum import UI
import pygame


class Window:

    def __init__(self,
                id,
                user_interface,
                location,
                size = (500,500)):
        """
        @ size: a tuple containing window size
        """
        self.surface = pygame.display.set_mode(size)

    def UI(self, ui : UI):
        #return the UI class
        pass
    
    def setLocation(self):
        raise NotImplemented

    def hide(self):
        raise NotImplemented

    def show(self):
        raise NotImplemented

    def exctractData(self):
        raise NotImplemented

    def color(self, color = '#FFFFFF'):
        """
        template '#??????' / (x,x,x) 0 <= x <= 255
        """
        self.surface.fill(pygame.Color(color))
        return self


