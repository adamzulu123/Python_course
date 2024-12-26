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

        #best fruit
        self.last_time_best_fruit = time.time()
        self.best_fruit_pos = None
        self.best_fruit_image = pygame.image.load('./assets/best_fruit.png')
        self.best_fruit_image = pygame.transform.scale(self.best_fruit_image, (27, 30))

        #speed fruit
        self.last_time_speed_fruit = time.time()
        self.speed_fruit_pos = None
        self.speed_fruit_image = pygame.image.load('./assets/speed_fruit.png')
        self.speed_fruit_image = pygame.transform.scale(self.speed_fruit_image, (30, 30))

        #slow fruit
        self.last_time_slow_fruit = time.time()
        self.slow_fruit_pos = None
        self.slow_fruit_image = pygame.image.load('./assets/slow_fruit.png')
        self.slow_fruit_image = pygame.transform.scale(self.slow_fruit_image, (30, 30))


    def render_map(self, screen, packman, tile, cols, rows, scoreBoard_height, ghosts):
        """renderowanie całej mapy - od scian do owoców, przez duszki, czy samege pacmana"""
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
                elif self.map[i][j] == 14:
                    pygame.draw.line(screen, pygame.Color("white"),
                                     (x + (0.5 * cols), y),
                                     (x + (0.5 * cols), y + rows), 1)

                elif self.map[i][j] == 40:
                    pygame.draw.line(screen, pygame.Color("yellow"),
                                     (x + (0.5 * cols), y),
                                     (x + (0.5 * cols), y + rows), 1)
                elif self.map[i][j] == 41:
                    pygame.draw.line(screen, pygame.Color("yellow"),
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


        #co 15s sprawn owocu który przyśpiesza pacmana
        if time.time() - self.last_time_speed_fruit > 15:
            self.spawn_speed_fruit()

        if self.speed_fruit_pos:
            speed_x, speed_y = self.speed_fruit_pos
            speed_fx = speed_x * tile + tile // 2
            speed_fy = speed_y * tile + tile // 2 + scoreBoard_height
            screen.blit(self.speed_fruit_image, (speed_fx - 15, speed_fy - 15))

        #co 15s owoc co zwalnia packmana - pułapka na mapie
        if time.time() - self.last_time_slow_fruit > 15:
            self.spawn_slow_fruit()

        if self.slow_fruit_pos:
            slow_x, slow_y = self.slow_fruit_pos
            slow_fx = slow_x * tile + tile // 2
            slow_fy = slow_y * tile + tile // 2 + scoreBoard_height
            screen.blit(self.slow_fruit_image, (slow_fx - 15, slow_fy - 15))


        #co 30s super owoc - najwięcej pkt z owoców
        if time.time() - self.last_time_best_fruit > 30:
            self.spawn_best_fruit()

        if self.best_fruit_pos:
            best_x, best_y = self.best_fruit_pos
            best_fx = best_x * tile + tile // 2
            best_fy = best_y * tile + tile // 2 + scoreBoard_height
            screen.blit(self.best_fruit_image, (best_fx - 15, best_fy - 15))


        #sprawdzamy czy były zdjedzone bo jesli tak to co 10s beda odnawiane te pkt
        to_remove = []
        for (i, j), (last_eaten_time, tile_value) in self.point_timers.items():
            if time.time() - last_eaten_time > 60:
                if self.map[i][j] == 0:
                    self.map[i][j] = tile_value
                    to_remove.append((i, j))

        for coords in to_remove:
            del self.point_timers[coords]


        # Rysowanie Pacmana
        px = packman.player_pos[0] * tile
        py = packman.player_pos[1] * tile + scoreBoard_height  # Przesunięcie o scoreboard_height
        screen.blit(packman.current_image, (px, py))

        for ghost in ghosts:
            gx = ghost.position[0] * tile
            gy = ghost.position[1] * tile + scoreBoard_height
            screen.blit(ghost.image, (gx, gy))

        pygame.display.update()

    def find_empty_positions_for_fruits(self):
        """do szukania pozycji gdzie pojawi się owocek"""
        return [(x, y) for y in range(len(self.map)) for x in range(len(self.map[0]))
                           if self.map[y][x] in {0}]

    def spawn_super_fruit(self):
        """Losowo wybieramy pozycję na mapie, aby pojawił się super owoc"""
        empty_positions = self.find_empty_positions_for_fruits()

        if empty_positions:
            self.super_fruit_pos = random.choice(empty_positions)
            x, y = self.super_fruit_pos
            self.map[y][x] = 12  # Ustawiamy super owoc w wybranej pozycji
            self.last_fruit_time = time.time()

    def spawn_speed_fruit(self):
        """Losowow tak samo jak w przypadku super fruit wybieramy pozycje gdzie pojawi się owoc przyśpieszający """
        empty_positions = self.find_empty_positions_for_fruits()

        if empty_positions:
            self.speed_fruit_pos = random.choice(empty_positions)
            x, y = self.speed_fruit_pos
            self.map[y][x] = 20
            self.last_time_speed_fruit = time.time()

    def spawn_slow_fruit(self):
        empty_positions = self.find_empty_positions_for_fruits()

        if empty_positions:
            self.slow_fruit_pos = random.choice(empty_positions)
            x, y = self.slow_fruit_pos
            self.map[y][x] = 21
            self.last_time_slow_fruit = time.time()

    def spawn_best_fruit(self):
        empty_positions = self.find_empty_positions_for_fruits()

        if empty_positions:
            self.best_fruit_pos = random.choice(empty_positions)
            x, y = self.best_fruit_pos
            self.map[y][x] = 30
            self.last_time_best_fruit = time.time()


