import unittest
from filerepo import FileRepo
from point import Point
from random import randint
import os
import tempfile
from unittest.mock import patch
import builtins

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
        self.repo.points = []
        # Overwrite the default data path with a temporary directory for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo.path = self.temp_dir.name

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_and_get_points(self):
        p = Point(10, 20)
        self.repo.add_point(p)
        self.assertEqual(self.repo.get_points(), [p])

    def test_clear_points(self):
        self.repo.add_point(Point(5, 5))
        self.repo.clear_points()
        self.assertEqual(self.repo.get_points(), [])

    def test_validFileName_no_existing_file(self):
        fileName = "test.txt"
        # No file exists in the temporary path; the name should remain unchanged.
        valid_name = self.repo.validFileName(fileName)
        self.assertEqual(valid_name, fileName)

    def test_validFileName_existing_overwrite_yes(self):
        fileName = "test.txt"
        # Create a dummy file so that the file exists.
        with open(os.path.join(self.repo.path, fileName), "w") as f:
            f.write("dummy")
        with patch.object(builtins, "input", return_value="y"):
            valid_name = self.repo.validFileName(fileName)
            self.assertEqual(valid_name, fileName)

    def test_validFileName_existing_overwrite_no(self):
        fileName = "test.txt"
        # Create a dummy file so that the file exists.
        with open(os.path.join(self.repo.path, fileName), "w") as f:
            f.write("dummy")
        with patch.object(builtins, "input", return_value="n"):
            valid_name = self.repo.validFileName(fileName)
            # The new name should be 'test_1.txt'
            self.assertEqual(valid_name, "test_1.txt")

    def test_check_disk_space(self):
        # Define a dummy statvfs result.
        class FakeStatVFS:
            f_frsize = 1
            f_bavail = 10000
        with patch("os.statvfs", return_value=FakeStatVFS()):
            self.assertTrue(self.repo.check_disk_space(self.repo.path, 5000))
            self.assertFalse(self.repo.check_disk_space(self.repo.path, 20000))

    def test_save_file_written_and_clears_points(self):
        # Create two points; the second point will produce a delta distance.
        points = [Point(0, 0), Point(3, 4)]
        self.repo.points = points.copy()
        # Patch validFileName to bypass file name validation issues.
        with patch.object(self.repo, "validFileName", return_value="points.txt"):
            self.repo.save(self.repo.get_points(), "points.txt")
        # Verify the file was created.
        file_path = os.path.join(self.repo.path, "points.txt")
        self.assertTrue(os.path.exists(file_path))
        # Read the file and check its content.
        with open(file_path, "r") as f:
            lines = f.readlines()
        # The first line is formatted as: "1, 0, x, y, 0, 0"
        self.assertIn(f"1, 0, {points[0].get_x()}, {points[0].get_y()}, 0, 0", lines[0])
        # There should be a line for the second point.
        self.assertGreater(len(lines), 1)
        # Points should be cleared after saving.
        self.assertEqual(self.repo.get_points(), [])

    def test_save_disk_space_error(self):
        points = randomPoints(10)
        self.repo.points = points.copy()
        # Force check_disk_space to return False, triggering an OSError.
        with patch.object(self.repo, "check_disk_space", return_value=False):
            with self.assertRaises(OSError):
                self.repo.save(points, "points.txt")
        # Ensure that points are not cleared if saving fails.
        self.assertEqual(self.repo.get_points(), points)

    
    

if __name__ == "__main__":
    unittest.main()

    