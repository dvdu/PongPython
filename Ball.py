__author__ = 'dvdu'
import pygame


class Ball:
    def __init__(self, ball_size):
        self.size = ball_size
        self.x = 0.0
        self.y = 0.0
        self.image = pygame.Surface((self.size, self.size))
        pygame.draw.circle(self.image,(255,255,255),(self.size/2,self.size/2),self.size/2)

    def reset_ball_pos(self, new_x, new_y):
        self.x = new_x-self.size/2
        self.y = new_y-self.size/2