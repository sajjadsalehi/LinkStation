import Point


class LinkStation:
    """
    A specific link station class with the center point and a radius.
    In addition most bottom, top, right and left coordinates are added for a simpler comparison in the algorithm.
    """
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.left = x-radius
        self.right = x+radius
        self.top = y+radius
        self.bottom = y-radius

    def contains(self, point: Point):
        """
        checks if the asked point is inside the reach of link station or not.
        :param point: a Point
        :return: True, or False
        """
        if pow((point.x - self.x), 2) + pow((point.y - self.y), 2) < pow(self.radius, 2):
            return True
        else:
            return False
