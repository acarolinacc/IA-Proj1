import pygame
import menu
from pc_play import PCPlay
from board import Board
from game_state import GameState
import macros
import time

#pygame.init()
#screen = pygame.display.set_mode((800, 600))
#pygame.display.set_caption("Cogito Menu")
#
#running = True
#while running:
#    screen.fill((0,0,0))
#    level_1_board.draw_board(screen)
#    pygame.display.flip()

#LEVEL 1 EXAMPLE 1 (3 initial movements)

def level_1_ex_1():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Menu")

    level_board_matrix = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, 'X', None, None, None, None, None],
        [None, None, None, 'X', 'X', 'X', None, None, None],
        [None, None, None, None, 'X', 'X', 'X', None, None],
        [None, None, None, 'X', 'X', None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]


    level_board = Board()
    level_board.set_board(level_board_matrix)
    level_state = GameState(level_board)
    level_pc_play = PCPlay(level_state)

    level_pc_play.a_star_search_out_of_place(screen)
    level_pc_play.a_star_search_manhattan(screen)
    level_pc_play.greedy_search_out_of_place(screen)
    level_pc_play.greedy_search_manhattan(screen)
    level_pc_play.uniform_cost_search(screen)
    level_pc_play.iterative_deepening_search(screen)
    level_pc_play.dfs(screen)
    level_pc_play.bfs(screen)

#LEVEL 1 EXAMPLE 2 (3 initial movements)

def level_1_ex_2():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Menu")

    level_board_matrix = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, 'X', None, None, None, None, None],
        [None, None, None, 'X', None, 'X', None, None, None],
        [None, None, None, 'X', 'X', 'X', None, None, None],
        [None, None, None, None, 'X', 'X', None, None, None],
        [None, None, None, None, 'X', None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]


    level_board = Board()
    level_board.set_board(level_board_matrix)
    level_state = GameState(level_board)
    level_pc_play = PCPlay(level_state)

    level_pc_play.a_star_search_out_of_place(screen)
    level_pc_play.a_star_search_manhattan(screen)
    level_pc_play.greedy_search_out_of_place(screen)
    level_pc_play.greedy_search_manhattan(screen)
    level_pc_play.uniform_cost_search(screen)
    level_pc_play.iterative_deepening_search(screen)
    level_pc_play.dfs(screen)
    level_pc_play.bfs(screen)

#LEVEL 2 EXAMPLE 1 (10 initial movements)

def level_2_ex_1():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Menu")

    level_board_matrix = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]


    level_board = Board()
    level_board.set_board(level_board_matrix)
    level_state = GameState(level_board)
    level_pc_play = PCPlay(level_state)

    level_pc_play.a_star_search_out_of_place(screen)
    level_pc_play.a_star_search_manhattan(screen)
    level_pc_play.greedy_search_out_of_place(screen)
    level_pc_play.greedy_search_manhattan(screen)
    level_pc_play.uniform_cost_search(screen)
    level_pc_play.iterative_deepening_search(screen)
    level_pc_play.dfs(screen)
    level_pc_play.bfs(screen)


#LEVEL 2 EXAMPLE 2 (10 initial movements)

def level_2_ex_2():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Menu")

    level_board_matrix = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]


    level_board = Board()
    level_board.set_board(level_board_matrix)
    level_state = GameState(level_board)
    level_pc_play = PCPlay(level_state)

    level_pc_play.a_star_search_out_of_place(screen)
    level_pc_play.a_star_search_manhattan(screen)
    level_pc_play.greedy_search_out_of_place(screen)
    level_pc_play.greedy_search_manhattan(screen)
    level_pc_play.uniform_cost_search(screen)
    level_pc_play.iterative_deepening_search(screen)
    level_pc_play.dfs(screen)
    level_pc_play.bfs(screen)


#LEVEL 3 EXAMPLE 1 (20 initial movements)

def level_3_ex_1():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Menu")

    level_board_matrix = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]


    level_board = Board()
    level_board.set_board(level_board_matrix)
    level_state = GameState(level_board)
    level_pc_play = PCPlay(level_state)

    level_pc_play.a_star_search_out_of_place(screen)
    level_pc_play.a_star_search_manhattan(screen)
    level_pc_play.greedy_search_out_of_place(screen)
    level_pc_play.greedy_search_manhattan(screen)
    level_pc_play.uniform_cost_search(screen)
    level_pc_play.iterative_deepening_search(screen)
    level_pc_play.dfs(screen)
    level_pc_play.bfs(screen)


#LEVEL 3 EXAMPLE 2 (20 initial movements)

def level_3_ex_2():
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Menu")

    level_board_matrix = [
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
    ]


    level_board = Board()
    level_board.set_board(level_board_matrix)
    level_state = GameState(level_board)
    level_pc_play = PCPlay(level_state)

    level_pc_play.a_star_search_out_of_place(screen)
    level_pc_play.a_star_search_manhattan(screen)
    level_pc_play.greedy_search_out_of_place(screen)
    level_pc_play.greedy_search_manhattan(screen)
    level_pc_play.uniform_cost_search(screen)
    level_pc_play.iterative_deepening_search(screen)
    level_pc_play.dfs(screen)
    level_pc_play.bfs(screen)
