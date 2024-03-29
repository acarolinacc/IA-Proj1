import pygame
from board import Board
from game_state import GameState
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cogito Menu")

board = Board()
board1 = Board()
game_state = GameState(board)
game_state1 = GameState(board1)

game_state.shift_column(4,'up')
game_state.shift_column(3,'down')
game_state.shift_column(4,'up')
game_state.shift_column(5,'down')

print(len(game_state.move_history))

i = 0

for child in game_state.move_history:
    screen.fill((0,0,0))
    child.draw_board(screen)
    i+=1
    print(i)
    pygame.display.flip()
    time.sleep(1)
