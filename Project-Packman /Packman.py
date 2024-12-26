import pygame
import random
import time
import math

class Packman:
    def __init__(self, cell, tile_size):
        self.cell = cell
        self.tile_size = tile_size
        self.player_pos = list(self.find_starting_pos())
        #inicjujemy jako kopia listy pozycji startowej
        self.target_pos = self.player_pos[:]  #tutaj przechowujemy kratke docelową aby potem stopnio aktualizowac pozycje packmana
        self.score = 0
        self.direction = 0  # 0: góra, 1: dół, 2: lewo, 3: prawo
        self.new_dir = 0
        self.speed = 0.25  #do regulacji stopnia predkosci poruszania
        self.speed_boost_end_time = 0
        self.slowness_end_time = 0
        self.allowed_tiles = {7, 8, 0, 12, 20, 21, 30, 40, 41, 42}

        #dostepne dla packmana kierunki poruszania
        self.directions = {
            0: (0, -1),  #gora
            1: (0, 1),  #dół
            2: (-1, 0),  #lewo
            3: (1, 0),  #prawo
        }

        self.images = {
            0: [pygame.image.load("./assets/pacman_top.png"), pygame.image.load("./assets/pacman_top_eating.png")],
            1: [pygame.image.load("./assets/pacman_down.png"), pygame.image.load("./assets/pacman_down_eating.png")],
            2: [pygame.image.load("./assets/pacman_left.png"), pygame.image.load("./assets/pacman_left_eating.png")],
            3: [pygame.image.load("./assets/pacman_right.png"), pygame.image.load("./assets/pacman_right_eating.png")]
        }
        self.animation_frame = 0  #0 -otwarta buzia, 1 - jedzenie
        self.update_current_image()

        self.current_image = pygame.image.load("./assets/packman.png") #domyslnie startowo zwykład kulka zółta
        self.current_image = pygame.transform.scale(self.current_image, (30, 30))


    def update_current_image(self):
        """Aktualizuje obraz na podstawie kierunku i animacji."""
        self.current_image = self.images[self.direction][self.animation_frame]
        self.current_image = pygame.transform.scale(self.current_image, (30, 30))


    def find_starting_pos(self):
        """ustalanie pozycji startowej która jest losowa, w obrebie dostepnych pol """
        available_positions = [(x, y) for y in range(len(self.cell.map)) for x in range(len(self.cell.map[0]))
                               if self.cell.map[y][x] in {7, 8}]
        return random.choice(available_positions)

    def can_move(self, direction):
        """Sprawdza, czy Pacman może ruszyć w danym kierunku."""
        dx, dy = self.directions[direction]
        x, y = self.target_pos
        new_x, new_y = x + dx, y + dy
        #sprawdzamy czy nie jest to sciana czy jest w granicach mapy
        if (0 <= new_x < len(self.cell.map[0]) and 0 <= new_y < len(self.cell.map) and
                self.cell.map[new_y][new_x] in self.allowed_tiles):  # Dozwolone pola
            return True
        return False

    def update_position(self):
        """Update pozycji pacmana w zależnosci czy zjadł specialnego owoca czy nie,
         czy jest w srodku pkt (wtedy zamknieta buzia).
         Generalnie przesuwanie pacmana po mapie
        """
        #czyli jesli nadal trwa czas boosta to poruszamy sie szybciej a jak nie to normalnie
        if time.time() < self.speed_boost_end_time:
            self.speed = 0.35
        if time.time() < self.slowness_end_time:
            self.speed = 0.15
        else:
            self.speed = 0.25

        if self.player_pos == self.target_pos: #czy dotarlismy do celu
            self.animation_frame = 0
            self.update_current_image()#aktualizujemy obraz

            # sprawdzamy czy jest nowy cel i czy mozemy sie tam poruszyc - i jesli tak to sie tam poruszamy
            if self.can_move(self.new_dir):
                self.direction = self.new_dir

            #sprawdzamy czy packman moze sie poruszac w aktualnym kierunku, czyli tym co wczesniej na klawiaturze wybralismy
            #i tym co w ruchu wczesniej dążylismy, czyli czy mozemy poruszanie kontynuowac
            if self.can_move(self.direction):
                dx, dy = self.directions[self.direction] #zawracamy słownik do poruszania w kierunku gdzie szlismy i aktualizujemy pozycję
                self.target_pos[0] += dx
                self.target_pos[1] += dy
            else:
                #jak nie został zmieniony kierunek i nie da sie poruszać w tym kierunku co wczesniej szlismy to wtedy stoimy w miejscu
                return

        else: #jak jesteśmy nadal w ruchu to jedzenie
            self.animation_frame = 1
            self.update_current_image()

        #przyłnne przemiejszezenie
        """
        Załóżmu idziemy z (1,1) do (2,1), czyli jestesmy za celem wiec pójdziemy w pierwszym kroku: 
        (1.25, 1) => (1.5, 1) => (1.75, 1) => (2, 1) - no i dla każdego kroku bedzeimy tez sprawdzali czy nie ma tam jakis pkt 
        które mozna do score dodac itp. dzięki funckji check_for_score
        """
        for i in range(2):  #iteracja po dwóch współrzednych niezbednych do poruszania (x, y)
            if self.player_pos[i] < self.target_pos[i]: #sprawdzamy czy packman jest przed celem na danej osi X/Y (czyli na lewo, na dół) od aktualnej pozycji
                self.player_pos[i] = min(self.player_pos[i] + self.speed, self.target_pos[i]) #przemieszanie do celu o wartosc speed
            elif self.player_pos[i] > self.target_pos[i]:#za celem
                self.player_pos[i] = max(self.player_pos[i] - self.speed, self.target_pos[i]) #zatrzymanie dokładnie na poziomie celu


        #spawdzenie czy na trasie nie mamy jakiegos owocka/pkt
        x, y = round(self.player_pos[0]), round(self.player_pos[1])
        self.check_for_score(x, y)

    def check_for_score(self, x, y):
        """sprawdzanie czy packman nie przechodzi przez pole z pkt lub owocem i wykonanie odpowiedniej akcji"""
        #rzutowanie na inty bo inaczej błędy z floatem
        x = int(x)
        y = int(y)

        current_tile = self.cell.map[y][x]

        if current_tile == 7:
            self.score += 10
            self.cell.map[y][x] = 0
            self.cell.point_timers[(y, x)] = (time.time(), 7)  # Ustawiamy timer po zjedzeniu

        elif current_tile == 8:
            self.score += 50
            self.cell.map[y][x] = 0
            self.cell.point_timers[(y, x)] = (time.time(), 8)

        # super owoc
        elif current_tile == 12:
            self.score += 1000
            self.cell.map[y][x] = 0
            self.cell.point_timers[(y, x)] = (time.time(), 12)
            self.cell.last_fruit_time = time.time()
            self.cell.super_fruit_pos = None

        elif current_tile == 20:
            self.cell.map[y][x] = 0
            self.cell.point_timers[(y, x)] = (time.time(), 20)
            self.cell.last_time_speed_fruit = time.time()
            self.cell.speed_fruit_pos = None
            self.speed_boost_end_time = time.time() + 5 #czyli przez 5s od zjedzenia mamy zboostowany speed

        elif current_tile == 21:
            self.cell.map[y][x] = 0
            self.cell.point_timers[(y, x)] = (time.time(), 21)
            self.cell.last_time_slow_fruit = time.time()
            self.cell.slow_fruit_pos = None
            self.slowness_end_time = time.time() + 5

        elif current_tile == 30:
            self.score += 5000
            self.cell.map[y][x] = 0
            self.cell.point_timers[(y, x)] = (time.time(), 30)
            self.cell.last_time_best_fruit = time.time()
            self.cell.best_fruit_pos = None



