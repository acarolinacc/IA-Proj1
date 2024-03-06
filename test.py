import pygame
from board import Board
from game_state import GameState
import time


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game_test")

board = Board()
game_state = GameState(board)
children = game_state.children()

for child in children:
    screen.fill((0,0,0))
    child.board.draw_board(screen)
    pygame.display.flip()
    time.sleep(1)

#for child in children:
#    screen.fill((0,0,0))
#    child.board.draw_board(screen)
#    pygame.display.flip()
#    time.sleep(1)
