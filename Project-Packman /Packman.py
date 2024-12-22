import pygame
import random

class Packman:
    def __init__(self, map_data):
        self.map = map_data
        self.player_pos = list(self.find_starting_pos())

    def find_starting_pos(self):
        # Wyszukujemy dostępne pozycje Pacmana
        available_positions = [(x, y) for y in range(len(self.map)) for x in range(len(self.map[0])) if self.map[y][x] in {0, 7, 8}]
        return random.choice(available_positions)

    def move(self, dx, dy):
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        # Sprawdzamy, czy Pacman może przejść do nowej komórki
        if 0 <= new_x < len(self.map[0]) and 0 <= new_y < len(self.map) and self.map[new_y][new_x] in {7, 8, 0}:  # Można przejść przez te komórki
            self.player_pos[0] = new_x
            self.player_pos[1] = new_y
