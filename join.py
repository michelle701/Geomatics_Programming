#code to compute a join
import math
x1 = float(input("enter X1 coordinate:"))  # get the x1 coordinate
y1 = float(input("enter Y1 coordinate:"))  # get the y1 coordinate
x2 = float(input("enter X2 coordinate:"))   #get the x2 coordinate
y2 = float(input("enter Y2 coordinate:"))   # get the y2 coordinate
dx = x2 - x1                                 #calculate  dx
dy = y2 - y1                                #calculate dy
a = math.degrees(math.atan(dy/dx))            # calculate the angle
if 0 < a < 90:          # angle adjustments by quadrants, first quadrant condition
    a
elif 90< a <180:        #second quadrant condition
     a = 180 - a
elif -180< a <-90:    #third quadrant condition
    a = a - 180
elif  -90< a <0:                     #fourth quadrant condition
    a = 360 - a
total = dx**2 + dy**2
d = math.sqrt(total)  # calculate distance

print(f"{d}meters, {a}degrees")  # show the result
