from menu import Menu
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cogito Game")

    menu = Menu(screen)
    menu.run()

    pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()