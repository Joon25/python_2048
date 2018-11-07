import pygame, sys, random
from pygame.locals import *

BORDER_COLOR = pygame.Color('BLUE')
NUM_COLOR = pygame.Color('RED')
DISABLE_COLOR = pygame.Color('aliceblue')
L1st_Color = pygame.Color('moccasin')        # 2
L2nd_Color = pygame.Color('navajowhite1')    # 4
L3rd_Color = pygame.Color('navajowhite2')    # 8
L4th_Color = pygame.Color('orange1')         # 16
L5th_Color = pygame.Color('olivedrab1')      # 32
L6th_Color = pygame.Color('lightpink1')      # 64
L7th_Color = pygame.Color('olivedrab1')      # 128
L8th_Color = pygame.Color('orchid1')         # 256
L9th_Color = pygame.Color('orange2')         # 512
L10th_Color = pygame.Color('olivedrab2')      # 1024
L11th_Color = pygame.Color('lightpink2')      # 2048
L12th_Color = pygame.Color('olivedrab2')      # 4096
L13th_Color = pygame.Color('orchid2')         # 8192
L14th_Color = pygame.Color('orange3')         # 16384
L15th_Color = pygame.Color('olivedrab3')      # 32768
L16th_Color = pygame.Color('lightpink3')      # 65536
L17th_Color = pygame.Color('olivedrab3')      # 131072
L18th_Color = pygame.Color('orchid3')         # 262144

ColorDict = {
    0 : 'aliceblue',
    2 : 'moccasin',
    4 : 'navajowhite1',
    8 : 'navajowhite2',
    16 : 'orange1',
    32 : 'olivedrab1',
    64 : 'lightpink1',
    128 : 'olivedrab1',
    256 : 'orchid1',
    512 : 'orange2',
    1024 : 'olivedrab2',
    2048 : 'lightpink2',
    4096 : 'olivedrab2',
    8192 : 'orchid2',
    16384 : 'orange3',
    32768 : 'olivedrab3',
    65536 : 'lightpink3'
}
