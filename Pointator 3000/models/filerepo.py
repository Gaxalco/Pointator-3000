import os
from math import *

class FileRepo:
    def __init__(self):
        self.points = []
        self.path = os.path.join(os.path.dirname(__file__), "../data")

    def add_point(self, point):
        self.points.append(point)

    def get_points(self):
        return self.points

    def clear_points(self):
        self.points = []

    def save(self, points):
        with open(f"{self.path}/points.txt", "w") as f:
            f.write(f"1, 0, {points[0].get_x()}, {points[0].get_y()}, 0, 0\n")
            for i in range(1, len(points)):
                point = points[i]
                f.write(f"{i}, {i-i}, {point.get_x()}, {point.get_y()}, {i-i}, {sqrt((points[i].get_x() - points[i-1].get_x())**2) + (points[i].get_y() - points[i-1].get_y())**2}\n")

    