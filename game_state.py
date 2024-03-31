from board import Board
from copy import deepcopy

class GameState:
    def __init__(self, board, depth=0, move_history=None):
        self.board = board
        self.depth = depth
        #self.move_history = move_history if move_history is not None else []
        if move_history is None:
            self.move_history = [deepcopy(board)]
        else:
            self.move_history = move_history
        self.id = id(self)

    def path_cost(self):
        return len(self.move_history)

    def add_move_to_history(self):
        self.move_history.append(deepcopy(self.board))

    def __hash__(self):
        board_hash = self.board.hash_value()
        return hash((board_hash, self.depth, tuple([row.hash_value() for row in self.move_history])))

    def __eq__(self, other):
        return isinstance(other, GameState) and self.board == other.board

    def __lt__(self, other):
        return self.path_cost() < other.path_cost()
    

    def children(self):
        children_states = []
        for direction in ['up', 'down', 'right', 'left']:
            for i in range(self.board.size): 
                new_state = deepcopy(self)  
                if direction in ['up', 'down']:
                    new_state.board.shift_column(i, direction) 
                else:
                    new_state.board.shift_row(i, direction)
                new_state.depth += 1 
                new_state.add_move_to_history()  # Update move history for each child state
                children_states.append(new_state)
        return children_states

    
    def goal_state(self):
        # Posições centrais fixas para um tabuleiro 9x9
        center_positions = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        board_matrix = self.board.getBoard() if hasattr(self.board, 'getBoard') else self.board.board

        # Contar quantas peças 'X' estão nas posições centrais
        x_in_center = sum(board_matrix[r][c] == 'X' for r, c in center_positions)

        # Verificar se todas as 9 peças 'X' estão nas posições centrais e só lá
        return x_in_center == 9 and all(cell == 'X' for r, c in center_positions for cell in board_matrix[r])



    #OPERATORS
    def shift_column(self, col, direction):
        self.board.shift_column(col, direction)
        self.depth += 1
        return self

    def shift_row(self, row, direction):
        self.board.shift_row(row, direction)
        self.depth += 1
        return self        
    
    def child_cost(self):
        return 1
    

