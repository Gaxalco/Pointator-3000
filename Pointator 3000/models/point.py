class Point:

    """
    Class representing a point in 2D space.
    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
    Methods:
        __init__(self, x: int, y: int): Initializes the point with given coordinates.
        __str__(self): Returns a string representation of the point.
        __repr__(self): Returns a string representation of the point for debugging.
        get(self): Returns the coordinates of the point as a tuple.
        set(self, x: int, y: int): Sets the coordinates of the point.
        get_x(self): Returns the x-coordinate of the point.
        get_y(self): Returns the y-coordinate of the point.
        set_x(self, x: int): Sets the x-coordinate of the point.
        set_y(self, y: int): Sets the y-coordinate of the point.
    """

    def __init__(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative")
        """
        To do : add raise if x or y is greater than the video resolution
        """
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

        """
        Returns the y-coordinate of the point.
        Returns:
            int: The y-coordinate of the point.
        """
        
        return self.y
    
    def set_x(self, x):

        """
        Sets the x-coordinate of the point.
        Args:
            x (int): The new x-coordinate of the point.
        Raises:
            ValueError: If the x-coordinate is negative.
            ValueError: If the x-coordinate is greater than the video resolution.
        """

        if x < 0:
            raise ValueError("X coordinate must be non-negative")
        """
        To do : add raise if x is greater than the video resolution
        """
        self.x = x

    def set_y(self, y):

        """
        Sets the y-coordinate of the point.
        Args:
            y (int): The new y-coordinate of the point.
        Raises:
            ValueError: If the y-coordinate is negative.
            ValueError: If the y-coordinate is greater than the video resolution.
        """

        if y < 0:
            raise ValueError("Y coordinate must be non-negative")
        """
        To do : add raise if y is greater than the video resolution
        """
        self.y = y