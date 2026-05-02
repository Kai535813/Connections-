# Kai Yun Chao | 3B | 2026

import pygame

from Button import Button
from Term import Term 
import random
    
pygame.init()
clock = pygame.time.Clock()
# Sound
pygame.mixer.init()
pygame.mixer.music.load("waterNoise.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1) 

selectedButtons = []
solvedGroups = []
MAX_SELECT = 4  
feedback_msg = ""
feedback_timer = 0
screen_state = "start"
def draw_start(screen, font, mouse_pos):
    title = font.render("CONNECTIONS", True, (255, 255, 255))
    screen.blit(title, title.get_rect(center=(245, 200)))
    start_btn.display(screen, start_btn.term, font, mouse_pos)

def draw_main(screen, font, mouse_pos):
    for i, grp in enumerate(solvedGroups):
        c1, c2 = groupColors[grp["group"]]
        y = Y_START + i * (BTN_H + GAP)
        pygame.draw.rect(screen, c1, (X_START, y, BTN_W * 4 + GAP * 3, BTN_H), border_radius=10)
        label = ", ".join(grp["terms"])
        surf = font.render(label, True, (0, 0, 0))
        screen.blit(surf, surf.get_rect(center=(245, y + BTN_H // 2)))

    

    for btn in buttons:
        btn.display(screen, btn.term, font, mouse_pos)

    for btn in functionButtons:
        btn.display(screen, btn.term, font, mouse_pos)

    count_surf = font.render(f"Selected: {len(selectedButtons)}/4", True, (255, 255, 255))
    screen.blit(count_surf, (15, 10))

    if feedback_timer > 0:
        fb_surf = font.render(feedback_msg, True, (255, 255, 255))
        screen.blit(fb_surf, fb_surf.get_rect(center=(245, 30)))  


def draw_gameover(screen, font, mouse_pos):
    msg = font.render("Game Over!", True, (255, 255, 255))
    screen.blit(msg, msg.get_rect(center=(245, 295)))
    again_btn.display(screen, again_btn.term, font, mouse_pos)
    exit_btn.display(screen, exit_btn.term, font, mouse_pos)

screen = pygame.display.set_mode((490, 590))
background = pygame.image.load("Gradient 1.png").convert()
# image = pygame.image.load("nycEdit.png").convert_alpha() 
# background.blit(image, (0, 0))
pygame.display.set_caption("Connections Game - Kai Yun Chao | 3B | 2026")
font = pygame.font.SysFont("Arial", 24, bold=True)
BTN_W, BTN_H = 105, 70
COLS, ROWS = 4, 4
X_START, Y_START = 15, 120
GAP = 10


Color = ((83, 216, 240), (125, 212, 227))
groupColors = [
     ((220, 180, 255), (190, 140, 240)), 
    ((150, 230, 150), (100, 200, 100)), 
    ((255, 200, 100), (235, 170,  60)),  
    ((130, 200, 255), ( 80, 160, 230)),  
]



def build_terms():
    selected_sets = random.sample(range(16), 4)  
    tagged = []
    for i, set_idx in enumerate(selected_sets):
        set_dict_idx = set_idx // 4
        key = f"set{set_idx + 1}"
        set_dict = Term.termSets[set_dict_idx]
        for term in set_dict[key]:
            tagged.append((term, i))
    random.shuffle(tagged)
    return tagged



BTN_SIZE = 110

def build_buttons(terms):
    btn_list = []
    for row in range(ROWS):
        for col in range(COLS):
            idx = row * COLS + col
            text, group_idx = terms[idx]
            x = X_START + col * (BTN_W + GAP)
            y = Y_START + row * (BTN_H + GAP)
            btn = Button(text, x, y, BTN_W, BTN_H, *Color)
            btn.group = group_idx           
            btn_list.append(btn)
    return btn_list

def toggleSelect(btn):
    if btn.selected:
        btn.selected = False
        selectedButtons.remove(btn)
    elif len(selectedButtons) < MAX_SELECT:
        btn.selected = True
        selectedButtons.append(btn)

# Logic for checking match completion by the player.
def trySubmit():
    global feedback_msg, feedback_timer
    if len(selectedButtons) != MAX_SELECT:
        return
    groups = {btn.group for btn in selectedButtons}
    if len(groups) == 1:
        group_idx = selectedButtons[0].group
        solvedGroups.append({"group": group_idx, "terms": [btn.term for btn in selectedButtons]})
        for btn in selectedButtons:
            buttons.remove(btn)
        selectedButtons.clear()
        feedback_msg = f"Solved group {group_idx + 1}!"   
        feedback_timer = 180                             
        if len(solvedGroups) == 4:
            global screen_state
            screen_state = "gameover"
    else:
        for btn in selectedButtons:
            btn.selected = False
        selectedButtons.clear()
        feedback_msg = "Not a match — try again!"        
        feedback_timer = 180


def shuffleBoard():
    random.shuffle(buttons)
    for i, btn in enumerate(buttons):
        row, col = divmod(i, COLS)
        btn.x = X_START + col * (BTN_W + GAP)
        btn.y = Y_START + row * (BTN_H + GAP)


start_btn = Button("START", 170, 280, 150, 50, *Color)
again_btn = Button("PLAY AGAIN", 145, 350, 200, 60, *Color)
exit_btn = Button("EXIT", 170, 410, 150, 50, *Color)
functionButtons = [
    Button("SUBMIT", 125, 55, 200, 50, *Color),   
    Button("SHUFFLE", 15,  55, 105, 50, *Color),  
    Button("CLEAR", 360, 55, 105, 50, *Color)
    
]
buttons = []





# Actual game loop.
running = True
while running:
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    if feedback_timer > 0:          
        feedback_timer -= 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_state == "start":
                if start_btn.overed():
                    terms = build_terms()
                    buttons = build_buttons(terms)
                    screen_state = "main"          
            elif screen_state == "main":
                for btn in functionButtons:
                    if btn.overed():
                        if btn.term == "SUBMIT":
                            trySubmit()
                        elif btn.term == "SHUFFLE":
                            shuffleBoard()
                        elif btn.term == "CLEAR":
                            for b in selectedButtons:
                                b.selected = False
                            selectedButtons.clear()

                
                for btn in buttons:
                    if btn.overed():
                        toggleSelect(btn)
                        break

            elif screen_state == "gameover":

                if again_btn.overed():
                    selectedButtons.clear()
                    solvedGroups.clear()
                    feedback_msg = ""
                    feedback_timer = 0

                    terms = build_terms()
                    buttons = build_buttons(terms)

                    screen_state = "main"

                elif exit_btn.overed():
                    running = False
            


   
    if screen_state == "start":
        draw_start(screen, font, mouse_pos)
    elif screen_state == "main":
        draw_main(screen, font, mouse_pos)
    elif screen_state == "gameover":
        draw_gameover(screen, font, mouse_pos)
        

        
    clock.tick(60)
    pygame.display.flip()

pygame.quit()