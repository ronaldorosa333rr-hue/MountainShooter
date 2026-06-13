import pygame
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 480))

    def run(self):
        menu = Menu(self.window)
        menu.run()