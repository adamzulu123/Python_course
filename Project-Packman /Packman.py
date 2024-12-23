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
        #dostepne dla packmana kierunki poruszania
        self.directions = {
            0: (0, -1),  #gora
            1: (0, 1),  #dół
            2: (-1, 0),  #lewo
            3: (1, 0),  #prawo
        }

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
                self.cell.map[new_y][new_x] in {7, 8, 0, 12}):  # Dozwolone pola
            return True
        return False

    def update_position(self):
        if self.player_pos == self.target_pos:  #czy dotatlismy do celu wtedy aktualna i kratka celu sa równe
            if self.can_move(self.new_dir): #sprawdzamy czy jest nowy cel i czy mozemy sie tam poruszyc
                self.direction = self.new_dir #jesli tak to ustawiamy nowy cel

            #sprawdzamy czy packman moze sie poruszac w aktualnym kierunku, czyli tym co wczesniej na klawiaturze wybralismy
            #i tym co w ruchu wczesniej dążylismy, czyli czy mozemy poruszanie kontynuowac
            if self.can_move(self.direction):
                dx, dy = self.directions[self.direction] #zawracamy słownik do poruszania w kierunku gdzie szlismy i aktualizujemy pozycję
                self.target_pos[0] += dx
                self.target_pos[1] += dy
            else:
                #jak nie został zmieniony kierunek i nie da sie poruszać w tym kierunku co wczesniej szlismy to wtedy stoimy w miejscu
                return

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
        x, y = self.player_pos
        self.check_for_score(x, y)

    def check_for_score(self, x, y):
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


''' 
    #FIRST VERSION
    def move(self, dx, dy):
        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        # Sprawdzamy, czy Pacman może przejść do nowej komórki
        if 0 <= new_x < len(self.cell.map[0]) and 0 <= new_y < len(self.cell.map):
            current_tile = self.cell.map[new_y][new_x]

            if current_tile == 7:
                self.score += 10
                self.cell.map[new_y][new_x] = 0
                self.cell.point_timers[(new_y, new_x)] = (time.time(), 7)  # Ustawiamy timer po zjedzeniu

            elif current_tile == 8:
                self.score += 50
                self.cell.map[new_y][new_x] = 0
                self.cell.point_timers[(new_y, new_x)] = (time.time(), 8)

            #super owoc
            elif current_tile == 12:
                self.score += 1000
                self.cell.map[new_y][new_x] = 0
                self.cell.point_timers[(new_y, new_x)] = (time.time(), 12)
                self.cell.last_fruit_time = time.time()
                self.cell.super_fruit_pos = None

            if self.cell.map[new_y][new_x] in {7, 8, 0, 12}:
                self.player_pos[0] = new_x
                self.player_pos[1] = new_y
'''