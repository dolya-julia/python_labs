import math
from abc import ABC, abstractmethod

class BaseFigure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def __eq__(self, other):
        if isinstance(other, BaseFigure):
            return self.area() == other.area()
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BaseFigure):
            return self.area() < other.area()
        else:
            return NotImplemented

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def compare(self, other):
        if self.__eq__(other):
            return 'equal'
        elif self.__lt__(other):
            return 'less'
        else:
            return 'larger'


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle(BaseFigure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print('_' * 15)
        print('A(', self.a.x, self.a.y, ')')
        print('B(', self.b.x, self.b.y, ')')
        print('C(', self.c.x, self.c.y, ')')

    def move(self, x, y):
        self.a = Point(self.a.x + x, self.a.y + y)
        self.b = Point(self.b.x + x, self.b.y + y)
        self.c = Point(self.c.x + x, self.c.y + y)

    def area(self):
        ab = math.sqrt((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2)
        bc = math.sqrt((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2)
        ca = math.sqrt((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2)
        p = (ab + bc + ca) / 2
        self.area_tr = math.sqrt(p * (p - ab) * (p - bc) * (p - ca))
        return self.area_tr


class Rectangle(BaseFigure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def print(self):
        print('_' * 15)
        print('A(', self.a.x, self.a.y, ')')
        print('B(', self.b.x, self.b.y, ')')
        print('C(', self.c.x, self.c.y, ')')
        print('D(', self.d.x, self.d.y, ')')

    def move(self, x, y):
        self.a = Point(self.a.x + x, self.a.y + y)
        self.b = Point(self.b.x + x, self.b.y + y)
        self.c = Point(self.c.x + x, self.c.y + y)
        self.d = Point(self.d.x + x, self.d.y + y)

    def area(self):
        ab = math.sqrt((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2)
        bc = math.sqrt((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2)
        self.area_r = ab * bc
        return self.area_r


if __name__ == '__main__':
    t = Triangle(Point(2, 2), Point(3, 4), Point(4, 2))
    # t.print()
    # t.move(1, -2)
    # t.print()
    # print(t.area())
    r = Rectangle(Point(5, 2), Point(5, 5), Point(9, 5), Point(9, 2))
    # r.print()
    # r.move(1, -2)
    # r.print()
    # print(r.area())
    # t1 = Triangle(Point(2, 2), Point(3, 4), Point(4, 2))
    # t2 = Triangle(Point(2, 2), Point(3, 4), Point(4, 2))
    print(r.compare(r))