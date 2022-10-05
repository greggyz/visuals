from pyclbr import Class
from re import S
import sys
from turtle import color
import pygame
from pygame.locals import *
from pygame import gfxdraw
from pygame.font import Font
import time
import random
import math


WIDTH = 1024    
HEIGHT = 768
FPS = 120

pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((WIDTH, HEIGHT))

pressedKeys = set()

palette = ((255, 255, 150),
            (255, 255, 120),
            (255, 255, 100),
            (255, 255, 80),
            (255, 255, 60),
            (255, 200, 50),
            (255, 173, 41),
            (247, 117, 33),
            (191, 74, 46),
            (115, 61, 56),
            (61, 38, 48))


class Ball:
    def __init__(self, color, x, y, radius) -> None:
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
    
    def update(self):
        self.x = mx
        self.y = my
        self.color = 1231231231
       
    def draw(self):
        pygame.draw.circle(surface, self.color, [self.x, self.y], self.radius)
    
    def isAlive(self):
        return True

class Phantom(Ball):
    def update(self):
        self.radius -= .3
        self.x = self.x + random.randint(-2, 2)
        self.y = self.y - random.randint(1, 3)
        
        if self.radius < 3:
            self.color = palette[-1]
        elif self.radius < 5:
            self.color = palette[-2]
        elif self.radius < 7:
            self.color = palette[-3]
        elif self.radius < 9:
            self.color = palette[-4]
        elif self.radius < 11:
            self.color = palette[-5]
        elif self.radius < 13:
            self.color = palette[-6]
        elif self.radius < 15:
            self.color = palette[-7]
        elif self.radius < 17:
            self.color = palette[-8]
        elif self.radius < 19:
            self.color = palette[-9]
        
    
    def isAlive(self):
        return self.radius > 0


phantoms = []
initx = WIDTH // 2
inity = HEIGHT // 2
color = 1 # palette[0]
radius = 20
surface.fill((0, 0, 0))
ball = Ball(color, initx, inity, radius)


while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            pressedKeys.add(event.key)
        elif event.type == KEYUP:
            pressedKeys.discard(event.key)
        elif event.type == MOUSEBUTTONDOWN:
            phantoms.append(Phantom(palette[0], mx, my, radius))
    mx, my = pygame.mouse.get_pos()
    print(phantoms)

    ball.update()
    for phantom in phantoms:
        phantom.update()
    phantoms.append(Phantom(palette[0], mx, my, radius))

    newPhantoms = []
    for phantom in phantoms:
        if phantom.isAlive():
            newPhantoms.append(phantom)
    phantoms = newPhantoms

    surface.fill((0, 0, 0))
    ball.draw()
    for phantom in phantoms:
        phantom.draw()
          
    
    pygame.display.update()
    clock.tick(FPS)