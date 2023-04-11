import pygame

W, H = 800, 600

display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("colored_text")
clock = pygame.time.Clock()

pygame.init()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick()

    display.blit(screen, (0, 0))
    pygame.display.update()
