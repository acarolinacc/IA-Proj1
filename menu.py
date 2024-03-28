import pygame
from play import Game
from game_state import GameState
from pc_play import PCPlay
from board import Board
import macros
import sys

# Classe que representa o menu do jogo

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('91657.jpg').convert()  
        self.font = pygame.font.Font('Retro Gaming.ttf', 36) 
        self.selected_option = 0
        self.options = ["Play", "PC Solve", "Quit"]

    def run(self):
        while True:
            self.screen.blit(self.bg_image, (0, 0))  
            self.draw_options()
            self.handle_events()

            pygame.display.flip()
            self.clock.tick(30)

    def draw_text_with_shadow(self, text, font, color, y, shadow_color):
        shadow_offset = 2
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        x_centered = (self.screen.get_width() - text_rect.width) // 2
        self.screen.blit(font.render(text, True, shadow_color), (x_centered + shadow_offset, y + shadow_offset))
        self.screen.blit(text_surface, (x_centered, y))

    def draw_title(self, title, font, color, shadow_color):
        text_surface = font.render(title, True, color)
        text_rect = text_surface.get_rect()
        x_centered = (self.screen.get_width() - text_rect.width) // 2
        y = 50
        self.screen.blit(font.render(title, True, shadow_color), (x_centered + 2, y + 2))
        self.screen.blit(text_surface, (x_centered, y))

    def draw_options(self):
        title_font = pygame.font.Font('Retro Gaming.ttf', 48)
        self.draw_title("Cogito", title_font, (255, 215, 0), (0, 0, 0))

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            shadow_color = (0, 0, 0) if i == self.selected_option else (50, 50, 50)
            y = 200 + i * 60
            self.draw_text_with_shadow(option, self.font, color, y, shadow_color)


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
        pc_play_options = ["BFS", "DFS", "Iterative Deepening", "Uniform Cost Search", "Greedy Search", "A* Search", "Back"]
        screen_width, screen_height = self.screen.get_size()  # Obtém as dimensões da tela
        
        # Desenha a imagem de fundo a cada frame
        background_image = pygame.image.load("91657.jpg")
        self.screen.blit(background_image, (0, 0))

        
        for i, option in enumerate(pc_play_options):
            # Muda a cor para amarelo se a opção estiver selecionada, caso contrário, branco
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2 + i * 50 - len(pc_play_options) * 25))
            
            self.screen.blit(text_surface, text_rect)



    def handle_pc_play_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % 7
                elif event.key == pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % 7
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
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            if pc_play.dfs(self.screen):
                pc_play.draw_history(pc_play.dfs(), self.screen)
            else:
                print("No solution found")
        elif self.selected_option == 2:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            if pc_play.iterative_deepening_search(self.screen):
                pc_play.draw_history(pc_play.iterative_deepening_search(), self.screen)
            else:
                print("No solution found")
        elif self.selected_option == 3:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            if pc_play.uniform_cost_search(self.screen):
                pc_play.draw_history(pc_play.uniform_cost_search(), self.screen)
            else:
                print("No solution found")
        elif self.selected_option == 4:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            if pc_play.greedy_search(self.screen):
                pc_play.draw_history(pc_play.greedy_search(), self.screen)
            else:
                print("No solution found")
        elif self.selected_option == 5:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            if pc_play.a_star_search(self.screen):
                pc_play.draw_history(pc_play.a_star_search(), self.screen)
            else:
                print("No solution found")

        elif self.selected_option == 6:
            self.run()
            return


        