import os
from math import *

class FileRepo:
    def __init__(self):
        self.points = []
        self.path = os.path.join(os.path.dirname(__file__), "../data")

    def add_point(self, point):

        """
        Adds a point to the list of points.
        Args:
            point (Point): The point to add.
        """
        
        self.points.append(point)

    def get_points(self):

        """
        Returns the list of points.
        Returns:
            list: The list of points.
        """

        return self.points

    def clear_points(self):

        """
        Clears the list of points.
        """
        
        self.points = []

    def validFileName(self, fileName) -> str:

        """
        Checks if the file name already exists in the specified path.
        Args:
            fileName (str): The name of the file to check.
        Returns:
            str: A valid file name that does not already exist in the path.
        """

        base, ext = os.path.splitext(fileName)
        counter = 1
        newFileName = fileName

        while os.path.exists(os.path.join(self.path, newFileName)):
            if counter == 1:
                response = input(f"{newFileName} already exists. Do you want to overwrite it? (y/n): ")
            if response.lower() == 'y':
                return newFileName
            else:
                newFileName = f"{base}_{counter}{ext}"
                counter += 1

        return newFileName
    
    def check_disk_space(self, path:str, required_space:int) -> bool:

        """
        Checks if there is enough disk space available at the given path.
        Args:
            path (str): The path to check for disk space.
            required_space (int): The required space in bytes.
        Returns:
            bool: True if there is enough space, False otherwise.
        """

        statvfs = os.statvfs(path)
        available_space = statvfs.f_frsize * statvfs.f_bavail
        return available_space >= required_space

    def save(self, points, fileName="points.txt"):

        """
        Saves the points to a CSV file in a specific format.
        Args:
            points (list): List of Point objects to save.
            fileName (str): The name of the file to save the points to.
        """

        # Estimate required space based on the number of points
        # Assuming each point entry in the file takes approximately 100 bytes
        required_space = len(points) * 100
        if not self.check_disk_space(self.path, required_space):
            raise OSError("Not enough disk space available")
        
        fileName = self.validFileName(fileName)    
        
        with open(f"{self.path}/{fileName}", "w") as f:
            f.write(f"1, 0, {points[0].get_x()}, {points[0].get_y()}, 0, 0\n")
            for i in range(1, len(points)):
                point = points[i]
                numFrame = i
                deltaTime = i - (i-1)           # TODO
                scale = 1                       # TODO
                deltaDist = sqrt((points[i].get_x() - points[i-1].get_x())**2 + (points[i].get_y() - points[i-1].get_y())**2)
                deltaX = sqrt((points[i].get_x() - points[i-1].get_x())**2)
                deltaY = sqrt((points[i].get_y() - points[i-1].get_y())**2)

                if numFrame < 0:
                    raise ValueError("numFrame must be non-negative")
                if deltaTime < 0:
                    raise ValueError("deltaTime must be non-negative")
                if deltaTime > 5000:
                    raise ValueError("deltaTime must be less than 5000ms")
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
