import board
from copy import deepcopy

class GameState:

    def __init__(self, board, depth = 0, move_history = []):
        self.board = board
        self.depth = depth
        if(depth == 0):
            self.move_history = [] + move_history + [deepcopy(self.board)] #add first state to history
        else:
            self.move_history = [] + move_history
        self.id = id(self)

    def __hash__(self):
        return hash((self.board, self.depth, tuple(self.move_history)))

    def __eq__(self, other):
        if isinstance(other, GameState):
            return self.board == other.board
        else:
            return False

    
    

    def children(self):
        children = []
        for i in range(self.board.size): #for each possible row/col index apply the associated move
            new_state = deepcopy(self)  # Create a deep copy of the current game state
            children.append(new_state.shift_column(i, 'up'))
        for i in range(self.board.size):
            new_state = deepcopy(self)  
            children.append(new_state.shift_column(i, 'down'))
        for i in range(self.board.size):
            new_state = deepcopy(self)  
            children.append(new_state.shift_row(i, 'right'))
        for i in range(self.board.size): 
            new_state = deepcopy(self)  
            children.append(new_state.shift_row(i, 'left'))
        return children
        
    def goal_state(self):
        new_board = board.Board()
        new_board.initialize_center_cells() #board with center cells red and rest as None
        return self.board == new_board


    #OPERATORS
    def shift_column(self, col, direction):
        self.board.shift_column(col, direction)
        self.depth += 1
        return self

    def shift_row(self, row, direction):
        self.board.shift_row(row, direction)
        self.depth += 1
        return self        