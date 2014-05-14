__author__ = 'dvdu'
import pygame
from pygame.locals import *
from sys import exit
import time
import Ball
import Paddle

class Pong:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.paddle_speed = 1
        pygame.init()
        self.screen=pygame.display.set_mode((self.screen_width,self.screen_height))
        pygame.display.set_caption("PONG")
        self.ai_paddle = False
        self.game_on = False
        #Paddles and Ball
        back = pygame.Surface((screen_width,screen_height))
        self.background = back.convert()
        self.background.fill((0,0,0))
        self.paddle_left = Paddle.Paddle(10, 50, self.screen_width, self.screen_height, True)
        self.paddle_right = Paddle.Paddle(10, 50, self.screen_width, self.screen_height, False)
        self.paddle_left_move, self.paddle_right_move = 0.,0.
        self.buffered_time = time.time()
        #circ_sur = pygame.Surface((15,15))
        #circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
        ball = Ball.Ball(15)

    def run_game(self):
        while True:
            self.handle_keys()

            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.paddle_left.image,(self.paddle_left.x,self.paddle_left.y))
            self.screen.blit(self.paddle_right.image,(self.paddle_right.x,self.paddle_right.y))
            # self.screen.blit(self.ball.image,(self.ball.x,self.ball.y))

            self.paddle_right.y += self.paddle_right_move
            self.paddle_left.y += self.paddle_left_move

            delta_time = self.buffered_time - time.time()
            self.buffered_time = time.time()
            pygame.display.update()


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.game_on = not self.game_on
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_UP:
                    self.paddle_right_move = -self.paddle_speed
                elif event.key == K_DOWN:
                    self.paddle_right_move = self.paddle_speed
                if not self.ai_paddle:
                    if event.key == K_a:
                        self.paddle_left_move = -self.paddle_speed
                    elif event.key == K_z:
                        self.paddle_left_move = self.paddle_speed
            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    self.paddle_right_move = 0.
                if not self.ai_paddle and (event.key == K_a or event.key == K_z):
                    self.paddle_left_move = 0.



def main():
    pong = Pong(640, 480)
    pong.run_game()

if __name__ == '__main__':
    main()