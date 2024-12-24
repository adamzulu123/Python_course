import random
import pygame
from collections import deque
import math
import time


class Ghost:
    def __init__(self, cell, image_path, identifier, tile, route):
        """
        :param cell: Obiekt mapy, na której znajduje się duszek.
        :param image_path: Ścieżka do obrazu duszka.
        :param identifier: Wartość identyfikująca duszka w mapie
        :param tile: Rozmiar kratki (mówi o jednostkowej wielkości na mapie).
        :param route: Domyślna trasa duszka.
        """
        self.cell = cell
        self.position = self._find_start_position(identifier)[0]
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.ghost_speed = 0.25
        self.target_pos = list(self.position)
        self.route = route
        self.tile = tile
        self.allowed_tiles = {0, 7, 8, 9, 12}

        #poruszanie po trasie domyślnej
        self.current_target_index = 0 #aktualny indeks trasy
        self.path_to_target = []

        #poruszanie w przypadku gonienia duszka
        self.path_to_current_target = [] #tymczasowa scieżka do gonienia
        self.chase_stop_time = 0 #czas zakończenia ostatniego gonienia przez duszka
        self.is_chasing = False #flaga oznaczajaca brak gonienia
        self.chase_duration = 8  #ile duszek moze gonic (sekundy)
        self.last_chase_time = 0  #czas kiedy ostatnio duszek gonił packmana

    def _find_start_position(self, identifier):
        """
        :param identifier: Wartość identyfikatora, która identyfikuje duszka na mapie.
        :return: Lista współrzędnych (x, y) początkowej pozycji duszka.
        """
        return [(x, y) for y in range(len(self.cell.map)) for x in range(len(self.cell.map[0]))
                if self.cell.map[y][x] == identifier]

    def ghost_move(self, packman_pos):
        """
        Metoda odpowiedzialna za ruch duszka - czy goni Pacmana, czy też porusza się po swojej domyślnej trasie.
        :param packman_pos: Współrzędne Pacmana na mapie.
        """
        if self.is_chasing:
            # jeśli flaga do gonienia jest na TRUE
            self.chase_packman(packman_pos)
        else:
            self.ghost_route_movement()

        #jesli nie goni, ale jestna tyle blisko ze powinien to odpalammy gonienie
        if not self.is_chasing and self.check_packman_nearby(packman_pos):
            if time.time() - self.chase_stop_time > 15: #i jesli mineło 10s od ostatniego gonienia
                self.start_chasing(packman_pos)

    def check_packman_nearby(self, packman_pos):
        """
        Sprawdza czy packman jest na tyle blisko (7 kratek odległosc), aby gonic.
        :param packman_pos: Współrzędne Pacmana na mapie.
        :return: True, jeśli Pacman jest blisko, w przeciwnym razie False.
        """
        deltaX = self.position[0] - packman_pos[0]
        deltaY = self.position[1] - packman_pos[1]
        distance = math.sqrt(deltaX ** 2 + deltaY ** 2)

        return distance < 7

    def start_chasing(self, packman_pos):
        """
        Rozpoczyna gonienie Pacmana przez duszka.
        :param packman_pos: Współrzędne Pacmana na mapie.
        """
        self.is_chasing = True
        self.last_chase_time = time.time()
        self.path_to_target = self.bfs_route(self.position, packman_pos) #pierwsza scieżka
        #kopia tej domyślniej scieżki początkowej jak packman wszedl w obszar i potem bedziemy na tej kopii operowali
        #do znajdywania nowych sciezek jak juz dojdziemy celu tej domyslnej!
        self.path_to_current_target = self.path_to_target
        print("Chasing Pacman!")


    def chase_packman(self, packman_pos):
        """
        Metoda odpowiedzialna za gonienie Pacmana przez duszka. Duszek porusza się w kierunku Pacmana
        aż do momentu, gdy minie czas gonienia lub jako duszek złapie packmana, ale to w klasie MAIN jest rozwiązane.
        :param packman_pos: Współrzędne Pacmana na mapie.
        """

        #czas ile juz goni jesli za długo to reset wszystkiego i przerwanie gonienia
        if time.time() - self.last_chase_time > self.chase_duration:
            self.is_chasing = False
            self.path_to_current_target = []
            self.chase_stop_time = time.time()
            print("Stopped chasing Pacman after 5 seconds.")
            return

        #print(self.path_to_current_target) #do testownaia ja te sciezki wygladaja
        """
        Jesli dotarlismy do zamierzonego pkt to wtedy usuwamy ten pkt ze sciezki i idziemy do next, natomiast jesli 
        to był juz cel aktualnej sceizki to wtedy wyliczamy nowa. 
        czyli duch zawsze idzie do konca sciezki wyznaczonej za danym razem i jak ja skonczy wyznacza nowa do packmana!
        """
        if self.path_to_current_target and self.position == self.path_to_current_target[0]:
            self.path_to_current_target.pop(0) #usuwamy go

            if not self.path_to_current_target:
                self.path_to_current_target = self.bfs_route(self.position, packman_pos)

        if not self.path_to_current_target:
            print(f"No path found to {packman_pos}. Stopping chase.")
            self.is_chasing = False
            return

        next_step = self.path_to_current_target[0] #kolejny krok gdzie chcemy isc

        #obliczamy odległosc do nastepnego pkt
        deltaX = next_step[0] - self.position[0]
        deltaY = next_step[1] - self.position[1]
        distance = math.sqrt(deltaX ** 2 + deltaY ** 2)

        #jesli jest blisko celu to ustawiamy nowa pozcje duszka, a jak nie to płynnie poruszamy w przód
        if distance <= self.ghost_speed:
            self.position = next_step
        else:
            self.position = (self.position[0] + (deltaX / distance * self.ghost_speed),
                             self.position[1] + (deltaY / distance * self.ghost_speed))

    def ghost_route_movement(self):
        """
        Ruch duszka po domyślnej trasie. Jeśli duszek dotrze do celu, przechodzi do kolejnego punktu.
        Jak skończy trase to wtedy cofa się na początek.
        """
        # Jeśli nie ma ścieżki lub duszek dotarł do celu w trasie
        if not self.path_to_target or self.position == self.route[self.current_target_index]:
            # Ustaw punkt docelowy na kolejny punkt w trasie
            # len(self.route) pozwala na to ze jak przejdziemy cała trase to cofamy sie do poczatku i duch moze krażyć
            self.current_target_index = (self.current_target_index + 1) % len(self.route)
            target = self.route[self.current_target_index]
            self.path_to_target = self.bfs_route(self.position, target)  # Wyznacz ścieżkę do nowego celu

        # Jeśli istnieje ścieżka, wykonaj krok
        if self.path_to_target:
            next_step = self.path_to_target[0]  #przypisujemy pole do którego dożymy do zmiennej, ale go nie usuwamy!
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

            distance = math.sqrt(deltaX ** 2 + deltaY ** 2)

            #jeśli dystans mniejszy niz speed to po prostu jako lokalizacje centrum tego pola
            if distance <= self.ghost_speed:
                self.position = next_step

            else:
                self.position = (self.position[0] + (deltaX / distance * self.ghost_speed),
                                 self.position[1] + (deltaY / distance * self.ghost_speed))

            #jak dotarlismy to usuwamy z listy ten pkt do któego dązylismy
            if self.position == next_step:
                self.path_to_target.pop(0)

    def bfs_route(self, start, target):
        """
        Jak sciezka nie zostanie znaleziona to zwracamy None, a jesli jest to wtedy lista pkt.
        Dlaczego jest lepszy niz DFS bo przeglda nasza mape (graf) warstwowo a nie kazda krawedz od poczatku do konca,
        zaczyna od najblizszych sasiadów.
        :param start: Współrzędne punktu startowego.
        :param target: Współrzędne punktu docelowego.
        :return: Lista punktów tworzących najkrótszą ścieżkę.
        """
        start = (round(start[0]), round(start[1]))  # Zaokrąglamy współrzędne startowe
        target = (round(target[0]), round(target[1]))  # Zaokrąglamy cel na wszelki wypadek

        rows, cols = len(self.cell.map), len(self.cell.map[0])
        queue = deque([(start, [start])])  #kolejka do przechowywaia pozycji i sciezki do nastepnej pozycji
        visited = set()

        while queue:
            (x, y), path = queue.popleft()  #pierwszy element z kolejki

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

    def check_collision(self, pacman_pos):
        """
         :param pacman_pos: Współrzędne Pacmana na mapie.
         :return: True, jeśli duszek i Pacman mają tę samą pozycję, w przeciwnym razie False.
         Sprawdzamy po zaokragleniu, bo nasze płynne przesuwanie powoduje że rozjezdzaja sie ich pozycje
         i np duszek może przelecieć przez packmana go nie zauważajac w przypadku bez zaokrąglenia!
         """
        ghost_pos = (round(self.position[0]), round(self.position[1]))
        pacman_pos = (round(pacman_pos[0]), round(pacman_pos[1]))
        return ghost_pos == pacman_pos