# Main File for Connections
# 0 == place holder for colors.
import pygame

from Button import Button


    
pygame.init()

screen = pygame.display.set_mode((490, 590))
pygame.display.set_caption("Connections")
font = pygame.font.SysFont("Arial", 16, bold=True)
BTN_W, BTN_H = 105, 70
COLS, ROWS = 4, 4
X_START, Y_START = 15, 120
GAP = 10
Grey = ((200, 200, 200), (170, 170, 170))

Grey = ((200, 200, 200), (170, 170, 170))

words = [
    "N/A", "N/A",  "N/A",  "N/A",
    "N/A",   "N/A",   "N/A", "N/A",
    "N/A",   "N/A",   "N/A",   "N/A",
    "N/A", "N/A",  "N/A",    "N/A",
]

BTN_SIZE = 110

buttons = []
for i, (cx, cy) in enumerate(Button.positions[1:]):   # cx, cy = center x, center y
    btn = Button(words[i], cx - BTN_SIZE//2, cy - BTN_SIZE//2, BTN_SIZE, BTN_SIZE, *Grey)
    buttons.append(btn)
buttons = []
for row in range(ROWS):
    for col in range(COLS):
        x = X_START + col * (BTN_W + GAP)
        y = Y_START + row * (BTN_H + GAP)
        btn = Button(words[row * COLS + col], x, y, BTN_W, BTN_H, *Grey)
        buttons.append(btn)

functionButtons = [
    Button("SUBMIT", 170, 520, 150, 50, *Grey),   
    Button("SHUFFLE", 10,  520, 100, 50, *Grey),  
    # add as many as you need...
]
running = True
while running:
    screen.fill((249, 249, 249))

    mouse_pos = pygame.mouse.get_pos()   # pass current mouse position each frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for btn in buttons:
        btn.display(screen, btn.term, font, mouse_pos)

    for btn in functionButtons:
        btn.display(screen, btn.term, font, mouse_pos)

    pygame.display.flip()

pygame.quit()