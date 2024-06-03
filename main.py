import pygame
from fox import Fox
from projectile import Projectile
from enemy import Enemy
import random
# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Defend the Flag")

# set up variables for the display
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

message = "Defend the Flag"
r = 50
g = 0
b = 100
# render the text for later
display_message = my_font.render(message, True, (255, 255, 255))

f = Fox(40, 60)
score = 0
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
start_game = False
blit_proj_list = []
projectiles = []
right = False
directions = []
health = 100
enemy_list = []
alive_list = []
# -------- Main Program Loop -----------
while run:


    e1 = Enemy(400, 200)
    e2 = Enemy(400, 300)
    e3 = Enemy(400, 400)
    enemy_list.extend((e1, e2, e3))
    alive_list.extend((True, True, True))

    for proj in projectiles:
        for e in enemy_list:
            if proj.rect.colliderect(e.rect) and alive_list[enemy_list.index(e)]:
                alive_list[enemy_list.index(e)] = False
                blit_proj_list[projectiles.index(proj)] = False


    if start_game:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            f.move_direction("right")
        if keys[pygame.K_a]:
            f.move_direction("left")

        if keys[pygame.K_w]:
            f.move_direction("up")

        if keys[pygame.K_s]:
            f.move_direction("down")

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONUP and start_game == False:
            start_game = True
            message = "Click to play!"
            message_display = my_font.render(message, True, (255, 255, 255))
        if start_game == True:
            if event.type == pygame.MOUSEBUTTONUP:
                proj = Projectile(f.x, f.y)
                projectiles.append(proj)
                blit_proj_list.append(True)
                if f.current_direction == 'right':
                    right = True
                    directions.append(right)
                elif f.current_direction == 'left':
                    right = False
                    directions.append(right)


    if start_game:
        score_display = my_font.render(f"Points: {score}", True, (255, 255, 255))
        screen.fill((r, g, b))
        screen.blit(score_display, (0, 30))

        screen.blit(display_message, (0, 15))
        screen.blit(f.image, f.rect)

        for a in alive_list:
            if a:
                screen.blit(enemy_list[alive_list.index(a)].eimage, enemy_list[alive_list.index(a)].rect)

        for p in projectiles:
            if blit_proj_list[projectiles.index(p)]:
                screen.blit(p.image, p.rect)
            if directions[projectiles.index(p)]:
                p.move_right()
            else:
                p.move_left()

        pygame.display.update()
    else:
        screen.fill((r, g, b))
        screen.blit(display_message, (200, 200))
        pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
