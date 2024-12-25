import copy
import sys
import pygame
from Cell import Cell
from Packman import Packman
from map_data import map_data
from Ghost import Ghost
from Menu import Menu

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

        self.menu = Menu(self.screen, width, 650)
        self.score = 0
        self.game_over = False

        #inicjujemy mape
        self.cell = Cell(map_data)
        self.packman = Packman(self.cell, tile)

        #inicjujemy duszki
        self.ghost_blue = Ghost(self.cell, "./assets/ghost1.png", 10, tile, [(5, 11), (1, 14), (1, 1), (4, 4), (5, 8)])
        self.ghost_pink = Ghost(self.cell, "./assets/ghost2.png", 11, tile, [(17, 8), (14, 5), (14, 1), (23, 1), (23, 5), (20, 8)])
        self.ghost_red = Ghost(self.cell, "./assets/ghost3.png", 13, tile, [(25, 14), (22, 13), (16, 14), (16, 11), (22, 11), (28, 8)])
        self.ghosts = [self.ghost_blue, self.ghost_pink, self.ghost_red]

    def draw_scoreboard(self):
        pygame.draw.rect(self.screen, (50, 50, 200), (0, 0, width, scoreBoard_height))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.packman.score}", True, (255, 255, 255))
        text_rect = score_text.get_rect(center=(width // 2, scoreBoard_height // 2))

        self.screen.blit(score_text, text_rect) #rysowanie wyniku na srodku score_box

    def run_game(self):
        self.game_over = False

        #tworzenie kopii mapy dla nowej gry
        new_map = copy.deepcopy(map_data)
        #inicjalizacja mapy gry z kopii mapy
        self.cell = Cell(new_map)

        #nowa istancja klasy packman i duszków za kazdym razem odpalania gierki
        self.packman = Packman(self.cell, tile)
        self.packman.score = self.score
        self.ghost_blue = Ghost(self.cell, "./assets/ghost1.png", 10, tile, [(5, 11), (1, 14), (1, 1), (4, 4), (5, 8)])
        self.ghost_pink = Ghost(self.cell, "./assets/ghost2.png", 11, tile, [(17, 8), (14, 5), (14, 1), (23, 1), (23, 5), (20, 8)])
        self.ghost_red = Ghost(self.cell, "./assets/ghost3.png", 13, tile, [(25, 14), (22, 13), (16, 14), (16, 11), (22, 11), (28, 8)])
        self.ghosts = [self.ghost_blue, self.ghost_pink, self.ghost_red]

        while not self.game_over:
            self.screen.fill((0, 0, 0))

            self.draw_scoreboard()

            self.cell.render_map(self.screen, self.packman, tile, cols, rows, scoreBoard_height, self.ghosts)

            #ghost movement
            for ghost in self.ghosts:
                ghost.ghost_move(self.packman.player_pos)
                collision_value = ghost.check_collision(self.packman.player_pos)
                if collision_value == 500:  # Za zabicie duszka w trybie scared +500pkt
                    self.packman.score += 500
                if collision_value == 0:
                    self.game_over = True


            #jak gra sie skonczuła to wyswietlamy na środku wynik i po 2 s cofamy do menu
            if self.game_over:
                font = pygame.font.Font(None, 72)
                game_over_text = font.render(f"Game Over! Score: {self.packman.score}", True, pygame.Color('darkred'))
                self.screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, 650 // 2))
                pygame.display.update()
                pygame.time.wait(2000)
                self.menu.update_score(self.packman.score) #aktualizacja wyniku w menu
                return #powrót do menu


            #sprawdzenie wciskanych klawiszy
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
                    pygame.quit()
                    sys.exit()

            self.clock.tick(20)  # Ograniczamy liczbę klatek na sekundę
            pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.menu.draw()
            action = self.menu.handle_input()
            if action == "start_game":
                self.run_game()

            if self.game_over:
                self.game_over = False
                self.packman.score = 0

if __name__ == "__main__":
    main_game = Main()
    main_game.run()
















