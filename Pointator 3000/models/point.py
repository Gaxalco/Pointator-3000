class Point:
    def __init__(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative")
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def get(self):
        return self.x, self.y
    def set(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative")
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        if x < 0:
            raise ValueError("X coordinate must be non-negative")
        self.x = x
    def set_y(self, y):
        if y < 0:
            raise ValueError("Y coordinate must be non-negative")
        self.y = y