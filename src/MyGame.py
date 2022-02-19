from enum import Enum
import pygame
import pygame_gui
from src import Window
from header.enum import UI

class MyGame:
    
    def __init__(self, windows):
        """ 
        Gui initialize 
        @ windows: a list of strings indicating window names
        """
        pygame.init()
        #init windows
        
        self.windows = [Window(name) for name in windows]
        self.active_events = '' #TODO

    
    def addWindow(self):
        pass
    
    def window(self, window):
        return self.windows[window]

            

    def start(self):
        
        self.running = True

        while self.running:
            
            self.__EventHandler()
            self.__applyChanges()
            
            pygame.display.flip()
        
        pygame.quit()



    def switchWindows(self, window : Enum('Windows')):
        """
        Hides all windows, other than @ window
        @ window : window to show
        """
        for w in self.windows:
            if w == window:
                w.show()
            else:
                w.hide()

    def __EventHandler(self):
        for event in pygame.event.get():
            for e in self.active_events:
                if event.type == e:
                    print("") #TODO execute function according


    def __applyChanges(self):
        pass
