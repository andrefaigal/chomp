import pygame
import sys

#initialize Pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

#Colors
blue = (0, 158, 219)
brown = (188, 143, 143)

#create the screen
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Blue Background with Brown Rectangle")

#Maine Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with blue
    screen.fill(blue)

    #Draw the brown rectangle at the bottom
    rectangle_height = 200
    pygame.draw.rect(screen,brown, (0, screen_height - rectangle_height, screen_width, rectangle_height))

    #update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

# print("hello world!")
# print("what is good world?")
# print('hi')