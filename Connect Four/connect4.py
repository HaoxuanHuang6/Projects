import numpy as np
import pygame

class ConnectFour():
    def __init__(self):
        self.ROW = 6
        self.COLUMN = 7

        self.BLUE = (0,0,255)
        self.BLACK = (0,0,0)
        self.RED = (255,0,0)
        self.YELLOW = (255,255,0)
        self.RED = (225,0,0)

        self.REC_EDGE = 100
        self.WIDTH = self.COLUMN * self.REC_EDGE
        self.HEIGHT = (self.ROW+1) * self.REC_EDGE
        self.RADIUS = self.REC_EDGE/2 - 5
        self.if_win = False
        self.turn = 0
        self.WINDOW = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("Connect Four")


    def create_board(self):
        size = (self.ROW,self.COLUMN)
        board = np.zeros(size)
        return board

    def check_win(self, board, color):
        # Horizontal Check
        for row in range(self.ROW):
            for column in range(self.COLUMN-3):
                if board[row][column] == color and board[row][column+1] == color and board[row][column+2] == color and board[row][column+3] == color:
                    self.if_win = True

        # Vertical Check
        for column in range(self.COLUMN):
            for row in range(self.ROW-4, -1, -1):
                if board[row][column] == color and board[row+1][column] == color and board[row+2][column] == color and board[row+3][column] == color:
                    self.if_win = True 
        
        # Bottom Left to Top Right Check
        for column in range(self.COLUMN-3):
            for row in range(self.ROW-4, -1, -1):
                if board[row][column+3] == color and board[row+1][column+2] == color and board[row+2][column+1] == color and board[row+3][column] == color:
                    self.if_win = True

        # Top Left to Bottom Right Check
        for column in range(self.COLUMN-3):
            for row in range(self.ROW-4, -1, -1):
                if board[row][column] == color and board[row+1][column+1] == color and board[row+2][column+2] == color and board[row+3][column+3] == color:
                    self.if_win = True

    def get_empty_row(self, board, column):
        for i in range(self.ROW-1, -1, -1):
            if board[i][column] == 0:
                return i

    def is_step_valid(self, board, column):
        if column < self.COLUMN or column >= 0:
            if board[0][column] == 0:
                return True
        return False

    def drop_piece(self, board, column, color):
        if self.is_step_valid(board, column):
            row = self.get_empty_row(board, column)
            board[row][column] = color
        else:
            self.turn -= 1
            #print("This self.COLUMN is Full. Please Choose a Different self.COLUMN!\n")

    def draw_board(self, board):
        pygame.draw.rect(self.WINDOW, self.BLUE, (0, self.REC_EDGE, self.COLUMN*self.REC_EDGE, self.ROW*self.REC_EDGE))
        #if not (self.check_win(board, self.RED) or self.check_win(board, self.YELLOW)):
        for row in range(self.ROW):
            for column in range(self.COLUMN):
                pygame.draw.circle(self.WINDOW, self.BLACK, (column*self.REC_EDGE+(self.REC_EDGE/2), self.REC_EDGE+row*self.REC_EDGE+(self.REC_EDGE/2)), self.RADIUS)
        
        for row in range(self.ROW):
            for column in range(self.COLUMN):
                if board[row][column] == 1:
                    pygame.draw.circle(self.WINDOW, self.RED, (column*self.REC_EDGE+(self.REC_EDGE/2), self.REC_EDGE+row*self.REC_EDGE+(self.REC_EDGE/2)), self.RADIUS)
                elif board[row][column] == 2:
                    pygame.draw.circle(self.WINDOW, self.YELLOW, (column*self.REC_EDGE+(self.REC_EDGE/2), self.REC_EDGE+row*self.REC_EDGE+(self.REC_EDGE/2)), self.RADIUS)
        
        pygame.display.update()


    def display_win(self):
        myFont = pygame.font.SysFont("arial", 80)
        word1 = myFont.render("Player1 Win!", True, self.RED)
        word2 = myFont.render("Player2 Win!", True, self.RED)
        if self.turn % 2 == 1:
            self.WINDOW.blit(word1, (self.WIDTH/4-self.REC_EDGE/2, 10))
        else:
            self.WINDOW.blit(word2, (self.WIDTH/4-self.REC_EDGE/2, 10))
        pygame.display.update()


def main():
    pygame.init()
    game = ConnectFour()
    board = game.create_board()
    
    while not game.if_win:
        game.draw_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            #if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(game.WINDOW, game.BLACK, (0, 0, game.WIDTH, game.REC_EDGE))
            x_cord = pygame.mouse.get_pos()[0]
            
            if x_cord <= game.RADIUS:
                x_cord = game.RADIUS
            elif x_cord >= game.WIDTH - game.RADIUS:
                x_cord = game.WIDTH - game.RADIUS
            if game.turn % 2 == 0:
                pygame.draw.circle(game.WINDOW, game.RED, (x_cord, game.REC_EDGE/2), game.RADIUS)
            else:
                pygame.draw.circle(game.WINDOW, game.YELLOW, (x_cord, game.REC_EDGE/2), game.RADIUS)
            pygame.display.update()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                column = int(event.pos[0]//game.REC_EDGE)
        
                # Player 1's turn if turn is even.
                if game.turn % 2 == 0:
                    game.drop_piece(board, column, 1)
                    game.turn += 1
                    game.check_win(board, 1)
                else:
                    game.drop_piece(board, column, 2)
                    game.turn = 0
                    game.check_win(board, 2)
    pygame.draw.rect(game.WINDOW, game.BLACK, (0, 0, game.WIDTH, game.REC_EDGE))
    game.draw_board(board)
    while True:
        pygame.init()
        game.display_win()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()

