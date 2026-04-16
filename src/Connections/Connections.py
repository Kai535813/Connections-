# Main File for Connections
import pygame
import random
from Button import Button
from Term import Term
def display(screen, font, clock):
    # Create buttons
    button1 = Button(100, 100, 200, 50, "Button 1", font)
    button2 = Button(100, 200, 200, 50, "Button 2", font)
    button3 = Button(100, 300, 200, 50, "Button 3", font)
    button4 = Button(400, 100, 200, 50, "Button 4", font)
    button5 = Button(400, 200, 200, 50, "Button 5", font)
    button6 = Button(400, 300, 200, 50, "Button 6", font)
    button7 = Button(700, 100, 200, 50, "Button 7", font)
    button8 = Button(700, 200, 200, 50, "Button 8", font)
    button9 = Button(700, 300, 200, 50, "Button 9", font)
    button10 = Button(1000, 100, 200, 50, "Button 10", font)
    button11 = Button(1000, 200, 200, 50, "Button 11", font)
    button12 = Button(1000, 300, 200, 50, "Button 12", font)
    button13 = Button(1300, 100, 200, 50, "Button 13", font)
    button14 = Button(1300, 200, 200, 50, "Button 14", font)
    button15 = Button(1300, 300, 200, 50, "Button 15", font)
    button16 = Button(1600, 100, 200, 50, "Button 16", font)
    Shuffle = Button(1600, 200, 200, 50, "Shuffle", font)
    restart = Button(1600, 300, 200, 50, "Restart", font)

   

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Clear screen with white background

        # Draw buttons and terms
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        term1.draw(screen)
        term2.draw(screen)
        term3.draw(screen)

        pygame.display.flip()
        clock.tick(60)


