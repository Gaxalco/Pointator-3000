from models.filerepo import FileRepo
from models.point import Point
from random import *



if __name__ == "__main__":
    points = randomPoints(1000)
    repo = FileRepo()
    for point in points:
        repo.add_point(point)
    repo.save(repo.get_points())