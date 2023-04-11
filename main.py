# imports
import pygame

# initializing pygame
pygame.init()

# variables
W, H = 800, 600
run = True

# window setup
display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("colored_text")
clock = pygame.time.Clock()

# main loop
while run:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # screen update
    clock.tick()
    display.blit(screen, (0, 0))
    pygame.display.update()
