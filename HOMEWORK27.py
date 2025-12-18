#Normal Writing Editon
import math
class C:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def display_area(self):
        print(f"The area of the circle with radius {self.radius} is: {self.area():.2f}")
C1 = C(5)
C2 = C(10)
C1.display_area()
C2.display_area()