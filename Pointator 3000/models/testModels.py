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
        x = randint(-500, 500)
        y = randint(-500, 500)
        points.append(Point(x, y))
    return points

class TestFileRepo(unittest.TestCase):
    def setUp(self):
        self.repo = FileRepo()
        self.points = randomPoints(1000)
        for point in self.points:
            self.repo.add_point(point)
    def test_add_point(self):
        self.assertEqual(len(self.repo.get_points()), 1000)
    def test_save(self):
        self.repo.save(self.repo.get_points())
        self.assertTrue(True)
    def test_get_points(self):
        self.assertEqual(len(self.repo.get_points()), 1000)
    def test_no_negative_coordinates(self):
        for point in self.points:
            self.assertGreaterEqual(point.x, 0)
            self.assertGreaterEqual(point.y, 0)
    def test_clear_points(self):
        self.repo.clear_points()
        self.assertEqual(len(self.repo.get_points()), 0)
    
    

if __name__ == "__main__":
    unittest.main()

    