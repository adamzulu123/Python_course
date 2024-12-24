import sys
import pygame
from Cell import Cell
from Packman import Packman
from map_data import map_data
from Ghost import Ghost

# Rozmiary mapy
width, height = 900, 950
scoreBoard_height = 100
tile = 30
cols, rows = width // tile, (height - 50) // tile

class Main:
    def __init__(self):
        pygame.init()
        # wysokosc sztynwno ustawiona bo juz generowanie mapy ustawiłem tak ze jak zmieniam na mniejsze to
        #wszystko sie rozjeżdza i troche nie wiem i nie chce się z tym męczyc
        self.screen = pygame.display.set_mode((width, 650))
        self.clock = pygame.time.Clock()

        self.game_over = False

        # Tworzenie instancji klas do generowania mapy i Pacmana
        self.cell = Cell(map_data)
        self.packman = Packman(self.cell, tile)


        #[(9, 6), (6, 5), (2, 2), (14,2), (11,5)]
        #inicjujemy niebieskiego ducha z pkt jego domyslnej trasy
        self.ghost_blue = Ghost(self.cell, "./assets/ghost1.png", 10, tile, [(5, 11), (1, 14), (1, 1), (4, 4), (5, 8)])

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
            self.cell.render_map(self.screen, self.packman.player_pos, tile, cols, rows, scoreBoard_height, self.ghost_blue)

            #ghost movement
            self.ghost_blue.ghost_move()
            if self.ghost_blue.check_collision(self.packman.player_pos):
                self.game_over = True


            # Jeśli gra zakończona, wyświetlamy wynik
            if self.game_over:
                font = pygame.font.Font(None, 72)
                game_over_text = font.render(f"Game Over! Score: {self.packman.score}", True, (255, 0, 0))
                self.screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2))
                pygame.display.update()
                pygame.time.wait(2000)
                running = False
                continue

            # Sprawdzanie, czy wciśnięto klawisze
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.packman.new_dir = 0
            elif keys[pygame.K_DOWN]:
                self.packman.new_dir = 1
            elif keys[pygame.K_LEFT]:
                self.packman.new_dir = 2
            elif keys[pygame.K_RIGHT]:
                self.packman.new_dir = 3

            self.packman.update_position()

            # Sprawdzamy wszystkie zdarzenia (np. zamknięcie okna)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick(20)  # Ograniczamy liczbę klatek na sekundę
            pygame.display.flip()


if __name__ == "__main__":
    main_game = Main()
    main_game.run()
















