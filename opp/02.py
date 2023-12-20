
class Fraction:
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __mul__(self, other):
        numerator = self.numerator * other.numerator 
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator 
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
    # object ko print function k andar pass karne se __str__ call hota hai


    # magic methods
    # __add__ -> +
    # __sub__ -> -
    # __mul__ -> *
    # __truediv__ -> /
    # __floordiv__ -> //
    # __mod__ -> %
    # __pow__ -> **
    # __and__ -> &
    # __or__ -> |
    # __xor__ -> ^
    # __invert__ -> ~


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x+y, 'x+y')
print(x+y, 'x-y')
print(x*y, 'x*y')


