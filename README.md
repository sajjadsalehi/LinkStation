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