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

game_state1.shift_column(4,'up')
game_state1.shift_column(4,'down')

print(hash(game_state))
print(hash(game_state1))


