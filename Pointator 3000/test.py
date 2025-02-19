from controller.controller import FileRepo
from models.model import Model
from models.point import Point
from random import *

def randomPoints(n:int) -> list:
    """
    Generate a list of n random points.
    """
    points = []
    for _ in range(n):
        x = randint(0, 100)
        y = randint(0, 100)
        points.append(Point(x, y))
    return points

if __name__ == "__main__":
    points = randomPoints(1000)
    model = Model()
    for point in points:
        model.add_point(point)
    repo = FileRepo()
    repo.save(model.get_points())