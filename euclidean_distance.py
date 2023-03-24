#Euclidean Distance formula.
import math
x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))
y1 = int(input("Enter y1:"))
y2 = int(input("Enter y2:"))

# distX = (x2 - x1)**2
# distY = (y2 - y1)**2
# euclid = distX + distY
euclid = (((x2 - x1)**2) + ((y2 - y1)**2))
print("The euclidean distance is:",math.sqrt(euclid))

