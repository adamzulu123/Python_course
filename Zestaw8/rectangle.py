from Points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x2 < x1 or y2<y1:
            raise ValueError("Warunek: x1<x2 lub y1<y2 nie został spełniony")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        #return "[" + str(self.pt1) + ',' + str(self.pt2) + "]"
        return "[({},{}),({},{})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y) #alternatywne rozwiaznie z uzyciem metody format

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ',' + str(self.pt1.y) + ',' + str(self.pt2.x) + ',' + str(self.pt2.y) + ")"
    def __eq__(self, other):    # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        return False
    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def area(self):             # pole powierzchni
        width = abs(self.pt1.x - self.pt2.x)
        height = abs(self.pt1.y - self.pt2.y)
        return width * height
    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)

    def intersection(self, other):  # część wspólna prostokątów
        new_x1 = max(self.pt1.x, other.pt1.x) #wybieramy x lewego dolnego części wspólnej
        new_y1 = max(self.pt1.y, other.pt1.y) #wybieramy y lewego dolnego częsci wspólnej

        new_x2 = min(self.pt2.x, other.pt2.x)
        new_y2 = min(self.pt2.y, other.pt2.y)

        return Rectangle(new_x1, new_y1, new_x2, new_y2)


    def cover(self, other):     # prostąkąt nakrywający oba
        cover_x1 = min(self.pt1.x, other.pt1.x)
        cover_y1 = min(self.pt1.y, other.pt1.y)

        cover_x2 = max(self.pt2.x, other.pt2.x)
        cover_y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(cover_x1, cover_y1, cover_x2, cover_y2)


    def make4(self):            # zwraca krotkę czterech mniejszych
        center_point = self.center #to potrzebujemy do stworzenia prostokątu w lewym dolnym i prawym górnym
        #co potrzeba do stworzenia reszty prostokątów
        #top_left_pt1 = Point(self.pt1.x, center_point.y)
        #top_left_pt2 = Point(center_point.x, self.pt2.y)
        #bottom_right_pt1 = Point(center_point.x, self.pt1.y)
        #bottom_right_pt2 = Point(self.pt2.x, center_point.y)

        #teraz nowe prostokąty
        bottom_left = Rectangle(self.pt1.x, self.pt1.y, center_point.x, center_point.y)
        bottom_right = Rectangle(center_point.x, self.pt1.y, self.pt2.x, center_point.y)
        top_left = Rectangle(self.pt1.x, center_point.y, center_point.x, self.pt2.y)
        top_right = Rectangle(center_point.x, center_point.y, self.pt2.x, self.pt2.y)

        return [bottom_left, bottom_right, top_left, top_right]

    @property
    def center(self):          # zwraca środek prostokąta
        center_x = (self.pt1.x + self.pt2.x) / 2
        center_y = (self.pt1.y + self.pt2.y) / 2
        return Point(center_x, center_y)

    def from_points(points):
        if len(points) != 2:
            raise ValueError("Nie podałeś dokładnie 2 pkt")
        else:
            point1, point2 = points
            return Rectangle(point1.x, point1.y, point2.x, point2.y)

    @property
    def top(self):
        return self.pt2.y
    @property
    def bottom(self):
        return self.pt1.y
    @property
    def left(self):
        return self.pt1.x
    @property
    def right(self):
        return self.pt2.x
    @property
    def width(self):
        return self.pt2.x - self.pt1.x
    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def top_left(self):
        return Point(self.pt1.x, self.pt2.y)
    @property
    def top_right(self):
        return Point(self.pt2.x, self.pt2.y)
    @property
    def bottom_left(self):
        return Point(self.pt1.x, self.pt1.y)
    @property
    def bottom_right(self):
        return Point(self.pt2.x, self.pt1.y)

    #brak definicji metody setter sprawia ze top_left, top_right, bottom_left i bottom_right sa tylko do odczytu
    #jak było w poleceniu zadania




