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
                numFrame = i
                deltaTime = i - (i-1)
                scale = 1
                deltaDist = sqrt((points[i].get_x() - points[i-1].get_x())**2 + (points[i].get_y() - points[i-1].get_y())**2)
                deltaX = sqrt((points[i].get_x() - points[i-1].get_x())**2)
                deltaY = sqrt((points[i].get_y() - points[i-1].get_y())**2)

                if numFrame < 0:
                    raise ValueError("numFrame must be non-negative")
                if deltaTime < 0:
                    raise ValueError("deltaTime must be non-negative")
                if scale < 0:
                    raise ValueError("Scale must be non-negative")
                if deltaDist < 0:
                    raise ValueError("deltaDist must be non-negative")
                if deltaX < 0:
                    raise ValueError("deltaX must be non-negative")
                if deltaY < 0:
                    raise ValueError("deltaY must be non-negative")

                f.write(f"{numFrame}, {deltaTime}, {point.get_x()}, {point.get_y()}, {scale}, {deltaDist}, {deltaX}, {deltaY}\n")
        self.clear_points()
        return True
