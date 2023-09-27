class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z
        
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z
        
    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z
        
    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
            
    def __getitem__(self, item):
        if item == "x":
            return f"x = {self.x}"
        
        elif item == "y":
            return f"y = {self.y}"
                
        elif item == "z":
            return f"z = {self.z}"

    def __setitem__(self, key, value):
        if key == "x":
            self.x = value
        
        elif key == "y":
            self.y = value
            
        elif key == "z":
            self.z = value 


p1 = Point3D(12, 15, 18)        
p2 = Point3D(6, 3, 9)
print("Сложение координат:", p1 + p2)
print("Вычитание координат:", p1 - p2)
print("Умножение координат:", p1 * p2)
print("Деление координат", p1 / p2)
print("Сравнение координат:", p1 == p2)
print(p1["x"], p2["x"])
print(p1["y"], p2["y"])
print(p1["z"], p2["z"])
p1["x"] = 345
print("Перезаписываем координату х:", p1["x"])