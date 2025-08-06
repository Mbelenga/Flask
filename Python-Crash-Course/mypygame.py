import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('DO EATER!!')

x, y = 200, 150
velocity = 5
dot_x, dot_y = random.randint(0, 400), random.randint(0, 300)