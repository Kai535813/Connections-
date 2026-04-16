import pygame
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
    def display(self, screen, text, font, mouseClicked):
        if self.x < mouseClicked[0] < self.x + self.w and self.y < mouseClicked[1] < self.y + self.h:
            self.over = True
        else:
            self.over = False
        if self.over:
            pygame.draw.rect(screen, self.C2, (self.x, self.y, self.w, self.h))
        else:
            pygame.draw.rect(screen, self.C1, (self.x, self.y, self.w, self.h))
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x + self.w / 2, self.y + self.h / 2))
        screen.blit(text_surface, text_rect)
    def overed(self):
        return self.over
       