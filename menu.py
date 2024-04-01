import pygame
from play import Game
from game_state import GameState
from pc_play import PCPlay
from board import Board
import macros
import sys


class Menu:
    """
    A class representing the main menu of the game.

    Attributes:
        screen: Pygame screen to display the menu.
    """
    def __init__(self, screen):
        """
        Initializes the Menu object.

        Args:
            screen: Pygame screen to display the menu.
        """
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('assets/background.jpg').convert()  
        self.font = pygame.font.Font('assets/retro.ttf', 36) 
        self.selected_option = 0
        self.options = ["Play", "PC Solve", "Quit"]

    def run(self):
        """
        Runs the main menu.
        """
        while True:
            self.screen.blit(self.bg_image, (0, 0))  
            self.draw_options()
            self.handle_events()

            pygame.display.flip()
            self.clock.tick(30)

    def draw_text_with_shadow(self, text, font, color, y, shadow_color):
        """
        Draws text with shadow on the screen.

        Args:
            text: Text to be displayed.
            font: Pygame font object.
            color: Color of the text.
            y: Y-coordinate of the text.
            shadow_color: Color of the shadow.
        """
        shadow_offset = 2
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        x_centered = (self.screen.get_width() - text_rect.width) // 2
        self.screen.blit(font.render(text, True, shadow_color), (x_centered + shadow_offset, y + shadow_offset))
        self.screen.blit(text_surface, (x_centered, y))

    def draw_title(self, title, font, color, shadow_color):
        """
        Draws the title on the screen.

        Args:
            title: Title to be displayed.
            font: Pygame font object.
            color: Color of the title.
            shadow_color: Color of the shadow.
        """
        text_surface = font.render(title, True, color)
        text_rect = text_surface.get_rect()
        x_centered = (self.screen.get_width() - text_rect.width) // 2
        y = 50
        self.screen.blit(font.render(title, True, shadow_color), (x_centered + 2, y + 2))
        self.screen.blit(text_surface, (x_centered, y))

    def draw_options(self):
        """
        Draws the menu options on the screen.
        """
        title_font = pygame.font.Font('assets/retro.ttf', 48)
        self.draw_title("Cogito", title_font, (255, 215, 0), (0, 0, 0))

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            shadow_color = (0, 0, 0) if i == self.selected_option else (50, 50, 50)
            y = 200 + i * 60
            self.draw_text_with_shadow(option, self.font, color, y, shadow_color)


    def handle_events(self):
        """
        Handles user events in the menu.
        """
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

    def select_option(self):
        """
        Executes the selected menu option.
        """
        if self.selected_option == 0:
            game = Game(self.screen)
            game.run()
        elif self.selected_option == 1:
            self.run_pc_play()
        elif self.selected_option == 2:
            print("Quitting...")
            pygame.quit()

    def run_pc_play(self):
        """
        Runs the PC solve menu.
        """
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_pc_play_options()
            self.handle_pc_play_events()

            pygame.display.flip()
            self.clock.tick(30)

    def draw_pc_play_options(self):
        """
        Draws PC solve menu options on the screen.
        """
        pc_play_options = ["BFS", "DFS", "Iterative Deepening", "Uniform Cost Search", "Greedy Search", "A* Search", "Back"]
        screen_width, screen_height = self.screen.get_size()  
        
        background_image = pygame.image.load("assets/background.jpg")
        self.screen.blit(background_image, (0, 0))

        
        for i, option in enumerate(pc_play_options):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2 + i * 50 - len(pc_play_options) * 25))
            
            self.screen.blit(text_surface, text_rect)



    def handle_pc_play_events(self):
        """
        Handles user events in the PC solve menu.
        """
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
                    self.selected_option = 6
                    self.select_pc_play_option()
                    return

    def select_pc_play_option(self):
        """
        Executes the selected option in the PC solve menu.
        """
        if self.selected_option == 0:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.bfs(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")

        elif self.selected_option == 1:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.dfs(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")

        elif self.selected_option == 2:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.iterative_deepening_search(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")

        elif self.selected_option == 3:
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.uniform_cost_search(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")

        elif self.selected_option == 4:
            self.run_heuristics_menu("greedy")
                
        elif self.selected_option == 5:
            self.run_heuristics_menu("a*")

        elif self.selected_option == 6:
            self.run()
            return

    def run_heuristics_menu(self, current_algorithm):
        """
        Runs the heuristics menu for a given algorithm.

        Args:
            current_algorithm: The current algorithm being used.
        """
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_heuristics()
            self.handle_heuristics(current_algorithm)

            pygame.display.flip()
            self.clock.tick(30)

    def draw_heuristics(self):
        """
        Draws heuristics menu options on the screen.
        """
        heuristic_options = ["Manhattan Distance","Out of Place Cells","Back"]
        screen_width, screen_height = self.screen.get_size()  
        
        background_image = pygame.image.load("assets/background.jpg")
        self.screen.blit(background_image, (0, 0))

        
        for i, option in enumerate(heuristic_options):
            color = (255, 255, 0) if i == self.selected_option else (255, 255, 255)
            text_surface = self.font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2 + i * 50 - len(heuristic_options) * 25))
            
            self.screen.blit(text_surface, text_rect)
        
    def handle_heuristics(self,current_algorithm):
        """
        Handles user events in the heuristics menu.

        Args:
            current_algorithm: The current algorithm being used.
        """
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
                    self.select_heuristic(current_algorithm)
                elif event.key == pygame.K_ESCAPE:
                    self.selected_option = 2
                    self.select_heuristic("")
                    return

    def select_heuristic(self, current_algorithm):
        """
        Executes the selected heuristic option.

        Args:
            current_algorithm: The current algorithm being used.
        """
        if self.selected_option == 0 and current_algorithm == "greedy": #greedy with manhattan distance
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.greedy_search_manhattan(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")


        elif self.selected_option == 1 and current_algorithm == "greedy": #greedy with out of place cells
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.greedy_search_out_of_place(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")
                
        elif self.selected_option == 0 and current_algorithm == "a*": #a* with manhattan distance
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.a_star_search_manhattan(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")

        elif self.selected_option == 1 and current_algorithm == "a*": #a* with out of place 
            self.screen.fill((0, 0, 0))
            game = Game(self.screen)
            game.make_initial_moves(macros.NUM_INITIAL_MOVES)
            initial_state = GameState(game.board)
            pc_play = PCPlay(initial_state)
            result = pc_play.a_star_search_out_of_place(self.screen) #resulting goal_state move_history

            if result is None:
                print("Solution Not Found")

        elif self.selected_option == 2:
            self.run_pc_play()
            return
