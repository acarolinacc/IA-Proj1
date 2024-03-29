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

        
    '''
    def goal_state(self):
        board_size = self.board.size if hasattr(self.board, 'size') else self.board.getSize()

        center_positions = []

        if board_size % 2 == 1:
            center_positions.append((board_size // 2, board_size // 2))
        else:
            mid_point = board_size // 2
            center_positions.extend([
                (mid_point - 1, mid_point - 1),
                (mid_point, mid_point - 1),
                (mid_point - 1, mid_point),
                (mid_point, mid_point)
            ])

        board_matrix = self.board.getBoard() if hasattr(self.board, 'getBoard') else self.board.board

        red_pieces_positions = [
            (x, y) for y, row in enumerate(board_matrix)
            for x, cell in enumerate(row) if cell == 'X'
        ]

        if len(red_pieces_positions) != len(center_positions):
            return False

        return all(position in center_positions for position in red_pieces_positions)
    '''

    def goal_state(self):
        goal_board = Board() #initialize_center_cells is called in board.__init__
        goal_state = GameState(goal_board,0,[])
        return goal_state == self


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
    

