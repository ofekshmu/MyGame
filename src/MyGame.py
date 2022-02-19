import pygame
import pygame_gui
from UI.button import Button

from src.Window import Window
from header.Constants import Windows, MainMenu,Size

class MyGame:
    
    def __init__(self):

        pygame.init()

        # Define user interface for Window
        dict = {MainMenu.Exit: Button(location = (0,0),
                                      text = "",
                                      size = Size.medium
                                      ),
                MainMenu.LogIn: Button(location = (0,0),
                                      text = "",
                                      size = Size.medium
                                      )
                }

        # Build window and feed it with UI
        self.windows[Windows.MainMenu] = Window(location = (0,0),
                                                size = (500, 500),
                                                color = (255,255,255),
                                                user_interface = dict)

        

    def start(self):        

        self.__sys_msg("MyGame Started succssesfully.")    
        self.running = True

        while self.running:
            
            self.__EventHandler()
            pygame.display.flip()
        

    def __EventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.windows[Windows.MainMenu].get(MainMenu.Exit):
                    self.__CallBack_MainMenuExit()
                
            if event.type == pygame.QUIT:
                pygame.quit()


    
    def __switchWindows(self, window : Windows):
        """
        Hides all windows, other than @ window
        @ window : window to show
        """
        for w in self.windows:
            if w == window:
                w.show()
            else:
                w.hide()
   
    # ********************************************************/
    #                       Call Backs                        /
    # ********************************************************/
    def __CallBack_MainMenuExit(self):
        raise NotImplemented   

    # ********************************************************/
    #                       System Msg                        /
    # ********************************************************/
    def __sys_msg(self, msg):
        print(f"\n\t\tMyGame: System Message\n{msg}\n")




