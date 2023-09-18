from math import pi


class Table:
    def __init__(self, height=None, width=None, radius=None):
        if width is None and radius is None:
            self.height = height
            self.width = height
        elif radius is None:
            self.height = height
            self. width = width
        elif height is None and width is None:
            self.radius = radius

    def calc_area(self):
        raise NotImplementedError("В дочерних методах должен быть определен метод calc_area")


class SquareTable(Table):
    def calc_area(self):
        return self.height * self.width


class RoundTable(Table):
    def calc_area(self):
        return round((pi * (self.radius ** 2)), 2)


t = SquareTable(20, 10, )
print(t.__dict__)
print(t.calc_area())

t1 = RoundTable(None, None, 20)
print(t1.__dict__)
print(t1.calc_area())

t2 = SquareTable(20, None, None)
print(t2.__dict__)
print(t2.calc_area())