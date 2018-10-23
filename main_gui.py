import  pygame, sys
from    pygame.locals import *
from    colour import *

pygame.init()
DISPLAY_GUI = pygame.display.set_mode((400,400))
pygame.display.set_caption("2048")

DISPLAY_GUI.fill(Black)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()