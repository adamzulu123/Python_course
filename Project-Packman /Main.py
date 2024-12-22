import sys
import pygame
from Cell import Cell
from Packman import Packman
from map_data import map_data

# Rozmiary mapy
width, height = 900, 950
tile = 30
cols, rows = width // tile, (height - 50) // tile

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        #tworzenie instancji klas do generowanie mapy i packmana
        self.cell = Cell(map_data)
        self.packman = Packman(map_data)

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            self.cell.render_map(self.screen, self.packman.player_pos, tile, cols, rows)

            # Sprawdzenie, czy wciśnięto klawisze
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.packman.move(0, -1)
            elif keys[pygame.K_DOWN]:
                self.packman.move(0, 1)
            elif keys[pygame.K_LEFT]:
                self.packman.move(-1, 0)
            elif keys[pygame.K_RIGHT]:
                self.packman.move(1, 0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick(10)

if __name__ == "__main__":
    main_game = Main()
    main_game.run()
















