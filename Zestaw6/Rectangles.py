from Points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return "[" + str(self.pt1) + ',' + str(self.pt2) + "]"
    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle(" + str(self.pt1.x) + ',' + str(self.pt1.y) + ',' + str(self.pt2.x) + ',' + str(self.pt2.y) + ")"
    def __eq__(self, other):    # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        return False
    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        center_x = (self.pt1.x + self.pt2.x) / 2
        center_y = (self.pt1.y + self.pt2.y) / 2
        return Point(center_x, center_y)

    def area(self):             # pole powierzchni
        width = abs(self.pt1.x - self.pt2.x)
        height = abs(self.pt1.y - self.pt2.y)
        return width * height
    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)

