# Main File for Connections
# 0 == place holder for colors.
import pygame

from Button import Button


    
pygame.init()

screen_state = "start"
def draw_start(screen, font, mouse_pos):
    title = font.render("CONNECTIONS", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(245, 200)))
    start_btn.display(screen, start_btn.term, font, mouse_pos)

def draw_main(screen, font, mouse_pos):
    for btn in buttons:
        btn.display(screen, btn.term, font, mouse_pos)
    for btn in functionButtons:
        btn.display(screen, btn.term, font, mouse_pos)

def draw_gameover(screen, font, mouse_pos):
    msg = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(msg, msg.get_rect(center=(245, 295)))

screen = pygame.display.set_mode((490, 590))
background = pygame.image.load("Gradient 1.png").convert()
pygame.display.set_caption("Connections Game")
font = pygame.font.SysFont("Arial", 24, bold=True)
BTN_W, BTN_H = 105, 70
COLS, ROWS = 4, 4
X_START, Y_START = 15, 120
GAP = 10


Grey = ((83, 216, 240), (125, 212, 227))

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

start_btn = Button("START", 170, 280, 150, 50, *Grey)
functionButtons = [
    Button("SUBMIT", 170, 55, 150, 50, *Grey),   
    Button("SHUFFLE", 15,  55, 105, 50, *Grey),  
    Button("CLEAR", 360, 55, 105, 50, *Grey)
    
]
running = True
while running:
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_state == "start":
                if start_btn.overed():
                    screen_state = "main"          # transition to game
            elif screen_state == "main":
                for btn in functionButtons:
                    if btn.overed() and btn.term == "SUBMIT":
                        pass  # your submit logic here

    # Draw based on current state
    if screen_state == "start":
        draw_start(screen, font, mouse_pos)
    elif screen_state == "main":
        draw_main(screen, font, mouse_pos)
    elif screen_state == "gameover":
        draw_gameover(screen, font, mouse_pos)

    pygame.display.flip()

pygame.quit()