from enum import UI
import pygame,pygame_gui


class Window:

    def __init__(self,
                location = (0,0),
                size = (500,500),
                color = (255,255,255),
                user_interface = {}):

        # *******************************************************/
        #                   Pygame settings                      /
        # *******************************************************/
        self.surface = pygame.display.set_mode(size)
        self.surface.fill(pygame.Color(color))
        manager = pygame_gui.UIManager(size)        

        # *******************************************************/
        #                   self settings                        /
        # *******************************************************/
        self.userUI = {k:v.create(manager) for k,v in user_interface.items()}
    
    def setLocation(self):
        raise NotImplemented

    def hide(self):
        for v in self.userUI.values():
            v.hide()

    def show(self):
        for v in self.userUI.values():
            v.show()

    def exctractData(self):
        raise NotImplemented

    def color(self, color = '#FFFFFF'):
        """
        template '#??????' / (x,x,x) x is 8bit dec
        """
        self.surface.fill(pygame.Color(color))


