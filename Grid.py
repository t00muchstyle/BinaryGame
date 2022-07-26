import sys
import random
import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 500
board =[[random.randrange(0, 2, 1) for i in range(8)]for j in range (10)]



def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        draw_numbers()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():


    blockSize = 50 #Set the size of the grid block
    for x in range(8):
        for y in range(8):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def draw_numbers():
    font = pygame.font.SysFont('bookantigua', 28, True, False)
    row = 0
    blockSize = 50
    offset = 20
    while row < 8:
        col = 0
        while col<8:
            output = board[row][col]

            b_text = font.render((str(output)), True, pygame.Color('white'))
            SCREEN.blit(b_text, pygame.Vector2((col*blockSize)+offset, (row*blockSize)+offset-3))
            col += 1
        row += 1


main()