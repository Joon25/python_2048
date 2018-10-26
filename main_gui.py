import pygame, sys, random
from pygame.locals import *
from colour_table import *

RECT_WIDTH = 50
RECT_HEIGHT = 50
TILE_SIZE = 50
X_TILE = 4
Y_TILE = 4
BASICFONTSIZE = 20
#BORDER_COLOR = pygame.Color('BLUE')
#NUM_COLOR = pygame.Color('RED')
#DISABLE_COLOR = pygame.Color('aliceblue')

def main():
    pygame.init()
    MainFrame = pygame.display.set_mode((RECT_WIDTH*10,RECT_HEIGHT*10))
    pygame.display.set_caption('Slide Game')
    MainFrame.fill(pygame.Color('white'))
    BasicFont = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)


    for yTile in range(Y_TILE):
        for xTile in range(X_TILE):
            #if ((yTile+1) * Y_TILE + xTile + 1) % 5 == 0:
                disableTile(MainFrame, RECT_WIDTH * (xTile+1), RECT_HEIGHT*(yTile+1))
            #else:
            #   drawTile(MainFrame, BasicFont, pygame.Color('Yellow'), RECT_WIDTH * (xTile+1), RECT_HEIGHT*(yTile+1),
            #       yTile * Y_TILE + xTile + 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print ('QUIT button pressed')
                pygame.quit()
                sys.exit()

        pygame.display.update()


def displayText(FontObj, text, color, top, left):
    textSurf = FontObj.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (top + int(TILE_SIZE/2), left + int(TILE_SIZE/2))
    return (textSurf, textRect)

def drawTile(MainObj, TextObj,  color, tilex, tiley, number):
    pygame.draw.rect(MainObj, color, (tilex, tiley, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(MainObj, BORDER_COLOR, (tilex, tiley, TILE_SIZE, TILE_SIZE), 2)
    textSurf, textRect = displayText(TextObj, str(number), pygame.Color('Red'), tilex, tiley)
    MainObj.blit(textSurf, textRect)

def disableTile(MainObj, tilex, tiley):
    pygame.draw.rect(MainObj, DISABLE_COLOR, (tilex, tiley, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(MainObj, BORDER_COLOR, (tilex, tiley, TILE_SIZE, TILE_SIZE), 2)

if __name__ == '__main__':
    main()
