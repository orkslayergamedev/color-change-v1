# imports
import pygame

# initializing pygame
pygame.init()

# basic variables
W, H = 800, 600
run = True

# window setup
display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("colored_text")
clock = pygame.time.Clock()

# color variables
black = (0, 0, 0)
white = (0, 0, 0)
col_spd = 1
col_dir = [1, 1, 1]
def_col = [100, 100, 100]
minimum = 100
maximum = 200


def draw_text(text: str, size: int, col: list, x: int, y: int) -> None:
    """
    A simple function for displaying text strings on the game screen.
    :param text: The string to display.
    :param size: Size of the text.
    :param col: Color of the text.
    :param x: X coordinate of the text.
    :param y: Y coordinate of the text.
    :return: None
    """
    font_type = pygame.font.get_default_font()
    font_object = pygame.font.Font(font_type, size)
    text_surface = font_object.render(text, True, col)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


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
