import pygame
from constants import *
from helpers import screen
from Post import Post

class ImagePost(Post):

    def __init__(self,username,location,description):
        super().__init__(username,location,description)
        self.image = pygame.image.load(IMAGE_PATH)
        self.image = pygame.image.sacle(self.image,POST_WIDTH,POST_HEIGHT)

    def display_content(self):
        screen.blit(self.image, (POST_X_POS,POST_Y_POS))
        pygame.display.update()