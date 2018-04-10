import math

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

# formula is pi x r^2 x h
    def volume(self):
        return self.height * math.pi *  (self.radius)**2

    def surface_area(self):
        top = math.pi * (self.radius**2)
        return 2*(top) + (2* math.pi * self.radius * self.height)

   
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
print(math.pi)

