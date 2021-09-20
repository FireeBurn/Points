class Point:
    def __init__(self, x, y, z):
        self.x = input()
        self.y = y
        self.z = z


class Triangle(Point):
    def __init__(self, a, b, c ):
        self.a = a
        self.b = b
        self.c = c

    
    def sides(self):
        A = Point(5, 7, 5)
        B = Point(input(), input(), input())
        C = Point(input(), input(), input())

        ab = ((x2-x1) ** 2 + (y2-y1) ** 2) ** (1/2)
        bc = ((x3-x2) ** 2 + (y3-y2) ** 2) ** (1/2)
        ca = ((x1-x3) ** 2 + (y1-y3) ** 2) ** (1/2)
        return ab, bc, ca

