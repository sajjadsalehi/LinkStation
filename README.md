# LinkStation

This is the repository of solved link station problem.
##Question
Write a program that solves the most suitable (with most power) link station for a device at given point [x,y]. Please make this project as complete as you think it should be to be maintainable in the long term by more than one maintainer. Provide instructions how to run the solution or if applicable how to access a deployed running version. This problem can be solved in 2-dimensional space. Link stations have reach and power. 
A link station’s power can be calculated:
```
power = (reach - device's distance from linkstation)^2
if distance > reach, power = 0
```
Program should output following line:
```
“Best link station for point x,y is x,y with power z”
or
“No link station within reach for point x,y”
```
## Solution
### Brute Forcing
Maybe it’s the easiest approach. we can solve this problem computing the power of each link station for each point. As shown in the picture below for a selected there should be 3 different comparisons to find out the best link station.\
![brute force example](https://github.com/sajjadsalehi/LinkStation/blob/main/pictures/brute-force.JPG?raw=true) \
In this case the average and worst time complexities are equal to O(N*M) where N is the number of points and M is the number of link stations.
### Quadtree
A quadtree is very similar to a binary tree while the major difference is that the quadtree nodes have four children instead of two in binary tree. In this way every node can divide the 2d plane into four different sections of north west, north east, south west and south east. By creating a point quadtree (a specific version of quad tree) for the nodes we are always aware of the position of the nodes in relation to each other (picture below) and searching among them will take only O (log n) in the average case. \
![quadtree example](https://github.com/sajjadsalehi/LinkStation/blob/main/pictures/quadtree.png?raw=true) \
After constructing such quad tree, we are ready to intersect it with the link stations with their reach area. As an example, in the picture below a link station is shown in relation to the points on the quad tree. obviously, the link station is situated in the north east side of the point A, and there is only one passage to get point C which is in reach of link station, while in brute force approach we had to calculate the position of all 6 points in relation to the link station. \
![quadtree with link station combined example](https://github.com/sajjadsalehi/LinkStation/blob/main/pictures/quadtree-linkstation.JPG?raw=true) \
In the worst-case scenario this algorithm will perform with O (N*M) where N is the number of points and M is the number of link stations. However, the worst-case scenario does not easily happen. On the other hand, the average-case scenario will be O (M log N) where N is the number of the points and M is the number of Link stations. 
## Installation

At the moment this project does not use any dependencies. So your normal Python 3 should run it perfectly.

## Usage
### Input data
The first step to get ready to run this project is to prepare the data.
In the data.json file you can input the link stations and points you want.
Here is an example of the data.json file:
```json
{
  "link_stations": [[0, 0, 10],[20, 20, 5],[10, 0, 12]],
  "points": [[0, 0], [100, 100], [15,10], [18, 18]]
}
```
Keep in mind that each link station has three elements of [x, y, reach] while each point has two elements of [x, y].
To tun the code it is enough to run the following command:

```bash
cd path/to/project/directory
python3 main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.