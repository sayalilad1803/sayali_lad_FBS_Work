class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self.normalize()

    def normalize(self):
        self.m += self.cm // 100
        self.cm = self.cm % 100

        self.km += self.m // 1000
        self.m = self.m % 1000

    def __del__(self):
        print("Distance object destroyed")

    def __add__(self, other):
        return Distance(self.km + other.km,
                        self.m + other.m,
                        self.cm + other.cm)

    def __sub__(self, other):
        km = self.km - other.km
        m = self.m - other.m
        cm = self.cm - other.cm

        if cm < 0:
            cm += 100
            m -= 1
        if m < 0:
            m += 1000
            km -= 1

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"


d1 = Distance(2, 750, 80)
d2 = Distance(1, 500, 50)

d3 = d1 + d2
d4 = d1 - d2

print("Distance 1:", d1)
print("Distance 2:", d2)
print("Addition:", d3)
print("Subtraction:", d4)