# main1.py

from graphics.rectangle import area as rect_area, perimeter as rect_peri
from graphics.circle import area as circle_area, perimeter as circle_peri
from graphics.ThreeDgraphics.cuboid import surface_area as cuboid_area
from graphics.ThreeDgraphics.sphere import surface_area as sphere_area

print("Rectangle Area:", rect_area(10, 5))
print("Rectangle Perimeter:", rect_peri(10, 5))

print("Circle Area:", circle_area(7))
print("Circle Perimeter:", circle_peri(7))

print("Cuboid Surface Area:", cuboid_area(4, 5, 6))
print("Sphere Surface Area:", sphere_area(5))
