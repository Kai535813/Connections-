import pygame
class Button:
    def __init__(self, term, x, y, w, h, C1, C2, selected_color=(0,0,0)):
        self.term = term
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.C1 = C1
        self.C2 = C2
        self.selected_color = selected_color 
        self.over = False
        self.selected = False
        self.group = None
    def display(self, screen, text, font, mouse_pos, radius=15):
        self.over = self.x < mouse_pos[0] < self.x + self.w and \
        self.y < mouse_pos[1] < self.y + self.h

        if self.selected:
            color = self.selected_color
        elif self.over:
            color = self.C2
        else:
            color = self.C1

        pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.h), border_radius=radius)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        screen.blit(text_surface, text_rect)

    def overed(self):
        return self.over
       
    positions = [(245,55), (65,165), (185, 165), (305, 165), (425, 165),(65, 285), (185, 285), (305, 285), (425, 285),(65, 405), (185, 405), (305, 405), (425, 405),(65, 525), (185, 525), (305, 525), (425, 525)]