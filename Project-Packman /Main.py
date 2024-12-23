import sys
import pygame
from Cell import Cell
from Packman import Packman
from map_data import map_data

# Rozmiary mapy
width, height = 900, 950
scoreBoard_height = 100
tile = 30
cols, rows = width // tile, (height - 50) // tile

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))  # Zwiększamy wysokość okna
        self.clock = pygame.time.Clock()

        # Tworzenie instancji klas do generowania mapy i Pacmana
        self.cell = Cell(map_data)
        self.packman = Packman(map_data)

    def draw_scoreboard(self):
        pygame.draw.rect(self.screen, (50, 50, 200), (0, 0, width, scoreBoard_height))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.packman.score}", True, (255, 255, 255))
        text_rect = score_text.get_rect(center=(width // 2, scoreBoard_height // 2))

        self.screen.blit(score_text, text_rect) #rysowanie wyniku na srodku score_box

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            # Rysowanie pola wyników
            self.draw_scoreboard()

            # Rysowanie mapy
            self.cell.render_map(self.screen, self.packman.player_pos, tile, cols, rows, scoreBoard_height)

            # Sprawdzanie, czy wciśnięto klawisze
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.packman.move(0, -1)
            elif keys[pygame.K_DOWN]:
                self.packman.move(0, 1)
            elif keys[pygame.K_LEFT]:
                self.packman.move(-1, 0)
            elif keys[pygame.K_RIGHT]:
                self.packman.move(1, 0)

            # Sprawdzamy wszystkie zdarzenia (np. zamknięcie okna)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick(10)  # Ograniczamy liczbę klatek na sekundę
            pygame.display.flip()


if __name__ == "__main__":
    main_game = Main()
    main_game.run()
















