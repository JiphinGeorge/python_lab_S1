# Program 10: Lambda Functions for Area Calculations

area_square = lambda s: s * s
area_rectangle = lambda l, w: l * w
area_triangle = lambda b, h: 0.5 * b * h

print("Area of Square:", area_square(4))
print("Area of Rectangle:", area_rectangle(5, 3))
print("Area of Triangle:", area_triangle(6, 4))
