# 0 == as color placeholder.
from tkinter import font

import pygame
import os
class Button:
    def __init__(self, term, x, y, w, h, C1, C2):
        self.term = term
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.C1 = C1
        self.C2 = C2
        self.over = False
    def display(self, screen, text, font, mouseClicked, radius=15):
        if self.x < mouseClicked[0] < self.x + self.w and self.y < mouseClicked[1] < self.y + self.h:
            self.over = True
        else:
            self.over = False
        if self.over:
            pygame.draw.rect(screen, self.C2, (self.x, self.y, self.w, self.h), border_radius=radius)
        else:
            pygame.draw.rect(screen, self.C1, (self.x, self.y, self.w, self.h), border_radius=radius)
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(self.x + self.w / 2, self.y + self.h / 2))
            screen.blit(text_surface, text_rect)
    def overed(self):
        return self.over
       
    positions = [(245,55), 
                 (65,165), (185, 165), (305, 165), (425, 165),
                 (65, 285), (185, 285), (305, 285), (425, 285),
                 (65, 405), (185, 405), (305, 405), (425, 405),
                 (65, 525), (185, 525), (305, 525), (425, 525)
                 ]