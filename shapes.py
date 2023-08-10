from shape_base import Shape

class BresenhamCircle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        
        vertices, edges = self._generate_circle_points()
        super().__init__(vertices, edges)
    
    def _generate_circle_points(self):
        x = self.radius
        y = 0

        # Collecting points in this list
        points = [(self.center_x + x, self.center_y + y)]

        # When the radius is zero, only a single point will be printed at center
        if self.radius > 0:
            points.append((self.center_x - x, self.center_y - y))
            points.append((self.center_x + x, self.center_y - y))
            points.append((self.center_x - x, self.center_y + y))
        
        # Initial point on circle at the end of radius
        p = 1 - self.radius
        while x > y:
            y += 1

            # Mid-point is inside or on the perimeter of the circle
            if p <= 0:
                p = p + 2 * y + 1
            else:  # Mid-point is outside the perimeter of the circle
                x -= 1
                p = p + 2 * y - 2 * x + 1

            # All the perimeter points have only integer values
            if x < y:
                break

            points.append((self.center_x + x, self.center_y - y))
            points.append((self.center_x - x, self.center_y - y))
            points.append((self.center_x + x, self.center_y + y))
            points.append((self.center_x - x, self.center_y + y))

            # If the generated point is on the line x=Y then the perimeter points
            # have only one set of symmetric points
            if x != y:
                points.append((self.center_x + y, self.center_y - x))
                points.append((self.center_x - y, self.center_y - x))
                points.append((self.center_x + y, self.center_y + x))
                points.append((self.center_x - y, self.center_y + x))
        
        # To create edges, we'll simply connect each point to the next, and then the last point back to the first
        edges = [(i, i + 1) for i in range(len(points) - 1)] + [(len(points) - 1, 0)]

        return points, edges

class Qa(Shape):
    def __init__(self):
        vertices = [
            (-129.75, 256.125), 
            (154.25, 132.125), 
            (-169.75, -263.875),
            (174.25, -265.875)
        ]

        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0)
        ]
        
        super().__init__(vertices, edges)  # Initialize the base class with these values

class Qb(Shape):
    def __init__(self):
        vertices = [
            (-90, 230),
            (246, 98),
            (200, 0),
            (-46, 96),
            (-100, 0),
            (0, -50),
            (-44, -138),
            (-152, -82),
            (-244, -262),
            (-338, -204)    
        ]

        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 8),
            (8, 9),
            (9, 0)
        ]
        
        super().__init__(vertices, edges)  # Initialize the base class with these values

class Qc(Shape):
    def __init__(self):
        vertices = [
            (-200, 300),
            (202, 264),
            (100, 32),
            (228, -256),
            (-16, -302),
            (-266, -254),
            (-310, 30)
        ]

        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 0)
        ]
        
        super().__init__(vertices, edges)  # Initialize the base class with these values

class Qd(Shape):
    def __init__(self):
        vertices = [
            (-200, 0),
            (100, 300),
            (-62, -200)
        ]

        edges = [
            (0, 1),
            (1, 2),
            (2, 0)
        ]
        
        super().__init__(vertices, edges)  # Initialize the base class with these values

class Qe(Shape):
    def __init__(self):
        vertices = [
            (-100, 200),
            (100, 200),
            (244, 0),
            (100, -200),
            (-100, -200),
            (-248, -2) 
        ]

        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 0)
        ]
        
        super().__init__(vertices, edges)  # Initialize the base class with these values

class Qf(Shape):
    def __init__(self):
        vertices = [
            (-126, 296),
            (134, 296),
            (246, 192),
            (254, 32),
            (170, -136),
            (48, -170),
            (-104, -160),
            (-222, -54),
            (-256, 150),
            (-212, 234)
        ]

        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 8),
            (8, 9),
            (9, 0)
        ]
        
        super().__init__(vertices, edges)  # Initialize the base class with these values
