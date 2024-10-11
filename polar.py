#program to calculate coordinates from polar

import math

d = float(input("Enter the distance value:"))  #get distance  from user
a = float(input("Enter the angular value in radians:")) #get angle in radians
x_coord: float = d * math.cos(a)  # x coordinate calculation
y_coord = d * math.sin(a)         # y cooordinate calculation
print(f"coordinates = ({x_coord}, {y_coord})")  #show result
