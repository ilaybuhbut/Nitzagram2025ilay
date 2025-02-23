import pygame

from helpers import *
from constants import *
from helpers import * 

class Comment:
    def __init__(self,text):
        self.text = text
    def display_comment(self, comment_number):
        comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        comment_text = comment_font.render(self.text, True, BLACK)
        screen.blit(comment_text, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + comment_number * COMMENT_LINE_HEIGHT))
