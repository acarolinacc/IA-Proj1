import pygame
from play import Game
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
            print("Solving with PC...")
        elif self.selected_option == 2:
            print("Quitting...")
            pygame.quit()
            sys.exit()