
import pygame
from player import Player
from projectile import Projectile
from enemy import Enemy
import time
# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
big_font = pygame.font.SysFont('Arial', 40)
pygame.display.set_caption("Tank Survival")
# set up variables for the display
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

message = "Survive"
r = 50
g = 0
b = 100
# render the text for later
message_display = big_font.render(message, True, (255, 255, 255))

f = Player(350, 60)
score = 0
# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
start_game = False

blit_proj_list = []
projectiles = []
shoot = True

shoot_time = 3
e_prj_dir = []
blit_e_proj_list = []
e_projectiles = []
right = False

directions = []
health = 100
shots = 0
bg = pygame.image.load("backgound.PNG")

e1 = Enemy(800, 100)
e2 = Enemy(800, 300)
e3 = Enemy(800, 700)
e4 = Enemy(100, 100)
e5 = Enemy(100, 400)
e6 = Enemy(100, 700)

enemy_list = []
enemy_list.extend((e1, e2, e3, e4, e5, e6))
alive_list = []
alive_list.extend((True, True, True, True, True, True))
move_time = 1
bg = pygame.image.load('backgound.PNG')  # Load the background image
backg = pygame.transform.scale(bg, (1500, 800))
end_screen = False
game_win = False
game_loss = False
end_num = 0


# -------- Main Program Loop -----------
while run:
    screen.blit(backg, (0, 0))
    for proj in projectiles:
        for e in enemy_list:
            if proj.rect.colliderect(e.rect) and alive_list[enemy_list.index(e)]:
                alive_list[enemy_list.index(e)] = False
                blit_proj_list[projectiles.index(proj)] = False

    for proj in e_projectiles:
        if proj.rect.colliderect(f.rect):
            blit_e_proj_list[e_projectiles.index(proj)] = False
            end_screen = True
            game_loss = True
            start_game = False
            break


    if True not in alive_list:
        end_screen = True
        game_win = True
        start_game = False
        message = "You Won"

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

        if start_game:
            if event.type == pygame.MOUSEBUTTONUP:
                if f.current_direction == "left":
                    proj = Projectile(f.x-10, f.y+27)
                    projectiles.append(proj)
                    blit_proj_list.append(True)

                if f.current_direction == "right":
                    proj = Projectile(f.x+170, f.y+30)
                    projectiles.append(proj)
                    blit_proj_list.append(True)

                if f.current_direction == 'right':
                    right = True
                    directions.append(right)
                elif f.current_direction == 'left':
                    right = False
                    directions.append(right)

        if event.type == pygame.MOUSEBUTTONUP and start_game == False and end_screen == False:
            start_game = True
            message = "Click to play!"
            message_display = my_font.render(message, True, (255, 255, 255))
            start_time = time.time()

    if end_screen and game_win:

        message = "You WON!"
        message_display = big_font.render(message, True, (255, 255, 255))
        screen.blit(message_display, (600, 400))

        time_final = elapsed_time
        display_elapsed_time = my_font.render("Time elapsed " + str(time_final)+ "s", True, (255, 255, 255))
        screen.blit(display_elapsed_time, (350, 340))



    elif end_screen and game_loss:
        message = "You LOSE!"
        message_display = big_font.render(message, True, (255, 255, 255))
        screen.blit(message_display, (600, 400))
        elapsed_time = time.time() - start_time
        time_display = my_font.render(f"Time: {(elapsed_time//0.1)/10}s", True, (255, 255, 255))


    elif start_game:

        elapsed_time = time.time() - start_time
        dis_elapsed_time = time.time() - start_time

        time_display = my_font.render(f"Time: {(elapsed_time//0.1)/10}s", True, (255, 255, 255))

        elapsed_time = int(elapsed_time)

        if elapsed_time == move_time:
            move_time += 1
            for e in enemy_list:
                if f.x < e.x:
                    e.move_left()
                if f.x > e.x:
                    e.move_right()

        if elapsed_time == shoot_time:
            shoot_time+=3
            for e in enemy_list:
                if alive_list[enemy_list.index(e)]:
                    blit_e_proj_list.append(True)
                    en = enemy_list[enemy_list.index(e)]
                    if en.x < f.x:
                        p = Projectile(en.x+185, en.y+5)
                        e_projectiles.append(p)
                        e_prj_dir.append(True)
                    else:
                        p = Projectile(en.x-8, en.y+6)
                        e_projectiles.append(p)
                        e_prj_dir.append(False)

        screen.blit(time_display, (0, 0))


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

        for p in e_projectiles:
            if blit_e_proj_list[e_projectiles.index(p)]:
                screen.blit(p.image, p.rect)
                if e_prj_dir[e_projectiles.index(p)]:
                    p.move_right()
                else:
                    p.move_left()


        pygame.display.update()

    if not start_game or end_screen:
        screen.blit(backg, (0, 0))
        screen.blit(message_display, (670, 350))
        pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
