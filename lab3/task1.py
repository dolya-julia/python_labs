import math
import numbers
from abc import ABC, abstractmethod


class TriangleNotExist(Exception):
    def __init__(self, message="The triangle doesn't exist. Points on the same line."):
        self.message = message
        super().__init__(self.message)


class RectangleNotExist(Exception):
    def __init__(self, message="The Rectangle doesn't exist."):
        self.message = message
        super().__init__(self.message)


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
        if not isinstance(other, BaseFigure):
            raise TypeError("the argument must be an object")
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
        self.id = id(self)
        if abs((self.a.x-self.c.x)*(self.b.y-self.c.y)-(self.b.x-self.c.x)*(self.a.y-self.c.y)) == 0:
            raise TriangleNotExist()

    def print(self):
        print('A(', self.a.x, self.a.y, ')')
        print('B(', self.b.x, self.b.y, ')')
        print('C(', self.c.x, self.c.y, ')')
        print('id = ', self.id)

    def move(self, x, y):
        if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
            raise TypeError("values must be numeric type")
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
        self.id = id(self)
        if (self.b.x - self.a.x)*(self.c.x-self.b.x)+(self.b.y-self.a.y)*(self.c.y-self.b.y) != 0 or (self.d.x - self.a.x) * (self.d.x - self.c.x) + (self.d.y - self.a.y) * (self.d.y - self.c.y) != 0:
            raise RectangleNotExist()

    def print(self):
        print('A(', self.a.x, self.a.y, ')')
        print('B(', self.b.x, self.b.y, ')')
        print('C(', self.c.x, self.c.y, ')')
        print('D(', self.d.x, self.d.y, ')')
        print('id = ', self.id)

    def move(self, x, y):
        if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
            raise TypeError("values must be numeric type")
        self.a = Point(self.a.x + x, self.a.y + y)
        self.b = Point(self.b.x + x, self.b.y + y)
        self.c = Point(self.c.x + x, self.c.y + y)
        self.d = Point(self.d.x + x, self.d.y + y)

    def area(self):
        ab = math.sqrt((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2)
        bc = math.sqrt((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2)
        self.area_rt = ab * bc
        return self.area_rt


if __name__ == '__main__':
    t = Triangle(Point(2, 2), Point(3, 4), Point(4, 2))
    t.print()
    t.move(5, -2)
    t.print()
    # print(t.area())
    r = Rectangle(Point(6, 3), Point(5, 5), Point(9, 5), Point(9, 2))
    # r.print()
    r.move(1, -2)
    r.print()
    # t1 = Triangle(Point(2, 2), Point(2, 2), Point(3, 4))
    # print(r.area())
    # t1 = Triangle(Point(2, 2), Point(3, 4), Point(4, 2))
    # t2 = Triangle(Point(2, 2), Point(3, 4), Point(4, 2))
    # print(r.compare(t))