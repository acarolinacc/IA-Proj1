from board import Board
from copy import deepcopy
import pygame

class GameState:
    """
    A class representing a state of the game.

    Attributes:
        board (Board): The game board.
        depth (int): The depth of the state in the search tree.
        move_history (list): A list of boards representing the move history.
        id (int): The unique identifier of the state.
    """
    def __init__(self, board, depth=0, move_history=None):
        """
        Initializes the GameState object.

        Args:
            board (Board): The game board.
            depth (int): The depth of the state in the search tree.
            move_history (list): A list of boards representing the move history.
        """
        self.board = board
        self.depth = depth
        #self.move_history = move_history if move_history is not None else []
        if move_history is None:
            self.move_history = [deepcopy(board)]
        else:
            self.move_history = move_history
        self.id = id(self)

    def path_cost(self):
        """
        Calculates the path cost of the state.

        Returns:
            int: The path cost.
        """
        return len(self.move_history)

    def add_move_to_history(self):
        """
        Adds the current board state to the move history.
        """
        self.move_history.append(deepcopy(self.board))

    def __hash__(self): #used to search values in visited sets. takes into account only the current state of the board
        """
        Computes the hash value of the state.

        Returns:
            int: The hash value.
        """
        board_hash = self.board.hash_value()
        return board_hash

    def __eq__(self, other):
        """
        Checks if two states are equal.

        Args:
            other (GameState): Another GameState object to compare.

        Returns:
            bool: True if the states are equal, False otherwise.
        """
        return isinstance(other, GameState) and self.board == other.board

    def __lt__(self, other):
        """
        Compares the states based on path cost.

        Args:
            other (GameState): Another GameState object to compare.

        Returns:
            bool: True if self has a lower path cost than other, False otherwise.
        """
        return self.path_cost() < other.path_cost()
    

    def children(self):
        """
        Generates child states from the current state.

        Returns:
            list: A list of child states.
        """
        children_states = []
        for direction in ['up', 'down', 'right', 'left']:
            for i in range(self.board.size): 
                new_state = deepcopy(self)  
                if direction in ['up', 'down']:
                    if new_state.board.has_red_cell('col',i): #only create children if column has 'x', in other words if shifting results in an observable alteration 
                        new_state.board.shift_column(i, direction) 
                else:
                    if new_state.board.has_red_cell('row',i): #only create children if row has 'x', in other words if shifting results in an observable alteration 
                        new_state.board.shift_row(i, direction)
                new_state.depth += 1 
                new_state.add_move_to_history()  # Update move history for each child state
                children_states.append(new_state)
        return children_states

    def goal_state(self):
        """
        Checks if the current state is a goal state.

        Returns:
            bool: True if the state is a goal state, False otherwise.
        """
        center_positions = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        board_matrix = self.board.getBoard() if hasattr(self.board, 'getBoard') else self.board.board

        # Verificar se todas as 9 peças 'X' estão nas posições centrais
        x_in_center = sum(board_matrix[r][c] == 'X' for r, c in center_positions)

        # Verificar se não há 'X' fora das posições centrais
        x_outside_center = sum(board_matrix[r][c] == 'X' for r in range(9) for c in range(9) if (r, c) not in center_positions)

        return x_in_center == 9 and x_outside_center == 0
    
    '''
    def goal_state(self):
        goal_board = Board() #initialize_center_cells is called in board.__init__
        goal_state = GameState(goal_board,0,[])
        return self == goal_state
    '''


    #OPERATORS
    def shift_column(self, col, direction):
        """
        Shifts a column of the board in the specified direction.

        Args:
            col (int): The column index to shift.
            direction (str): The direction to shift ('up' or 'down').

        Returns:
            GameState: The resulting game state after the shift.
        """
        self.board.shift_column(col, direction)
        self.depth += 1
        return self

    def shift_row(self, row, direction):
        """
        Shifts a row of the board in the specified direction.

        Args:
            row (int): The row index to shift.
            direction (str): The direction to shift ('left' or 'right').

        Returns:
            GameState: The resulting game state after the shift.
        """
        self.board.shift_row(row, direction)
        self.depth += 1
        return self        
    
    def child_cost(self):
        """
        Calculates the cost of reaching a child state from the current state.

        Returns:
            int: The cost of reaching a child state.
        """
        return 1
    
    def draw_time_taken(self, screen, time_taken):
        """
        Draws the time taken to solve the puzzle on the screen.

        Args:
            screen (pygame.Surface): The Pygame screen to draw on.
            time_taken (float): The time taken to solve the puzzle.
        """
        screen.fill((19, 8, 64))
    
        font = pygame.font.Font(None, 36)
        text = font.render("Tempo total: " + str(round(time_taken, 2)) + "s", True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()