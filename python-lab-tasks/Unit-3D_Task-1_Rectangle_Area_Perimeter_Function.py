# Unit-3D Task-1: Function returning area and perimeter of a rectangle

def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter          # returned as a tuple


length = 5
breadth = 3

area, perimeter = rectangle_area_perimeter(length, breadth)
print("Area:", area)
print("Perimeter:", perimeter)
