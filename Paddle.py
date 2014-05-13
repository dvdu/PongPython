__author__ = 'dvdu'
import pygame


class Paddle:
    def __init__(self, width, height, screen_width, screen_height, left_paddle = True):
        if left_paddle:
            self.x = 0.0+1
            self.y = screen_height/2 - height/2
        else:
            self.x = screen_width-width-1
            self.y = screen_height/2 - height/2

        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))