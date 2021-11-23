from Point import Point


class Tree:
    """
    it is a point-quadtree with four children for each node which are north west, north east, south west and south east.
    This tree put the new coming point in relation with the previously inserted points.
    """
    def __init__(self, point: Point):
        self.point = point
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

    def insert(self, point: Point):
        """
        inserts a point into the tree in relation with the previously inserted points
        :param point: the new point to be inserted
        :return: Tree
        """
        node = self
        while True:
            if point.x < node.point.x and point.y < node.point.y:
                if node.sw is None:
                    node.sw = Tree(point)
                    break
                else:
                    node = node.sw
            elif point.x < node.point.x and point.y > node.point.y:
                if node.nw is None:
                    node.nw = Tree(point)
                    break
                else:
                    node = node.nw
            elif point.x > node.point.x and point.y < node.point.y:
                if node.se is None:
                    node.se = Tree(point)
                    break
                else:
                    node = node.se
            else:
                if node.ne is None:
                    node.ne = Tree(point)
                    break
                else:
                    node = node.ne
        return self
