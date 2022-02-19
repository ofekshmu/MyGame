import pygame
import pygame_gui

from header.enum import Size

class Button:

    def __init__(self,
                    location,
                    text = "",
                    size = Size.medium):
        
        self.location = location
        self.size = size
        self.text = text

        self.events = {}

        self.object = None


    def create(self, manager):
        self.object = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(self.location, self.size),
                                             text = self.text,
                                             manager = manager)
        return self

    def addEvent(self, event : pygame_gui, function):
        self.events[event] = function
        return self

    def setText(self, text):
        """
        Sets the Button's text
        """    
        self.object.set_text(text)
        return self