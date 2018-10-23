import pygame, sys, random
from pygame.locals import *
from colour_table import *

RECT_WIDTH = 50
RECT_HEIGHT = 50
TILE_SIZE = 50
X_GRID = 4
Y_GRID = 4
BASICFONTSIZE = 20

def main():
    pygame.init()
    MainFrame = pygame.display.set_mode((RECT_WIDTH*10,RECT_HEIGHT*10))
    pygame.display.set_caption('Slide Game')
    MainFrame.fill(WHITE)
    BasicFont = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    drawTile(MainFrame, BasicFont, pygame.Color('Yellow'), 50, 50, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print ('QUIT button pressed')
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawBox(Obj, boxX, boxY, border):
    pygame.draw.rect(Obj, BLUE, (boxX, boxY, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(Obj, BLACK, (boxX, boxY, RECT_WIDTH, RECT_HEIGHT), border)

def makeText(FontObj, text, color, bgcolor, top, left):
    textSurf = FontObj.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

def drawTile(MainObj, TextObj,  color, tilex, tiley, number):
    pygame.draw.rect(MainObj, color, (tilex, tiley, TILE_SIZE, TILE_SIZE))
    textSurf = TextObj.render(str(number), True, pygame.Color('Red'))
    textRect = textSurf.get_rect()
    textRect.center = (tilex + int(TILE_SIZE/2), tiley + int(TILE_SIZE/2))

    MainObj.blit(textSurf, textRect)

if __name__ == '__main__':
    main()
