import unittest
from filerepo import FileRepo
from point import Point
from random import randint

def randomPoints(n:int) -> list:
    """
    Generate a list of n random points.
    """
    points = []
    for _ in range(n):
        x = randint(0, 500)
        y = randint(0, 500)
        points.append(Point(x, y))
    return points

class TestFileRepo(unittest.TestCase):
    def setUp(self):
        self.repo = FileRepo()
        self.points = randomPoints(1000)
        for point in self.points:
            self.repo.add_point(point)
    def test_save(self):
        self.repo.save(self.repo.get_points())
    def test_validFileName(self):
        fileName = "test.txt"
        self.assertEqual(self.repo.validFileName(fileName), fileName)
    def test_clear_points(self):
        self.repo.clear_points()
        self.assertEqual(self.repo.get_points(), [])
    def test_get_points(self):
        self.assertEqual(self.repo.get_points(), self.points)
    def test_add_point(self):
        point = Point(1, 1)
        self.repo.add_point(point)
        self.assertEqual(self.repo.get_points(), self.points + [point])
    def test_get(self):
        for point in self.points:
            self.assertEqual(point.get(), (point.get_x(), point.get_y()))
    def test_set(self):
        for point in self.points:
            point.set(2, 3)
            self.assertEqual(point.get(), (2, 3))
    def test_get_x(self):
        for point in self.points:
            self.assertEqual(point.get_x(), point.x)
    def test_get_y(self):
        for point in self.points:
            self.assertEqual(point.get_y(), point.y)
    def test_set_x(self):
        for point in self.points:
            point.set_x(2)
            self.assertEqual(point.get_x(), 2)
    def test_set_y(self):
        for point in self.points:
            point.set_y(3)
            self.assertEqual(point.get_y(), 3)
    def test_str(self):
        for point in self.points:
            self.assertEqual(str(point), f"({point.x}, {point.y})")
    def test_repr(self):
        for point in self.points:
            self.assertEqual(repr(point), f"Point({point.x}, {point.y})")
    def test_init(self):
        for point in self.points:
            self.assertEqual(point.x, point.x)
            self.assertEqual(point.y, point.y)
    def test_init_invalid(self):
        with self.assertRaises(ValueError):
            Point(-1, -1)
    def test_init_invalid_x(self):
        with self.assertRaises(ValueError):
            Point(-1, 0)
    def test_init_invalid_y(self):
        with self.assertRaises(ValueError):
            Point(0, -1)
    
    

if __name__ == "__main__":
    unittest.main()

    