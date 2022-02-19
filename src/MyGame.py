from enum import Enum
import pygame
from header.enum import UI

class MyGame:
    
    def __init__(self, windows):
        """ 
        Gui initialize 
        @ windows: a list of strings indicating window names
        """

        self.windows = Enum('Windows', windows)
        

    def add(self, ui : UI,
                window : Enum('Windows')
                ):
        """ add UI to screen
        @ ui : enum of User interface to add
        @ window : associated window 

        """
        pass
            

    def start(self):
        
        self.running = True

        while self.running:
            
            self.__EventHandler()
            self.__applyChanges()



    def switchWindows(self, windows : Enum('Windows')):
        pass

    def __EventHandler(self):
        pass

    def __applyChanges(self):
        pass
