import pygame
import os

# read from a text file and create the board list
with open (os.path.abspath("Sudoku/matrix.txt")) as file:
    matrix = file.read()
board = []
for i in range(9):
    board.append([])
    
index = 0   
for string in matrix:
    for number in string:
        if number not in (",", "\n", "[", "]"):
            board[index].append(int(number))
        if number == "\n":
            index+=1
"""
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
"""

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

WHITE = (225,225,225)
BLUE = (0,0,225)
BLACK = (0,0,0)
RED = (225,0,0)
FPS = 60
buffer = 5

def if_win(board):
    block = []
    column = []
    for row in board:
        for element in range(1,10):
            if row.count(element) != 1:                    
                return False

    for c in range (9):
        for r in range (9):
            column.append(board[r][c])
        for element in range(1,10):
            if column.count(element) != 1:                    
                return False
        column = []

    for times in range(3):
        for r in range (3):
            for c in range (3):
                block.append(board[0+3*r][c+3*times])
                block.append(board[1+3*r][c+3*times])
                block.append(board[2+3*r][c+3*times])
            for element in range(1,10):
                if block.count(element) != 1:                    
                    return False
            block = []
    return True

def draw_window():
    WIN.fill(WHITE)
    for i in range(1, 10):
        if i % 3 == 0:
            width = 3       
        else:
            width = 1
        pygame.draw.lines(WIN, BLACK, True, ((0,(500/9)*i),(500,(500/9)*i)), width) # Horizontal Line
        pygame.draw.lines(WIN, BLACK, True, (((500/9)*i,0),((500/9)*i,500)), width) # Vertical Line

    myFont = pygame.font.SysFont("Comic Sans MS", 35)
    
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if (0 < board[i][j] < 10): 
                number = myFont.render(str(board[i][j]), True, BLUE)
                WIN.blit(number,(17+j*(500/9),7+(500/9)*i))

    pygame.display.update()

def insert(window, position):
    i, j = position[1], position[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == 48: # event.key is a ascii number, 0 is 48
                    board[i][j] = event.key - 48
                    pygame.draw.rect(window, WHITE, (j * 100 , i * 100, 200, 200))
                    pygame.display.update()
                if (0 < event.key - 48 < 10):
                    pygame.draw.rect(window, WHITE, (j * 100 , i * 100, 200, 200))
                    board[i][j] = event.key - 48
                    pygame.display.update()
                    return
            return
        
def display_win(window):
    myFont = pygame.font.SysFont("arial", 80)
    words = myFont.render("You Win!", True, RED)
    window.blit(words, (75, 200))
    pygame.display.update()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    i = 0
    while run:
        run = not if_win(board)
        clock.tick(FPS)
        for event in pygame.event.get():
            i+=1
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                insert(WIN, (int(pos[0]//(500/9)), int(pos[1]//(500/9))))
        draw_window()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display_win(WIN)

    #pygame.quit()

if __name__ == "__main__":
    main()
    
