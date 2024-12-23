import random
import pygame

class Ghost:
    def __init__(self, cell, image_path, identifier, tile):
        """
        Tworzy duszka.
        :param map_data: Lista mapy.
        :param image_path: Ścieżka do obrazu duszka.
        :param identifier: Wartość identyfikująca duszka w mapie (np. 10 lub 11).
        """
        self.cell = cell
        self.position = self._find_start_position(identifier)
        self.image = pygame.image.load(image_path)  # Wczytanie obrazu duszka
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.ghost_speed = 0.2
        self.target_pos = list(self.position)

    def _find_start_position(self, identifier):
        return [(x, y) for y in range(len(self.cell.map)) for x in range(len(self.cell.map[0]))
                if self.cell.map[y][x] == identifier]

    def move_randomly(self):
        pass

    def check_collision(self, pacman_pos):
        # Sprawdzanie kolizji duszka z Pacmanem
        return self.position == tuple(pacman_pos)
