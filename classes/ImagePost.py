import pygame

from constants import *
from helpers import screen

class ImagePost(Post):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(IMAGE_PATH)
        