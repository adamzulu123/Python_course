import random
import pygame

class Ghost:
    def __init__(self, map_data, image_path, identifier, move_delay):
        """
        Tworzy duszka.
        :param map_data: Lista mapy.
        :param image_path: Ścieżka do obrazu duszka.
        :param identifier: Wartość identyfikująca duszka w mapie (np. 10 lub 11).
        """
        self.map = map_data
        self.position = self._find_start_position(identifier)
        self.image = pygame.image.load(image_path)  # Wczytanie obrazu duszka
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.last_move_time = pygame.time.get_ticks()
        self.move_delay = move_delay

    def _find_start_position(self, identifier):
        # Znalezienie pozycji startowej dla duszka o zadanym identyfikatorze
        for y, row in enumerate(self.map):
            for x, value in enumerate(row):
                if value == identifier:
                    return (x, y)
        raise ValueError(f"Nie znaleziono pozycji dla duszka z identyfikatorem {identifier}.")

    def move_randomly(self):
        current_time = pygame.time.get_ticks()

        #sprawdzamy czy opoznienie juz ogarniete
        if current_time - self.last_move_time >= self.move_delay:
            possible_moves = []

            for dx, dy in self.directions:
                new_x, new_y = self.position[0] + dx, self.position[1] + dy
                if 0 <= new_x < len(self.map[0]) and 0 <= new_y < len(self.map):
                    if self.map[new_y][new_x] in {7, 8, 9, 0}:
                        possible_moves.append((new_x, new_y))

            if possible_moves:
                self.position = random.choice(possible_moves)

            self.last_move_time = current_time

    def check_collision(self, pacman_pos):
        # Sprawdzanie kolizji duszka z Pacmanem
        return self.position == tuple(pacman_pos)




