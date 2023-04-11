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
white = (255, 255, 255)
col_spd = 1

col_dir_flash = [1, 1, 1]
def_col_flash = [100, 100, 100]

col_dir_breathe = [1, 1, 1]
def_col_breathe = [100, 100, 100]

minimum = 0
maximum = 255


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
    text_surface = font_object.render(text, False, col)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def col_change_flash(color: list, direction: list) -> None:
    """
    This function changes an RGB list in a way that we achieve a cool flashing effect.
    This looks good on black background. For transparency we should use the alpha value.
    :param color: List of RGB values.
    :param direction: List of color change direction values (-1, 0, or 1).
    :return: None
    """
    for i in range(3):
        color[i] += col_spd * direction[i]
        if color[i] >= maximum:
            color[i] = minimum
        elif color[i] <= minimum:
            color[i] = maximum


def col_change_breathe(color: list, direction: list) -> None:
    """
    This function changes an RGB list in a way that we achieve nice breathing effect.
    :param color: List of RGB values.
    :param direction: List of color change direction values (-1, 0, or 1).
    :return: None
    """
    for i in range(3):
        color[i] += col_spd * direction[i]
        if color[i] >= maximum or color[i] <= minimum:
            direction[i] *= -1
        if color[i] >= maximum:
            color[i] = maximum
        elif color[i] <= minimum:
            color[i] = minimum


# main loop
while run:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # color update
    col_change_flash(def_col_flash, col_dir_flash)
    col_change_breathe(def_col_breathe, col_dir_breathe)

    # text displaying
    draw_text("this text is flashing", 40, def_col_flash, W / 2, 200)
    draw_text("this text is breathing", 40, def_col_breathe, W / 2, 400)

    # screen update
    clock.tick()
    display.blit(screen, (0, 0))
    pygame.display.update()
