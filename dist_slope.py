class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
# d is sqrt of (x2-x1)^2 + (y2-y1)^2
    def distance(self):
        return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2) **.5

# slope is y2 - y1 / x2 - x1
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return 1.0 * (y2 - y1) / (x2 - x1)
        # return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

c1 = (3,2)
c2 = (8,10)
li = Line(c1, c2)

# li.distance is 9.43398...
# li.slope is 1.6

print(li.distance())
print (li.slope())