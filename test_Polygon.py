from Polygon import Triangle, Rectangle, Circle
import unittest
import math
from io import StringIO
import sys

class TestPolygon(unittest.TestCase):
    
    def setUp(self):
        # 테스트 전에 표준 출력을 캡처하기 위해 StringIO 객체를 사용합니다.
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_rectangle_perimeter(self):
        rect = Rectangle(4, 5)
        rect.calc_perimeter()
        self.assertIn('Perimeter: 20', sys.stdout.getvalue())
        print("test_rectangle_perimeter: Passed")

    def test_rectangle_area(self):
        rect = Rectangle(4, 5)
        rect.calc_area()
        self.assertIn('Area: 25', sys.stdout.getvalue())
        print("test_rectangle_area: Passed")

    def test_triangle_perimeter(self):
        tri = Triangle(3, 4)
        tri.calc_perimeter()
        self.assertIn('Perimeter: 12', sys.stdout.getvalue())
        print("test_triangle_perimeter: Passed")

    def test_triangle_area(self):
        tri = Triangle(3, 4)
        tri.calc_area()
        self.assertIn(f"Area: {math.sqrt(3) / 4 * (4 * 4)}", sys.stdout.getvalue())
        print("test_triangle_area: Passed")

    def test_circle_perimeter(self):
        circ = Circle(0, 3)
        circ.calc_perimeter()
        self.assertIn(f"Perimeter: {2 * 3 * math.pi}", sys.stdout.getvalue())
        print("test_circle_perimeter: Passed")

    def test_circle_area(self):
        circ = Circle(0, 3)
        circ.calc_area()
        self.assertIn(f"Area: {math.pi * 3 * 3}", sys.stdout.getvalue())
        print("test_circle_area: Passed")

    def tearDown(self):
        # 테스트 후에 원래의 표준 출력으로 복원합니다.
        sys.stdout = self.held

if __name__ == '__main__':
    unittest.main()