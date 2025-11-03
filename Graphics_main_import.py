from graphics.circle import area as circle_area, perimeter as circle_perimeter
from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.ThreeDgraphics import *

# Circle
r = float(input("Enter the radius of the circle: "))
print("Circle area:", circle_area(r))
print("Circle perimeter:", circle_perimeter(r))

# Rectangle
l = float(input("\nEnter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
print("Rectangle area:", rect_area(l, b))
print("Rectangle perimeter:", rect_perimeter(l, b))

# Cuboid
l = float(input("\nEnter the length of the cuboid: "))
b = float(input("Enter the breadth of the cuboid: "))
h = float(input("Enter the height of the cuboid: "))
print("Cuboid surface area:", cuboid_surface_area(l, b, h))
print("Cuboid volume:", cuboid_volume(l, b, h))

# Sphere
r = float(input("\nEnter the radius of the sphere: "))
print("Sphere surface area:", sphere_surface_area(r))
print("Sphere volume:", sphere_volume(r))
