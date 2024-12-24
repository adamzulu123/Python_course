import random
import pygame
from collections import deque
import math

class Ghost:
    def __init__(self, cell, image_path, identifier, tile, route):
        """
        Tworzy duszka.
        :param map_data: Lista mapy.
        :param image_path: Ścieżka do obrazu duszka.
        :param identifier: Wartość identyfikująca duszka w mapie (np. 10 lub 11).
        """
        self.cell = cell
        self.position = self._find_start_position(identifier)[0]
        self.image = pygame.image.load(image_path)  # Wczytanie obrazu duszka
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.ghost_speed = 0.25
        self.target_pos = list(self.position)
        self.route = route #scieżka domyślna
        self.tile = tile #rozmiar kratki
        self.allowed_tiles = {0, 7, 8, 9, 12}

        self.current_target_index = 0 # Indeks aktualnego celu na trasie
        self.path_to_target = []  # Ścieżka do aktualnego celu

    def _find_start_position(self, identifier):
        return [(x, y) for y in range(len(self.cell.map)) for x in range(len(self.cell.map[0]))
                if self.cell.map[y][x] == identifier]

    def ghost_move(self):
        # Jeśli nie ma ścieżki lub duszek dotarł do celu w trasie
        if not self.path_to_target or self.position == self.route[self.current_target_index]:
            # Ustaw punkt docelowy na kolejny punkt w trasie
            # len(self.route) pozwala na to ze jak przejdziemy cała trase to cofamy sie do poczatku i duch moze krażyć
            self.current_target_index = (self.current_target_index + 1) % len(self.route)
            target = self.route[self.current_target_index]
            self.path_to_target = self.bfs_route(self.position, target)  # Wyznacz ścieżkę do nowego celu

        # Jeśli istnieje ścieżka, wykonaj krok
        if self.path_to_target:
            next_step = self.path_to_target[0]  #pobieramy ale jeszcze nie usuwamy kolejnego kroku ze sciezki
            '''
            Mechanizm płynnego poruszania duszka: 
            *delta - dystans w kratkach do przebycia 
            *distance - realny dystans do przebycia do pkt docelowego (tak zawana delta) 
            !!!dlaczego nowa pozycje obliczamy w taki sposób deltaY/distance *self.ghost_speed, bo dzieki algorytmowi 
            bfs który wyznacza nasza scieżke po kratkach i tak zawsze bedziemy poruszali sie wzdłuż osi X lub Y, wiec 
            i tak nie bedzie sytuacji ze szybkiej bedzei pojsc na ukos bo idziemy kratka po kratce tak jak bfs kazał!!!
            '''
            deltaX = next_step[0] - self.position[0]
            deltaY = next_step[1] - self.position[1]

            distance = math.sqrt(deltaX ** 2 + deltaY **2)

            if distance <= self.ghost_speed:
                self.position = next_step #od razy skaczemy do pkt

            else:
                self.position = (self.position[0] + (deltaX/distance * self.ghost_speed),
                                 self.position[1] + (deltaY/distance * self.ghost_speed))

            if self.position == next_step:
                self.path_to_target.pop(0)

    def check_collision(self, pacman_pos):
        ghost_pos = (round(self.position[0]), round(self.position[1]))
        pacman_pos = (round(pacman_pos[0]), round(pacman_pos[1]))
        # sprawdzamy po zaokragleniu bo nasze płynne przesuwanie powoduje rozjezdzaja sie ich pozycje i np. moga przez siebie przejechac
        return ghost_pos == pacman_pos


    def bfs_route(self, start, target):
        """
        Jak sciezka nie zostanie znaleziona to zwracamy None, a jesli jest to wtedy lista pkt.
        Dlaczego jest lepszy niz DFS bo przeglda nasza mape (graf) warstwowo a nie kazda krawedz od poczatku do konca,
        zaczyna od najblizszych sasiadów
        """
        rows, cols = len(self.cell.map), len(self.cell.map[0])
        queue = deque([(start, [start])])  #kolejka do przechowywaia pozycji i sciezki do nastepnej pozycji
        visited = set()

        while queue:
            (x, y), path = queue.popleft() #pierwszy element z kolejki

            if (x, y) == target:
                #print(f"Found path: {path}")
                return path

            if (x, y) not in visited:
                visited.add((x, y))
                #sprawdzamy sąsiednie kratki
                for dx, dy in self.directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < cols and 0 <= ny < rows and (nx, ny) not in visited:
                        if self.cell.map[ny][nx] in self.allowed_tiles:
                            queue.append(((nx, ny), path + [(nx, ny)]))

        return None  #jak nie znaleziono sciezki











