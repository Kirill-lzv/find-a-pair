import pygame
from settings import size, clock
from menu import start_screen
from first_level import first_l



def color():
    PINK = 255, 228, 181
    return PINK



pygame.init()
screen = pygame.display.set_mode(size)
start_screen(screen, clock)

first_l()





