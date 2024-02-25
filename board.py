import pygame
import macros

class Board:
    def __init__(self):
        self.size = 9
        self.cell_size = 50
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.initialize_center_cells()

    def __eq__(self, other):
        if len(self.board) != len(other.board) or len(self.board[0]) != len(other.board[0]):
            return False

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != other.board[i][j]:
                    return False

        return True

    def initialize_center_cells(self): #center cells are 'x' all others are 'o'        for i in range(3, 6):
        for i in range(3,6):
            for j in range(3, 6):
                self.board[i][j] = 'X'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def draw_board(self, screen):
        # Draw the board grid
        for row in range(self.size):
            for col in range(self.size):
                pygame.draw.rect(screen, (255, 255, 255), (macros.X_OFFSET + col * self.cell_size, macros.Y_OFFSET + row * self.cell_size, self.cell_size, self.cell_size), 1)

        # Draw stones or marks on the board
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == "X":
                    pygame.draw.circle(screen, (255, 0, 0), (macros.X_OFFSET + col * self.cell_size + self.cell_size // 2, macros.Y_OFFSET + row * self.cell_size + self.cell_size // 2), self.cell_size // 3)
                else:
                    pygame.draw.circle(screen, (0, 255, 0), (macros.X_OFFSET + col * self.cell_size + self.cell_size // 2, macros.Y_OFFSET + row * self.cell_size + self.cell_size // 2), self.cell_size // 3)

    def shift_column(self, col, direction):
        if direction == 'up':
            temp = self.board[0][col]
            for i in range(self.size - 1):
                self.board[i][col] = self.board[i + 1][col]
            self.board[self.size - 1][col] = temp
        else:
            temp = self.board[self.size - 1][col]
            for i in range(self.size - 1, 0, -1):
                self.board[i][col] = self.board[i - 1][col]
            self.board[0][col] = temp

    def shift_row(self, row, direction):
        if direction == 'left':
            temp = self.board[row][0]
            for i in range(self.size - 1):
                self.board[row][i] = self.board[row][i + 1]
            self.board[row][self.size - 1] = temp
        else:
            temp = self.board[row][self.size - 1]
            for i in range(self.size - 1, 0, -1):
                self.board[row][i] = self.board[row][i - 1]
            self.board[row][0] = temp
