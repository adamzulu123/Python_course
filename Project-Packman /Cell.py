# Reprezentacja labiryntu: 1 to ściana, 0 to przestrzeń otwarta
import sys
import pygame
import numpy as n
import math
import random
import time


class Cell:
    def __init__(self, map_data):
        self.map = map_data
        self.point_timers = {} #słownik z czasem dla pktów
        self.last_fruit_time = time.time()
        self.super_fruit_pos = None
        self.super_fruit_image = pygame.image.load('./assets/fruit1.png')
        self.super_fruit_image = pygame.transform.scale(self.super_fruit_image, (30, 30))

    def render_map(self, screen, player_pos, tile, cols, rows, scoreBoard_height, ghosts):
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                # Obliczenie współrzędnych z przesunięciem o scoreboard_height
                x = j * cols
                y = i * rows + scoreBoard_height

                if self.map[i][j] == 0:
                    pygame.draw.rect(screen, pygame.Color("Black"), pygame.Rect(x, y, cols, rows))
                elif self.map[i][j] == 1:
                    pygame.draw.line(screen, pygame.Color("blue"), (x + (0.5 * cols), y),
                                     (x + (0.5 * cols), y + rows), 1)
                elif self.map[i][j] == 2:
                    pygame.draw.line(screen, pygame.Color("blue"), (x, y + (0.5 * rows)),
                                     (x + cols, y + (0.5 * rows)), 1)
                elif self.map[i][j] == 3:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [x - (cols * 0.5), y + (0.5 * rows), cols, rows],
                                    0, math.pi / 2, 1)
                elif self.map[i][j] == 4:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [x + (cols * 0.5), y + (0.5 * cols), cols, rows],
                                    math.pi / 2, math.pi, 1)
                elif self.map[i][j] == 5:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [x + (cols * 0.5), y - (0.5 * rows), cols, rows],
                                    math.pi, 3 * math.pi / 2, 1)
                elif self.map[i][j] == 6:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [x - (cols * 0.5), y - (0.5 * rows), cols, rows],
                                    3 * math.pi / 2, 2 * math.pi, 1)
                elif self.map[i][j] == 7:
                    pygame.draw.circle(screen, 'white',
                                       (x + (0.5 * cols), y + (0.5 * rows)), 3)
                elif self.map[i][j] == 8:
                    pygame.draw.circle(screen, 'white',
                                       (x + (0.5 * cols), y + (0.5 * rows)), 7)
                elif self.map[i][j] == 9:
                    pygame.draw.line(screen, pygame.Color("white"),
                                     (x, y + (0.5 * rows)),
                                     (x + cols, y + (0.5 * rows)), 1)



        #co 10s spawn super owocu
        if time.time() - self.last_fruit_time > 10:
            self.spawn_super_fruit()  # Spawning a new super fruit

        if self.super_fruit_pos:
            x, y = self.super_fruit_pos
            sfx = x * tile + tile // 2
            sfy = y * tile + tile // 2 + scoreBoard_height
            screen.blit(self.super_fruit_image, (sfx - 15, sfy-15))

        #sprawdzamy czy były zdjedzone bo jesli tak to co 10s beda odnawiane te pkt
        to_remove = []
        for (i, j), (last_eaten_time, tile_value) in self.point_timers.items():
            if time.time() - last_eaten_time > 30:
                if self.map[i][j] == 0:
                    self.map[i][j] = tile_value
                    to_remove.append((i, j))

        for coords in to_remove:
            del self.point_timers[coords]


        # Rysowanie Pacmana
        px = player_pos[0] * tile + tile // 2
        py = player_pos[1] * tile + tile // 2 + scoreBoard_height  # Przesunięcie o scoreboard_height
        pygame.draw.circle(screen, 'yellow', (px, py), 10)

        #rysowanie duszków
        for ghost in ghosts:
            gx = ghost.position[0] * tile
            gy = ghost.position[1] * tile + scoreBoard_height
            screen.blit(ghost.image, (gx, gy))

        pygame.display.update()

    def spawn_super_fruit(self):
        """Losowo wybieramy pozycję na mapie, aby pojawił się super owoc"""
        empty_positions = [(x, y) for y in range(len(self.map)) for x in range(len(self.map[0]))
                           if self.map[y][x] in {0}]  # Wybieramy pozycje, gdzie jest pusta przestrzeń
        if empty_positions:
            self.super_fruit_pos = random.choice(empty_positions)
            x, y = self.super_fruit_pos
            self.map[y][x] = 12  # Ustawiamy super owoc w wybranej pozycji
            self.last_fruit_time = time.time()



