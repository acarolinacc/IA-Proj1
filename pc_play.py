import pygame
from queue import PriorityQueue
import macros
import board
from queue import PriorityQueue
from copy import deepcopy
import heapq
import time


class PCPlay: 

    def __init__(self, initial_state):
        self.initial_state = initial_state
        
    def bfs(self, screen):
        print("BFS")
        queue = [self.initial_state]
        visited = set() # to avoid visiting the same state twice
        start_time = time.time()
        duplicates =0
        while queue:
            state = queue.pop(0)    # get the first state from the queue
            visited.add(state)  # add the state to the visited set


            # Uncomment below lines if you want to visualize the board
            screen.fill((0, 0, 0))
            state.board.draw_board(screen)
            pygame.display.flip()
            
            if state.goal_state():
                print(time.time()-start_time)
                return state.move_history

            for child in state.children():
                if child not in visited:
                    queue.append(child) # add the child state to the queue
                else:
                    duplicates+=1
        return None 



    def dfs(self, screen):
        print("DFS")
        stack = [self.initial_state]
        visited = set()
        start_time = time.time()

        while stack:
            state = stack.pop(0)
            visited.add(state)

            screen.fill((0, 0, 0))
            state.board.draw_board(screen)
            pygame.display.flip()


            if state.goal_state():
                print(time.time()-start_time)
                return state.move_history

            for child in reversed(state.children()):  # traverse children in reverse order
                if child not in visited:
                    stack.append(child)
        return None


    def iterative_deepening_search(self, screen):
        def depth_limited_search(state, depth):
            
            screen.fill((0, 0, 0))
            state.board.draw_board(screen)
            pygame.display.flip()
            if state.goal_state():
                return state.move_history
            if depth == 0:
                return None
            for child in state.children():
                result = depth_limited_search(child, depth-1)
                if result is not None:
                    return result
            return None

        print("Iterative Deepening")
        start_time = time.time()
        max_depth = 20 # max depth to search TODO: this should depend on the level?
        for depth in range(1, max_depth+1):
            result = depth_limited_search(self.initial_state, depth)
            if result is not None:
                print(time.time()-start_time)
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
                    return state.move_history  # Retorna imediatamente ao encontrar o estado objetivo

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
                        heuristic_value = child.board.manhattan_distance_heuristic() 
                        queue.put((heuristic_value, child))

        return None

    def a_star_search(self, screen):
        print("A* Search")
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
                        g = len(state.move_history) + 1  # g(n) = cost so far
                        h = self.manhattan_distance_heuristic(child)  # h(n) = heuristic value of the child state
                        f = g + h  # f(n) = g(n) + h(n)
                        queue.put((f, child))
                    else:
                        existing_g = len(child.move_history)
                        new_g = len(state.move_history) + 1
                        if new_g < existing_g:
                            h = self.manhattan_distance_heuristic(child)
                            f = new_g + h
                            queue.put((f, child))

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

        current_move = len(move_history) - 1  # Começar do final da lista
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
