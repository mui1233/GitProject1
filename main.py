
import pygame
from fox import Fox
from projectile import Projectile
from enemy import Enemy
import time
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

f = Fox(200, 60)
score = 0
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
start_game = False
blit_proj_list = []
projectiles = []
right = False
directions = []
health = 100
shoot = True
e1 = Enemy(800, 200)
e2 = Enemy(800, 300)
e3 = Enemy(800, 400)
e4 = Enemy(100, 200)
e5 = Enemy(100, 300)
e6 = Enemy(100, 400)
enemy_list = []
enemy_list.extend((e1, e2, e3, e4, e5, e6))
alive_list = []
alive_list.extend((True, True, True, True, True, True))
move_time = 1
shift_left = False
shift_right = False
# -------- Main Program Loop -----------
while run:

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
            start_time = time.time()

        if start_game:
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
        screen.fill((r, g, b))

        elapsed_time = time.time() - start_time
        elapsed_time //= 1
        elapsed_time = int(elapsed_time)
        time_display = my_font.render(f"Time: {elapsed_time}s", True, (255, 255, 255))

        if elapsed_time == move_time:
            move_time += 1
            for e in enemy_list:
                if f.x < e.x:
                    e.move_left()
                if f.x > e.x:
                    e.move_right()
        screen.blit(time_display, (0, 0))

        score_display = my_font.render(f"Points: {score}s", True, (255, 255, 255))


        screen.blit(score_display, (0, 30))

        screen.blit(display_message, (0, 15))
        screen.blit(f.image, f.rect)


        for i in range(len(alive_list)):
            if alive_list[i]:
                if f.x > enemy_list[i].rect.x:
                    enemy_list[i].update_image(True)  # Face right

                    screen.blit(enemy_list[i].image, enemy_list[i].rect)

                else:
                    enemy_list[i].update_image(False)

                    screen.blit(enemy_list[i].image, enemy_list[i].rect)

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
