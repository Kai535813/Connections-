# Main File for Connections
# 0 == place holder for colors.
import pygame

from Button import Button
from Term import Term
def display(screen):
    pass
    
screen = pygame.display.set_mode((490,590))


running = True
while running:   

    screen.fill((255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()