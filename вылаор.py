class Points:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Triangle(Points):
    def __init__(self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    def sides(self):
        a = Points()
        b = Points()
        c = Points()
        ab = ((b.x-a.x) ** 2 + (b.y-a.y) ** 2 + (b.z-a.z)) ** (1/2)
        bc = ((c.x-b.x) ** 2 + (c.y-b.y) ** 2 + (c.z-b.z)) ** (1/2)
        ca = ((a.x-c.x) ** 2 + (a.y-c.y) ** 2 + (a.z-c.z)) ** (1/2)
        return ab, bc, ca

    def area(self):
        P = ab + bc + ca

a = Triangle(input(), input(), input())
b = Triangle(input(), input(), input())
c = Triangle(input(), input(), input())
print(a.sides())