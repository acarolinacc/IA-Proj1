import pygame
from queue import PriorityQueue
import macros
import board
from queue import PriorityQueue
from copy import deepcopy
import heapq


class PCPlay: 

    def __init__(self, initial_state):
        self.initial_state = initial_state
        
    def bfs(self, screen):
        print("BFS")
        queue = [self.initial_state]
        visited = set()
        duplicates = 0

        while queue:
            state = queue.pop(0)

            if state in visited:
                duplicates += 1
                continue

            visited.add(state)

            # Uncomment below lines if you want to visualize the board
            # screen.fill((0, 0, 0))
            # state.board.draw_board(screen)
            # pygame.display.flip()
            # pygame.time.wait(50)

            if state.goal_state():
                return state.move_history

            for child in state.children():
                queue.append(child)

        print(f"duplicates = {duplicates}")  # Print the count of duplicates
        return None



    def dfs(self, screen):
        print("DFS")
        stack = [self.initial_state] 
        visited = set()  

        while stack:
            state = stack.pop()  
            if state not in visited:
                visited.add(state)
                screen.fill((0, 0, 0))
                state.board.draw_board(screen)
                pygame.display.flip()
                pygame.time.wait(50)

                if state.goal_state():
                    return state.move_history

                for child in reversed(state.children()): 
                    if child not in visited:
                        stack.append(child)

        return None

    def iterative_deepening_search(self, screen):
        def depth_limited_search(state, depth, screen):
            if state.goal_state(): 
                return state.move_history
            if depth == 0:
                return None
            for child in state.children():
                result = depth_limited_search(child, depth - 1, screen)
                if result is not None:
                    return result
            return None

        print("Iterative Deepening")
        for depth in range(1, 100):  
            result = depth_limited_search(self.initial_state, depth, screen)
            if result is not None:
                return result
        return None


    def uniform_cost_search(self, screen):
        print("Uniform Cost Search")
        queue = []
        heapq.heappush(queue, (0, self.initial_state)) 
        visited = set() 
        while queue:
            cost, state = heapq.heappop(queue)  
            if state not in visited:
                visited.add(state)
                screen.fill((0, 0, 0))
                state.board.draw_board(screen)
                pygame.display.flip()

                if state.goal_state():  
                    return state.move_history()

                for child in state.children():
                    if child not in visited:
                        total_cost = cost + child.path_cost() 
                        heapq.heappush(queue, (total_cost, child))

        return None


    def greedy_search(self, screen):
        print("Greedy Search")
        queue = PriorityQueue()
        queue.put((0, self.initial_state))  
        visited = set() 

        while not queue.empty():
            _, state = queue.get()  
            if state not in visited:
                visited.add(state)
                screen.fill((0, 0, 0))
                state.board.draw_board(screen)
                pygame.display.flip()

                if state.goal_state(): 
                    return state.move_history

                for child in state.children():
                    if child not in visited:
                        heuristic_value = child.board.manhattan_distance_heuristic()  # Calcula a heurística para o estado filho
                        queue.put((heuristic_value, child))

        return None



    def a_star_search(self, screen):
        print("A* Search")
        queue = []
        heapq.heappush(queue, (0, 0, self.initial_state)) 
        visited = set() 

        while queue:
            total_cost, real_cost, state = heapq.heappop(queue)
            state_hash = hash(state)
            if state_hash not in visited:
                visited.add(state_hash)
                screen.fill((0, 0, 0))
                state.board.draw_board(screen)
                pygame.display.flip()
                
                if state.goal_state():  
                    return state.move_history()
                
                for child in state.children():
                    child_hash = hash(child)
                    if child_hash not in visited:
                        child_real_cost = real_cost + child.child_cost()  
                        child_total_cost = child_real_cost + self.manhattan_distance_heuristic(child)
                        heapq.heappush(queue, (child_total_cost, child_real_cost, child))
                        
        return None



    def manhattan_distance_heuristic(self, state):
        goal_positions = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
        total_distance = 0

        for row_index, row in enumerate(state.board.board):
            for col_index, cell in enumerate(row):
                if cell == 'X':  
                    min_distance = min(abs(row_index - goal[0]) + abs(col_index - goal[1]) for goal in goal_positions)
                    total_distance += min_distance

        return total_distance

        
    def draw_history(self, move_history, screen):
        print("draw_history")
        print(f"len={len(move_history)}")
        pygame.display.set_caption("Move History")
        clock = pygame.time.Clock()

        bg_image = pygame.image.load('assets/background.jpg').convert()  

        current_move = 0
        running = True

        while running:
            screen.blit(bg_image, (0, 0)) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_LEFT:
                        if current_move > 0:
                            current_move -= 1
                    elif event.key == pygame.K_RIGHT:
                        if current_move < len(move_history) - 1:
                            current_move += 1

            current_state = move_history[current_move]
            current_state.draw_board(screen)  # Pass the screen to draw_board
            
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()


    