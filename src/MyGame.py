from enum import Enum
import pygame
from Main import Windows
from header.enum import UI

class MyGame:
    
    def __init__(self, windows):
        """ 
        Gui initialize 
        @ windows: a list of strings indicating window names
        """
        pygame.init()
        #init windows
        
        self.windows = Enum('Windows', windows)
        

    # def add(self, ui : UI,
    #             window : Enum('Windows')
    #             ):
    #     """ add UI to screen
    #     @ ui : enum of User interface to add
    #     @ window : associated window 

    #     """
    #     pass

    def window(self, window):
        return self.windows[window]

            

    def start(self):
        
        self.running = True

        while self.running:
            
            self.__EventHandler()
            self.__applyChanges()
            
            pygame.display.flip()
        
        pygame.quit()



    def switchWindows(self, windows : Enum('Windows')):
        pass

    def __EventHandler(self):
        pass

    def __applyChanges(self):
        pass
