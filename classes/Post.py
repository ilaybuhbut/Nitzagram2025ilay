import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self,username,location,description): #TODO: add parameters
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def add_like(self):
        self.likes_counter += 1
    
    def view_more_comments(self):
        #self.comments_display_index = min(self.comments_display_index + 1, len(self.comments))
        if self.comments_display_index >= len(self.comments) - 1:
            self.reset_comment_display_index()
        else:
            self.comments_display_index += 1

    def reset_comment_display_index(self):
        self.comments_display_index = 0

    def add_comment(self, text):
        self.comments.append(Comment(text))


    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        # TODO: write me!
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        # leave blank here. Override in ImagePost class and TextPost class
        pass

    def display_header(self):
    # Font settings for the header
        header_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)

        # Render username
        username_text = header_font.render(self.username, True, BLACK)
        screen.blit(username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))

        # Render location
        location_text = header_font.render(self.location, True, GREY)
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        # Render description
        description_text = header_font.render(self.description, True, BLACK)
        screen.blit(description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))


    def display_likes(self):
        # Display number of likes "Liked by X users"
        likes_font = pygame.font.SysFont('chalkduster.ttf')

        likes_font = likes_font.render( self.likes, True, RED)
        screen.blit(likes_font, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None

        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



