import math
import LinkStation


class Point:
    """
    A specific 2d point which has not only a x and y but also a link station with the reach power.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.power = 0
        self.link = None

    def distance(self, x, y):
        """
        calculated the distance between this point and another point using the other point's x, and y
        :param x: other point's x
        :param y: other point's y
        :return: distance between the points
        """
        return math.sqrt(pow(self.x - x, 2) + pow(self.y - y, 2))

    def set_link_station(self, link_station: LinkStation):
        """
        if the point is in the reach of a link station sets it as the new link station only when the new link station
        has a higher power than the previously set link station.
        :param link_station: the new link station which is in reach with the point.
        """
        power = pow(link_station.radius - self.distance(link_station.x, link_station.y), 2)
        if power > self.power:
            self.power = power
            self.link = link_station

    def print_link_station(self):
        """
        prints out the link station which has the best power for this point
        """
        if self.link is not None:
            print("Best link station for point {},{} is {},{} with power {}".format(self.x, self.y, self.link.x, self.link.y, self.power))
        else:
            print("No link station within reach for point {},{}".format(self.x, self.y))
