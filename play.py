from board import Board
import pygame
import macros
import sys  
import random
import time

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()    
        self.selected_arrow = 0
        self.game_over = False


    def run(self):
        self.screen.fill((0, 0, 0))
        self.board.draw_board(self.screen)
        pygame.display.flip()
        self.make_random_moves(10) # Make 10 random moves to start the game
        while not self.game_over:
            self.board.draw_board(self.screen)
            self.draw_arrows()  # Draw arrows on top of the board
            self.handle_events()
            pygame.display.flip()


    def draw_arrows(self):
        arrow_width = 30 #values for top and bottom arrows
        arrow_height = 25 #values for top and bottom arrows
        arrow_spacing = 50 
        for i in range(9): #top arrows
            arrow_x = (macros.X_ARROW_OFFSET) + i * arrow_spacing
            arrow_y = macros.Y_ARROW_OFFSET  # Adjusted y-coordinate for top arrows
            color = (255, 255, 0) if i == self.selected_arrow else (255, 255, 255)
            pygame.draw.polygon(self.screen, color, [(arrow_x, arrow_y), 
                                                    (arrow_x + arrow_width, arrow_y), 
                                                    (arrow_x + arrow_width / 2, arrow_y + arrow_height)])

        for i in range(9,18): #rigth arrows
            arrow_x = macros.X_ARROW_OFFSET + macros.BOARD_SIZE
            arrow_y = macros.Y_SIDE_ARROW_OFFSET + (i-9) * arrow_spacing
            color = (255, 255, 0) if i == self.selected_arrow else (255, 255, 255)
            pygame.draw.polygon(self.screen, color, [(arrow_x + arrow_height, arrow_y), 
                                                  (arrow_x + arrow_height, arrow_y + arrow_width), 
                                                  (arrow_x, arrow_y + arrow_width / 2)])

        for i in range(18,27): #bottom arrows
            arrow_x = (macros.X_ARROW_OFFSET) + (8-(i-18)) * arrow_spacing # adjusted x coordinate. 8-(i-18) is used to reverse the order of the arrows , arrows come clockwise
            arrow_y = macros.Y_OFFSET + macros.BOARD_SIZE + (macros.Y_OFFSET-(macros.Y_ARROW_OFFSET + arrow_height)) # Adjusted y-coordinate for bottom arrows  
            color = (255, 255, 0) if i == self.selected_arrow else (255, 255, 255)
            pygame.draw.polygon(self.screen, color, [(arrow_x, arrow_y + arrow_height), 
                                                    (arrow_x + arrow_width, arrow_y + arrow_height), 
                                                    (arrow_x + arrow_width / 2, arrow_y)])

        for i in range(27,36): #left arrows
            arrow_x = macros.X_OFFSET - arrow_height - macros.X_SIDE_ARROW_OFFSET
            arrow_y = macros.Y_SIDE_ARROW_OFFSET + (8-(i-27)) * arrow_spacing
            color = (255, 255, 0) if i == self.selected_arrow else (255, 255, 255)
            pygame.draw.polygon(self.screen, color, [(arrow_x, arrow_y), 
                                                    (arrow_x, arrow_y + arrow_width), 
                                                    (arrow_x + arrow_height, arrow_y + arrow_width / 2)])


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.select_arrow("up")
                elif event.key == pygame.K_DOWN:
                    self.select_arrow("down")
                elif event.key == pygame.K_LEFT:
                    self.select_arrow("left") 
                elif event.key == pygame.K_RIGHT:
                    self.select_arrow("right") 
                elif event.key == pygame.K_RETURN:
                    self.execute_move()
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True


    def select_arrow(self, direction): #simpler version for debugging
        if direction == "left":
            if self.selected_arrow == 0:
                self.selected_arrow = 35
            elif self.selected_arrow > 0 and self.selected_arrow < 9:
                self.selected_arrow -= 1
            elif self.selected_arrow >= 18 and self.selected_arrow < 27:
                self.selected_arrow += 1
            else:
                print("Invalid Movement")
        elif direction == "right":
            if self.selected_arrow >= 0 and self.selected_arrow < 9:
                self.selected_arrow += 1
            elif self.selected_arrow >= 18 and self.selected_arrow < 27:
                self.selected_arrow -= 1
            else:
                print("Invalid Movement")
        elif direction == "up":
            if self.selected_arrow == 35:
                self.selected_arrow = 0
            elif self.selected_arrow >= 27 and self.selected_arrow < 36:
                self.selected_arrow += 1
            elif self.selected_arrow >= 9 and self.selected_arrow < 18:
                self.selected_arrow -= 1
            else:
                print("Invalid Movement")
        elif direction == "down":
            if self.selected_arrow >= 27 and self.selected_arrow < 36:
                self.selected_arrow -= 1
            elif self.selected_arrow >= 9 and self.selected_arrow < 18:
                self.selected_arrow += 1
            else:
                print("Invalid Movement")           


    def execute_move(self):
        if self.selected_arrow < 9: #top arrows
            self.board.shift_column(self.selected_arrow, 'down')
        elif self.selected_arrow < 18 and self.selected_arrow >= 9: #right arrows
            self.board.shift_row(self.selected_arrow - 9, 'left')
        elif self.selected_arrow < 27 and self.selected_arrow >= 18: #bottom arrows
            self.board.shift_column((35 - self.selected_arrow) - 9, 'up')
        elif self.selected_arrow < 36 and self.selected_arrow >= 27: #left arrows
            self.board.shift_row(35 - self.selected_arrow, 'right')


    def make_random_moves(self, num_moves):
        arrows = random.sample(range(36), num_moves)
        for arrow in arrows:
            time.sleep(1.0)
            self.selected_arrow = arrow
            self.execute_move()
            self.board.draw_board(self.screen)
            pygame.display.flip()

    