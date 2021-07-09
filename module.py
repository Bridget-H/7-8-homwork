import math

def area(length, width):
   calc_area = (length * width)
   print(f'your home is {calc_area} square feet')
print(area(5, 3))


def circle(r):
    circ = (math.pi*r*2)
    return circ
circle(4)
