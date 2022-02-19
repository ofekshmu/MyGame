import pygame

pygame.init()
dim_lst = pygame.display.get_desktop_sizes()
(Width, Height) = dim_lst[0] if len(dim_lst) > 0 else dim_lst 

Center_X = Width/2
Center_Y = Height/2
