from menu import Menu
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Game")

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Menu")

    menu = Menu(screen)
    menu.run()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False                

    
    pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()