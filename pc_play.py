import pygame
from queue import PriorityQueue
import macros
import board

class PCPlay: 

    def __init__(self, initial_state):
        self.initial_state = initial_state
        
    def bfs(self,screen):
        print("BFS")
        queue = [self.initial_state]
        visited = set()

        while queue:
            state = queue.pop(0)
            visited.add(state)
            #TODO: remove draw board from here
            screen.fill((0,0,0))
            state.board.draw_board(screen)
            pygame.display.flip()
            pygame.time.wait(1000)
            if state.goal_state():
                return state.move_history()

            for child in state.children():
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
        
        return None


    def draw_history(self, move_history,screen):
        pygame.display.set_caption("Move History")

        current_move = 0
        running = True

        while running:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if current_move > 0:
                            current_move -= 1
                    elif event.key == pygame.K_RIGHT:
                        if current_move < len(move_history) - 1:
                            current_move += 1

            current_state = move_history[current_move]
            current_state.board.draw_board()

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

    