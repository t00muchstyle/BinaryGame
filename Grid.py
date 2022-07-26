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
        draw_inp_box()
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


def draw_inp_box():

    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    input_box = pygame.Rect(400, 350,
                               200, 50)
    pygame.draw.rect(SCREEN, WHITE, input_box, 1)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ""
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]

                    else:
                        text += event.unicode

        SCREEN.fill((30, 30, 30))
        ##draw_inp_box()
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        SCREEN.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(SCREEN, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


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