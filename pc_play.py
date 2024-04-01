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
        visited = set()  
        start_time = time.time()  
        duplicates = 0

        while queue:
            state = queue.pop(0)  
            visited.add(state) 
            #print(f"current state depth: {state.depth}") 

            #Uncomment to display algorithm working
            #screen.fill((0, 0, 0))
            #state.board.draw_board(screen)
            #pygame.display.flip()

            if state.goal_state():
                end_time = time.time() 
                elapsed_time = end_time - start_time
                print(f"BFS completado em {end_time - start_time:.2f} segundos.")
                self.draw_results(elapsed_time, state.move_history, screen)
                return state.move_history

            for child in state.children():
                if child not in visited:
                    queue.append(child) 
                else:
                    duplicates += 1

        end_time = time.time()
        print(f"BFS terminou sem encontrar um estado objetivo em {end_time - start_time:.2f} segundos.")
        return None




    def dfs(self, screen):
        print("DFS")
        stack = [self.initial_state]
        visited = set()
        start_time = time.time()

        while stack:
            state = stack.pop(0)
            visited.add(state)
            #print(f"current state depth: {state.depth}") 

            #Uncomment to display algorithm working
            #screen.fill((0, 0, 0))
            #state.board.draw_board(screen)
            #pygame.display.flip()


            if state.goal_state():
                end_time = time.time()  # Finaliza a medição do tempo
                print(f"DFS completado em {end_time - start_time:.2f} segundos.")
                elapsed_time = end_time - start_time
                self.draw_results(elapsed_time, state.move_history, screen)
                return state.move_history

            for child in reversed(state.children()): 
                if child not in visited:
                    stack.append(child)
        return None


    def iterative_deepening_search(self, screen):
        def depth_limited_search(state, depth):
            
            #Uncomment to display algorithm working
            #screen.fill((0, 0, 0))
            #state.board.draw_board(screen)
            #pygame.display.flip()

            if state.goal_state():
                end_time = time.time()  # Finaliza a medição do tempo
                elapsed_time = end_time - start_time
                self.draw_results(elapsed_time, state.move_history, screen)
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
            print(f"depth: {depth}")
            result = depth_limited_search(self.initial_state, depth)
            if result is not None:
                print(f"Iterative Deepening completado em {time.time() - start_time:.2f} segundos.")
                return result
        return None

    def uniform_cost_search(self, screen):
        print("Uniform Cost Search")
        start_time = time.time()
        queue = []
        heapq.heappush(queue, (0, self.initial_state))
        visited = set()

        while queue:
            cost, state = heapq.heappop(queue)
            if state not in visited:
                visited.add(state)
                
                #Uncomment to display algorithm working
                #screen.fill((0, 0, 0))
                #state.board.draw_board(screen)
                #pygame.display.flip()

                if state.goal_state():
                    end_time = time.time()  # Finaliza a medição do tempo
                    elapsed_time = end_time - start_time
                    self.draw_results(elapsed_time, state.move_history, screen)
                    return state.move_history 

                for child in state.children():
                    if child not in visited:
                        total_cost = cost + child.path_cost()
                        heapq.heappush(queue, (total_cost, child))

        return None


    def greedy_search_manhattan(self, screen):
        print("Greedy Search - Manhattan Distance Heuristic")
        start_time = time.time() 

        queue = PriorityQueue()
        queue.put((0, self.initial_state))  
        visited = set() 

        while not queue.empty():
            _, state = queue.get()  
            if state not in visited:
                visited.add(state)

                #Uncomment to display algorithm working
                #screen.fill((0, 0, 0))
                #state.board.draw_board(screen)
                #pygame.display.flip()

                if state.goal_state(): 
                    end_time = time.time()  # Finaliza a medição do tempo
                    elapsed_time = end_time - start_time
                    print(f"Greedy Search completado em {end_time - start_time:.2f} segundos.")
                    self.draw_results(elapsed_time, state.move_history, screen)
                    return state.move_history

                for child in state.children():
                    if child not in visited:
                        heuristic_value = child.board.manhattan_distance_heuristic() 
                        queue.put((heuristic_value, child))

        return None

    def greedy_search_out_of_place(self, screen):
        print("Greedy Search - Out-of-Place Heuristic")
        start_time = time.time() 

        queue = PriorityQueue()
        queue.put((0, self.initial_state))  
        visited = set() 

        while not queue.empty():
            _, state = queue.get()  
            if state not in visited:
                visited.add(state)
            
                #Uncomment to display algorithm working
                #screen.fill((0, 0, 0))
                #state.board.draw_board(screen)
                #pygame.display.flip()

                if state.goal_state(): 
                    end_time = time.time()  # Finaliza a medição do tempo
                    elapsed_time = end_time - start_time
                    print(f"Greedy Search completado em {end_time - start_time:.2f} segundos.")
                    self.draw_results(elapsed_time, state.move_history, screen)
                    return state.move_history

                for child in state.children():
                    if child not in visited:
                        heuristic_value = child.board.out_of_place_heuristic() 
                        queue.put((heuristic_value, child))

        return None



    def a_star_search_manhattan(self, screen):
        print("A* Search - Manhattan Distance Heuristic")
        start_time = time.time() 

        queue = PriorityQueue()
        queue.put((0, self.initial_state))
        visited = set()

        while not queue.empty():
            _, state = queue.get()
            if state not in visited:
                visited.add(state)

                #Uncomment to display algorithm working
                #screen.fill((0, 0, 0))
                #state.board.draw_board(screen)
                #pygame.display.flip()

                if state.goal_state():
                    end_time = time.time() 
                    elapsed_time = end_time - start_time 
                    print(f"A* Search (manhattan) completado em {end_time - start_time:.2f} segundos.")
                    #self.draw_results(elapsed_time, state.move_history, screen)
                    return state.move_history

                for child in state.children():
                    if child not in visited:
                        g = len(state.move_history) + 1  # g(n) = cost so far
                        h = child.board.manhattan_distance_heuristic()   # h(n) = heuristic value of the child state
                        f = g + h  # f(n) = g(n) + h(n)
                        queue.put((f, child))
                    else:
                        existing_g = len(child.move_history)
                        new_g = len(state.move_history) + 1
                        if new_g < existing_g:
                            h = child.board.manhattan_distance_heuristic() 
                            f = new_g + h
                            queue.put((f, child))

        end_time = time.time() 
        print(f"A* Search (manhattan) terminou sem encontrar um estado objetivo em {end_time - start_time:.2f} segundos.")
        return None

    def a_star_search_out_of_place(self, screen):
        print("A* Search - Out-of-Place Heuristic")
        start_time = time.time() 

        queue = PriorityQueue()
        queue.put((0, self.initial_state))
        visited = set()

        while not queue.empty():
            _, state = queue.get()
            if state not in visited:
                visited.add(state)
                
                #Uncomment to display algorithm working
                #screen.fill((0, 0, 0))
                #state.board.draw_board(screen)
                #pygame.display.flip()

                if state.goal_state():
                    end_time = time.time() 
                    elapsed_time = end_time - start_time 
                    print(f"A* Search (out-of-place) completado em {end_time - start_time:.2f} segundos.")
                    return state.move_history

                for child in state.children():
                    if child not in visited:
                        g = len(state.move_history) + 1  # g(n) = cost so far
                        h = child.board.out_of_place_heuristic()  # h(n) = heuristic value of the child state
                        f = g + h  # f(n) = g(n) + h(n)
                        queue.put((f, child))
                    else:
                        existing_g = len(child.move_history)
                        new_g = len(state.move_history) + 1
                        if new_g < existing_g:
                            h = child.board.out_of_place_heuristic()
                            f = new_g + h
                            queue.put((f, child))

        end_time = time.time() 
        print(f"A* Search (out-of-place) terminou sem encontrar um estado objetivo em {end_time - start_time:.2f} segundos.")
        return None
    
    def draw_history(self, move_history, screen):
        print("draw_history")
        print(f"len={len(move_history)}")
        pygame.display.set_caption("Move History")
        clock = pygame.time.Clock()

        bg_image = pygame.image.load('assets/background.jpg').convert()  
        font = pygame.font.Font('assets/retro.ttf', 18)

        current_move = 0 #começar no inicio da lista (initial_state)
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
            
            caption_text = "Use LEFT and RIGHT keys to navigate steps, ESC to leave"
            caption_render = font.render(caption_text, True, (255, 255, 255))
            caption_rect = caption_render.get_rect(center=(screen.get_width() // 2, screen.get_height() - 50))
            screen.blit(caption_render, caption_rect)

            pygame.display.flip()
            clock.tick(30)


    def draw_results(self, time_taken, move_history, screen):
        pygame.display.set_caption("Results")
        clock = pygame.time.Clock()

        bg_image = pygame.image.load('assets/background.jpg').convert()
        font = pygame.font.Font('assets/retro.ttf', 36)
        button_font = pygame.font.Font('assets/retro.ttf', 30)
        text_color = (255, 255, 255)
        shadow_color = (0, 0, 0, 50)
        text_shadow_offset = 2
        button_color = (234, 182, 118)  # Cor nova para o botão
        button_hover_color = (210, 164, 106)  # Cor mais escura para o estado hover

        button_rect = pygame.Rect(screen.get_width() / 2 - 100, 300, 200, 50)

        total_moves = len(move_history) - 1 #dont account for initial state

        running = True
        while running:
            screen.blit(bg_image, (0, 0))

            mouse_pos = pygame.mouse.get_pos()
            button_hover = button_rect.collidepoint(mouse_pos)

            def draw_text_with_shadow(text, pos, shadow_offset=2):
                text_surface = font.render(text, True, text_color)
                shadow_surface = font.render(text, True, shadow_color)
                text_pos = text_surface.get_rect(center=pos)
                shadow_pos = text_pos.copy()
                shadow_pos.x += shadow_offset
                shadow_pos.y += shadow_offset
                screen.blit(shadow_surface, shadow_pos)
                screen.blit(text_surface, text_pos)

            draw_text_with_shadow(f"Time taken: {time_taken:.2f} seconds", (screen.get_width() / 2, 150))
            draw_text_with_shadow(f"Total moves: {total_moves}", (screen.get_width() / 2, 200))

            pygame.draw.rect(screen, button_hover_color if button_hover else button_color, button_rect)
            button_text = button_font.render("See Steps", True, text_color)
            button_text_rect = button_text.get_rect(center=button_rect.center)
            screen.blit(button_text, button_text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and button_hover:
                    self.draw_history(move_history,screen)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_RETURN:
                        self.draw_history(move_history,screen)
                    elif event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.flip()
            clock.tick(60)
