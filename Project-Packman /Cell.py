# Reprezentacja labiryntu: 1 to ściana, 0 to przestrzeń otwarta
import sys
import pygame
import numpy as n
import math
import random
class Cell:
    def __init__(self, map_data):
        self.map = map_data

    def render_map(self, screen, player_pos, tile, cols, rows, scoreBoard_height):
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

        # Rysowanie Pacmana
        px = player_pos[0] * tile + tile // 2
        py = player_pos[1] * tile + tile // 2 + scoreBoard_height  # Przesunięcie o scoreboard_height
        pygame.draw.circle(screen, 'green', (px, py), 10)

        pygame.display.update()
