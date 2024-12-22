# Reprezentacja labiryntu: 1 to ściana, 0 to przestrzeń otwarta
import sys
import pygame
import numpy as n
import math
import random
class Cell:
    def __init__(self, map_data):
        self.map = map_data

    def render_map(self, screen, player_pos, tile, cols, rows, offset_y):
        # Zmieniamy renderowanie mapy, dodając margines na górze
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 0:
                    pygame.draw.rect(screen, pygame.Color("Black"), pygame.Rect(j * cols, i * rows + offset_y, cols, rows))
                if self.map[i][j] == 1:
                    pygame.draw.line(screen, pygame.Color("blue"), (j * cols + (0.5 * cols), i * rows + offset_y),
                                     (j * cols + (0.5 * cols), i * rows + offset_y + rows), 1)
                if self.map[i][j] == 2:
                    pygame.draw.line(screen, pygame.Color("blue"), (j * cols, i * rows + (0.5 * rows) + offset_y),
                                     (j * cols + cols, i * rows + (0.5 * rows) + offset_y), 1)
                if self.map[i][j] == 3:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [(j * cols - (cols * 0.5)), (i * rows + (0.5 * rows) + offset_y), cols, rows], 0, math.pi / 2,
                                    1)
                if self.map[i][j] == 4:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [(j * cols + (cols * 0.5)), (i * rows + (0.5 * cols) + offset_y), cols, rows], math.pi / 2,
                                    math.pi, 1)
                if self.map[i][j] == 5:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [j * cols + (cols * 0.5), (i * rows - (0.5 * rows) + offset_y), cols, rows], math.pi,
                                    3 * math.pi / 2, 1)
                if self.map[i][j] == 6:
                    pygame.draw.arc(screen, pygame.Color("blue"),
                                    [(j * cols - (cols * 0.5)), i * rows - (0.5 * rows) + offset_y, cols, rows], 3 * math.pi / 2,
                                    2 * math.pi, 1)
                if self.map[i][j] == 7:
                    pygame.draw.circle(screen, 'white', (j * cols + (0.5 * cols), i * rows + (0.5 * rows) + offset_y), 3)
                if self.map[i][j] == 8:
                    pygame.draw.circle(screen, 'white', (j * cols + (0.5 * cols), i * rows + (0.5 * rows) + offset_y), 7)
                if self.map[i][j] == 9:
                    pygame.draw.line(screen, pygame.Color("white"), (j * cols, i * rows + (0.5 * rows) + offset_y),
                                     (j * cols + cols, i * rows + (0.5 * rows) + offset_y), 1)

        # Rysowanie Pacmana
        pygame.draw.circle(screen, 'green', (player_pos[0] * tile + tile // 2, player_pos[1] * tile + tile // 2 + offset_y), 10)
        pygame.display.update()
