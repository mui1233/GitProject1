import pygame
from fox import Fox
import random
# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Coin Collector!")

# set up variables for the display
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

message = "Collision not detected"
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
# -------- Main Program Loop -----------
while run:


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

    if start_game:
        score_display = my_font.render(f"Points: {score}", True, (255, 255, 255))
        screen.fill((r, g, b))
        screen.blit(score_display, (0, 30))

        screen.blit(display_message, (0, 15))
        screen.blit(f.image, f.rect)
        pygame.display.update()
    else:
        screen.fill((r, g, b))
        screen.blit(display_message, (200, 200))
        pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()



