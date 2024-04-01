import pygame
import macros
import time

class Board:
    """
    A class representing the game board.

    Attributes:
        size (int): The size of the board.
        cell_size (int): The size of each cell in pixels.
        board (list): A 2D list representing the game board.
    """
    def __init__(self):
        """
        Initializes the Board object.
        """
        self.size = 9
        self.cell_size = 50
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.initialize_center_cells()

        
    def initialize_center_cells(self): #center cells are 'x' all others are None
        """
        Initializes the center cells of the board.
        """
        for i in range(3,6):
            for j in range(3, 6):
                self.board[i][j] = 'X'

    def set_board(self, board):
        """
        Sets the board to the given state.

        Args:
            board (list): A 2D list representing the new board state.
        """
        if len(board) != self.size or any(len(row) != self.size for row in board):
            raise ValueError("Invalid board size. Board must be 9x9.")
        
        self.board = board

    def print_board(self):
        """
        Prints the current state of the board.
        """
        for row in self.board:
            print(row)

    def manhattan_distance_heuristic(self):
        """
        Calculates the Manhattan distance heuristic for the current board state.

        Returns:
            int: The Manhattan distance heuristic value.
        """
        distance = 0
        center_positions = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        for row_index, row in enumerate(self.board):
            for col_index, cell in enumerate(row):
                if cell == 'X': 
                    min_distance = min(abs(row_index - target_row) + abs(col_index - target_col) for target_row, target_col in center_positions)
                    distance += min_distance
        return distance


    def out_of_place_heuristic(self):
        """
        Calculates the out-of-place heuristic for the current board state.

        Returns:
            int: The out-of-place heuristic value.
        """
        center_positions = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        outside_pieces_count = 0

        for row_index, row in enumerate(self.board):
            for col_index, cell in enumerate(row):
                if cell == 'X' and (row_index, col_index) not in center_positions:
                    outside_pieces_count += 1

        return outside_pieces_count


    def __eq__(self, other):
        """
        Checks if two board objects are equal.

        Args:
            other (Board): Another Board object to compare.

        Returns:
            bool: True if the boards are equal, False otherwise.
        """
        if len(self.board) != len(other.board) or len(self.board[0]) != len(other.board[0]):
            return False

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != other.board[i][j]:
                    return False

        return True

    def hash_value(self):
        """
        Computes the hash value of the board.

        Returns:
            int: The hash value of the board.
        """
        return hash(tuple(tuple(row) for row in self.board))


    def draw_board(self, screen):
        """
        Draws the current board state on the screen.

        Args:
            screen (pygame.Surface): The Pygame screen to draw on.
        """
        screen.fill((19, 8, 64))  

        for row in range(self.size):
            for col in range(self.size):
                cell_rect = pygame.Rect(macros.X_OFFSET + col * self.cell_size, macros.Y_OFFSET + row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (255, 255, 255), cell_rect, 2, border_radius=5)  

                if self.board[row][col] == "X":
                    pygame.draw.circle(screen, (231, 214, 100), cell_rect.center, self.cell_size // 3)
                else:
                    pygame.draw.circle(screen, (127, 30, 136, 255), cell_rect.center, self.cell_size // 3)


    def draw_movements(self, screen):
        """
        Draws the movements of the board on the screen.

        Args:
            screen (pygame.Surface): The Pygame screen to draw on.
        """
        screen.fill((19, 8, 64))  

        for row in range(self.size):
            for col in range(self.size):
                cell_rect = pygame.Rect(macros.X_OFFSET + col * self.cell_size, macros.Y_OFFSET + row * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (255, 255, 255), cell_rect, 2, border_radius=5)  

                if self.board[row][col] == "X":
                    pygame.draw.circle(screen, (231, 214, 100), cell_rect.center, self.cell_size // 3)
                else:
                    pygame.draw.circle(screen, (127, 30, 136, 255), cell_rect.center, self.cell_size // 3)


    def shift_column(self, col, direction):
        """
        Shifts a column of the board in the specified direction.

        Args:
            col (int): The column index to shift.
            direction (str): The direction to shift ('up' or 'down').
        """
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
        """
        Shifts a row of the board in the specified direction.

        Args:
            row (int): The row index to shift.
            direction (str): The direction to shift ('left' or 'right').
        """
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


    def is_red_cell(self,row,col):
        """
        Checks if a cell is a red cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            bool: True if the cell is red, False otherwise.
        """
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        return self.board[row][col] == "X"


    def has_red_cell(self,row_or_col,index):
        """
        Checks if a row or column has a red cell.

        Args:
            row_or_col (str): Either 'row' or 'col' indicating whether to check a row or column.
            index (int): The index of the row or column.

        Returns:
            bool: True if the row or column has a red cell, False otherwise.
        """
        if row_or_col == "row":
            for i in range(self.size):
                if self.is_red_cell(index,i):
                    return True
        else:
            for i in range(self.size):
                if self.is_red_cell(i,index):
                    return True
        return False
