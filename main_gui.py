import pygame, sys, random
from pygame.locals import *
from colour import *
from random import randint
from random import choices

RECT_WIDTH = 50
RECT_HEIGHT = 50
TILE_SIZE = 50
X_TILE = 4
Y_TILE = 4
BASICFONTSIZE = 20

tile_array = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

def main():
    pygame.init()
    MainFrame = pygame.display.set_mode((RECT_WIDTH*10,RECT_HEIGHT*10))
    pygame.display.set_caption('Slide Game')
    MainFrame.fill(pygame.Color('white'))
    BasicFont = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)


    for yTile in range(Y_TILE):
        for xTile in range(X_TILE):
            disableTile(MainFrame, xTile, yTile)

    for i in range(2):
        x_pos, y_pos,  number = generateNewTile(MainFrame, tile_array, X_TILE, Y_TILE)
        drawTile(MainFrame, BasicFont, pygame.Color(ColorDict[number]), x_pos, y_pos, number)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print ('QUIT button pressed')
                pygame.quit()
                sys.exit()

            key_valid = False;
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    key_valid = True;
                if event.key == K_UP:
                    key_valid = True;
                if event.key == K_RIGHT:
                    key_valid = True;
                if event.key == K_LEFT:
                    key_valid = True;

                if key_valid == True:
                    moveTiles(MainFrame, BasicFont, event.key, tile_array)


        pygame.display.update()


def displayText(FontObj, text, color, top, left):
    textSurf = FontObj.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (top + int(TILE_SIZE/2), left + int(TILE_SIZE/2))
    return (textSurf, textRect)

'''
MainObj : Main Frame object
TextObj : Text Font object
color   : Tile color
tilex   : x position of the tile
tiley   : y position of the tile
number  : number to be assigned to the tile
'''
def drawTile(MainObj, TextObj,  color, index_x, index_y, number):
    tilex = (index_x+1) * RECT_WIDTH
    tiley = (index_y+1) * RECT_HEIGHT
    pygame.draw.rect(MainObj, color, (tilex, tiley, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(MainObj, BORDER_COLOR, (tilex, tiley, TILE_SIZE, TILE_SIZE), 2)
    textSurf, textRect = displayText(TextObj, str(number), pygame.Color('Red'), tilex, tiley)
    MainObj.blit(textSurf, textRect)

'''
MainObj : Main frame object
tilex   : x position of the tile
tiley   : y position of the tile
'''
def disableTile(MainObj, tilex, tiley):
    pygame.draw.rect(MainObj, DISABLE_COLOR, ((tilex+1)*RECT_WIDTH, (tiley+1)*RECT_HEIGHT, TILE_SIZE, TILE_SIZE))
    pygame.draw.rect(MainObj, BORDER_COLOR, ((tilex+1)*RECT_WIDTH, (tiley+1)*RECT_HEIGHT, TILE_SIZE, TILE_SIZE), 2)

def generateNewTile(MainObj, array, xSize, ySize):

    while True:
        new_index = randint(0, (xSize * ySize) - 1)
        x_pos = int(new_index/Y_TILE)
        y_pos = new_index%Y_TILE
        population = [2, 4]
        weights = [0.9, 0.1]

        if array[x_pos][y_pos] == 0:
            array[x_pos][y_pos] = choices(population, weights)[0]
            return (x_pos, y_pos, array[x_pos][y_pos])

        if array.count[0] == 0:
            return (-1, -1, -1)

def moveTiles(MainObj, FontObj, direction, array):

    drawAllTiles(MainObj, FontObj, array)

    if direction == K_DOWN:
        print ("Down key pressed")

    if direction == K_UP:
        print ("Up key pressed")
    if direction == K_RIGHT:
        print ("Right key pressed")
    if direction == K_LEFT:
        print ("Left key pressed")
    score = 0
    return score

def drawAllTiles(MainObj, FontObj, array):
    for yTile in range(Y_TILE):
        for xTile in range(X_TILE):
            number = xTile + yTile*Y_TILE
            print (number, yTile, xTile)
            if array[xTile][yTile] == 0:
                disableTile(MainObj, xTile, yTile)
            else:
                drawTile(MainObj, FontObj, pygame.Color(ColorDict[array[xTile][yTile]]), xTile, yTile, array[xTile][yTile])


if __name__ == '__main__':
    main()
