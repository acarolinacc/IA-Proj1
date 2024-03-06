import pygame
from play import Game
from game_state import GameState
from pc_play import PCPlay
from board import Board
import macros
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.selected_option = 0
        self.options = ["Play", "PC Solve", "Quit"]

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_options()
            self.handle_events()

            pygame.display.flip()
            self.clock.tick(30)

    def draw_options(self):
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(400, 200 + i * 50))
            self.screen.blit(text_surface, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.select_option()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, option in enumerate(self.options):
                    text_rect = self.font.render(option, True, (0, 0, 0)).get_rect(center=(400, 200 + i * 50))
                    if text_rect.collidepoint(mouse_pos):
                        self.selected_option = i
                        self.select_option()

    def select_option(self):
        if self.selected_option == 0:
            game = Game(self.screen)
            game.run()
        elif self.selected_option == 1:
            self.run_pc_play()
        elif self.selected_option == 2:
            print("Quitting...")
            pygame.quit()

    def run_pc_play(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_pc_play_options()
            self.handle_pc_play_events()

            pygame.display.flip()
            self.clock.tick(30)

    def draw_pc_play_options(self):
        pc_play_options = ["BFS", "DFS", "Back to Main Menu"]
        for i, option in enumerate(pc_play_options):
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(400, 200 + i * 50))
            self.screen.blit(text_surface, text_rect)

    def handle_pc_play_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % 3
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % 3
                elif event.key == pygame.K_RETURN:
                    self.select_pc_play_option()
                elif event.key == pygame.K_ESCAPE:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, option in enumerate(self.options):
                    text_rect = self.font.render(option, True, (0, 0, 0)).get_rect(center=(400, 200 + i * 50))
                    if text_rect.collidepoint(mouse_pos):
                        self.selected_option = i
                        self.select_pc_play_option()

    def select_pc_play_option(self):
        if self.selected_option == 0:
            #initializes necessary objects for initial_state (TODO refactor (change make_initial_moves to board?))
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            if pc_play.bfs(self.screen):
                pc_play.draw_history(pc_play.bfs(), self.screen)
            else:
                print("No solution found")
        elif self.selected_option == 1:
            # Perform DFS
            pass
        elif self.selected_option == 2:
            self.run()
            return


        