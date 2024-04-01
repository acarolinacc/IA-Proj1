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
        self.mouse_pos = (0, 0)
        self.start_time = time.time()


    def run(self):
        self.screen.fill((0, 0, 0))
        self.board.draw_board(self.screen)
        pygame.display.flip()
        #self.make_random_moves(10) # Make 10 random moves to start the game
        self.make_initial_moves(macros.NUM_INITIAL_MOVES)
        
        #gameplay
        while not self.game_over:

            self.board.draw_board(self.screen)

            #timer functions
            elapsed_time = int(time.time() - self.start_time)
            self.draw_timer(elapsed_time)

            self.draw_arrows()  # Draw arrows on top of the board
            self.handle_events()
            pygame.display.flip()
            self.check_game_over()
        
        #game over screen
        while True:
            self.draw_game_over()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                

    def draw_timer(self, elapsed_time):
        font = pygame.font.Font('assets/retro.ttf', 20)
        text = font.render("Time: " + str(elapsed_time) + "s", True, (255, 255, 255))

        self.screen.blit(text, (10,10))

    def draw_arrows(self):
        arrow_width = 30
        arrow_height = 25
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = pygame.mouse.get_pos()
                self.selected_arrow_mouse()
            elif event.type == pygame.MOUSEBUTTONUP:
                if(self.mouse_pos == pygame.mouse.get_pos()):
                    self.execute_move()


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


    def selected_arrow_mouse(self):
        arrow_width = 30
        arrow_height = 25
        arrow_spacing = 50
        for i in range(9): #top arrows
            arrow_x = (macros.X_ARROW_OFFSET) + i * arrow_spacing
            arrow_y = macros.Y_ARROW_OFFSET  # Adjusted y-coordinate for top arrows
            if arrow_x <= self.mouse_pos[0] <= arrow_x + arrow_width and arrow_y <= self.mouse_pos[1] <= arrow_y + arrow_height:
                self.selected_arrow = i
                return

        for i in range(9,18): #rigth arrows
            arrow_x = macros.X_ARROW_OFFSET + macros.BOARD_SIZE
            arrow_y = macros.Y_SIDE_ARROW_OFFSET + (i-9) * arrow_spacing
            if arrow_x <= self.mouse_pos[0] <= arrow_x + arrow_height and arrow_y <= self.mouse_pos[1] <= arrow_y + arrow_width:
                self.selected_arrow = i
                return

        for i in range(18,27): #bottom arrows
            arrow_x = (macros.X_ARROW_OFFSET) + (8-(i-18)) * arrow_spacing # adjusted x coordinate. 8-(i-18) is used to reverse the order of the arrows , arrows come clockwise
            arrow_y = macros.Y_OFFSET + macros.BOARD_SIZE + (macros.Y_OFFSET-(macros.Y_ARROW_OFFSET + arrow_height)) # Adjusted y-coordinate for bottom arrows  
            if arrow_x <= self.mouse_pos[0] <= arrow_x + arrow_width and arrow_y <= self.mouse_pos[1] <= arrow_y + arrow_height:
                self.selected_arrow = i
                return

        for i in range(27,36): #left arrows
            arrow_x = macros.X_OFFSET - arrow_height - macros.X_SIDE_ARROW_OFFSET
            arrow_y = macros.Y_SIDE_ARROW_OFFSET + (8-(i-27)) * arrow_spacing
            if arrow_x <= self.mouse_pos[0] <= arrow_x + arrow_height and arrow_y <= self.mouse_pos[1] <= arrow_y + arrow_width:
                self.selected_arrow = i
                return
        self.select_arrow = 0 #if no arrow is selected, select the first arrow

    def execute_move(self):
        if self.selected_arrow < 9: #top arrows
            self.board.shift_column(self.selected_arrow, 'down')
        elif self.selected_arrow < 18 and self.selected_arrow >= 9: #right arrows
            self.board.shift_row(self.selected_arrow - 9, 'left')
        elif self.selected_arrow < 27 and self.selected_arrow >= 18: #bottom arrows
            self.board.shift_column((35 - self.selected_arrow) - 9, 'up')
        elif self.selected_arrow < 36 and self.selected_arrow >= 27: #left arrows
            self.board.shift_row(35 - self.selected_arrow, 'right')


    def make_random_moves(self, num_moves): #makes the initial random moves
        arrows = random.sample(range(36), num_moves)
        for arrow in arrows:
            time.sleep(0.5) #wait 1 second before making the next move
            self.selected_arrow = arrow
            self.execute_move()
            self.board.draw_board(self.screen)
            pygame.display.flip()

    def make_initial_moves(self,num_moves): #perfected version of make_random_moves, only moves columns/rows with x's in them
        make_move = False
        i = 0
        while(i < num_moves):
            self.selected_arrow = random.randint(0,35) #randomly select an arrow
            if self.selected_arrow < 9: #top arrows
                make_move = self.board.has_red_cell("column", self.selected_arrow)
                print(str(make_move) + " " + str(self.selected_arrow))
            elif self.selected_arrow < 18 and self.selected_arrow >= 9: #right arrows
                make_move = self.board.has_red_cell("row", self.selected_arrow - 9)
                print(str(make_move) + " " + str(self.selected_arrow))               
            elif self.selected_arrow < 27 and self.selected_arrow >= 18: #bottom arrows
                make_move = self.board.has_red_cell("column", 35 - self.selected_arrow - 9)
                print(str(make_move) + " " + str(self.selected_arrow))
            elif self.selected_arrow < 36 and self.selected_arrow >= 27: #left arrows
                make_move = self.board.has_red_cell("row", 35 - self.selected_arrow)
                print(str(make_move) + " " + str(self.selected_arrow))

            if make_move:
                i += 1
                time.sleep(0.5) #wait 1 second before making the next move
                self.execute_move()
                self.board.draw_board(self.screen)
                pygame.display.flip()
            else:
                make_move = False  
                continue              

    def check_game_over(self):
        game_over_board = Board()
        game_over_board.initialize_center_cells()
        if self.board.board == game_over_board.board:
            self.game_over = True
            print("Game Over")
            return True
        else:
            return False

    def draw_game_over(self):
        self.screen.fill((0, 0, 0))

        background_image = pygame.image.load("assets/background.jpg") 
        self.screen.blit(background_image, (0, 0))  

        font_victory = pygame.font.Font(None, 72)
        text_victory = font_victory.render("VICTORY!", True, (118,181,197))
        textpos_victory = text_victory.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2 - 50))
        self.screen.blit(text_victory, textpos_victory)

        
        font_press_esc = pygame.font.Font(None, 36)
        text_press_esc = font_press_esc.render("Press Esc to Leave", True, (255, 255, 255))
        textpos_press_esc = text_press_esc.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2 + 80))
        self.screen.blit(text_press_esc, textpos_press_esc)

        pygame.display.flip()
