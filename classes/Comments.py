import pygame

from helpers import *
from constants import *
from Post import display_comments
from helpers import * 

class Comment:
    def __init__(self,text):
        self.text = read_comment_from_user()
display_comments()
