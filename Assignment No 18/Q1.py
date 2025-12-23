class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("ComplexNumber object destroyed")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imag - other.imag)

    def __str__(self):
        sign = "+" if self.imag >= 0 else ""
        return f"{self.real}{sign}{self.imag}i"


c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

c3 = c1 + c2
c4 = c1 - c2

print("Complex Number 1:", c1)
print("Complex Number 2:", c2)
print("Addition:", c3)
print("Subtraction:", c4)