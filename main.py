from Tree import Tree
from LinkStation import LinkStation
from Point import Point
import json


def quad_tree(tree: Tree, link_station: LinkStation):
    """
    traversing the quadtree to find out if the point in the tree is included in the link station reach or it is
    positioned in a specific area out of the reach.
    :param tree: accepts a quadtree which is ready to traverse
    :param link_station: accepts a link station object with a specific range and sets the link station on the point if
    it is the best Link Station
    """
    if tree is None:
        return
    if link_station.contains(tree.point):
        tree.point.set_link_station(link_station)
        quad_tree(tree.nw, link_station)
        quad_tree(tree.ne, link_station)
        quad_tree(tree.sw, link_station)
        quad_tree(tree.se, link_station)
    else:
        position = ""
        top = link_station.top - tree.point.x
        bottom = link_station.bottom - tree.point.x
        left = link_station.left - tree.point.y
        right = link_station.right - tree.point.y

        if top > 0:
            position += "n"
        elif top <= 0:
            position += "s"
        if bottom >= 0:
            position += "n"
        elif bottom < 0:
            position += "s"
        if left >= 0:
            position += "e"
        elif left < 0:
            position += "w"
        if right > 0:
            position += "e"
        elif right <= 0:
            position += "w"

        if "n" in position and "e" in position:
            quad_tree(tree.ne, link_station)
        if "n" in position and "w" in position:
            quad_tree(tree.nw, link_station)
        if "s" in position and "e" in position:
            quad_tree(tree.se, link_station)
        if "s" in position and "w" in position:
            quad_tree(tree.sw, link_station)


def traverse(tree):
    """
    traversing the tree and print out the nearest link station available.
    """
    if tree is None:
        return
    traverse(tree.sw)
    traverse(tree.nw)
    traverse(tree.ne)
    traverse(tree.se)
    tree.point.print_link_station()


def load_data():
    """
    loading the data from the file and loading the points, and link stations data
    """
    points = []
    link_stations = []
    try:
        with open('data.json') as json_file:
            data = json.load(json_file)
            for point in data.get("points"):
                points.append(Point(point[0], point[1]))
            for link_station in data.get("link_stations"):
                link_stations.append(LinkStation(link_station[0], link_station[1], link_station[2]))

            del point
            del link_station
            del data
            del json_file
    except:
        print("malformed data.json file")
        return None, None

    return points, link_stations


def main():
    points, link_stations = load_data()

    if points is None:
        return

    if len(points) <= 0:
        print("There are no points to search.")
        return
    if len(link_stations) <= 0:
        print("There are no link stations.")
        return
    tree = Tree(points.pop(0))
    for point in points:
        tree.insert(point)
    del point
    for link_station in link_stations:
        quad_tree(tree, link_station)
    del link_station
    traverse(tree)


if __name__ == '__main__':
    main()
