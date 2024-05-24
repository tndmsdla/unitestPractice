import math

class Polygon:
    def __init__(self, point=0, length=0.0):
        self.mPoint = point  # 꼭지점의 갯수
        self.mLength = length  # 한 변의 길이

    def calc_perimeter(self):
        print("Perimeter: empty")

    def calc_area(self):
        print("Area: empty")

class Rectangle(Polygon):
    def __init__(self, point, length):
        super().__init__(point, length)

    def calc_perimeter(self):
        print(f"Perimeter: {self.mPoint * self.mLength}")

    def calc_area(self):
        print(f"Area: {self.mLength * self.mLength}")

class Triangle(Polygon):
    def __init__(self, point, length):
        super().__init__(point, length)

    def calc_perimeter(self):
        print(f"Perimeter: {self.mPoint * self.mLength}")

    def calc_area(self):
        print(f"Area: {math.sqrt(3) / 4 * (self.mLength * self.mLength)}")

class Circle(Polygon):
    def __init__(self, point, length):
        super().__init__(point, length)

    def calc_perimeter(self):
        print(f"Perimeter: {2 * self.mLength * math.pi}")

    def calc_area(self):
        print(f"Area: {math.pi * self.mLength * self.mLength}")
