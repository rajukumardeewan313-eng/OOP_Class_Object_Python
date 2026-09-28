# Two types of the datat types 1.Built-in-dataType 2.User-definedatatype
# 1.Integer 2.Floate 3.Boolean 4.Double 5.String 6.Char 
class Fraction:
    # Parameterized Constructor
    def __init__(self, x, y):
        self.num = x
        self.den = y

    # Second Magic Method
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    # Third Magic Method
    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den) 

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

    def __mul__(self,other):
      new_num=self.num*other.num
      new_den=self.den*other.den
      return '{}/{}'.format(new_num,new_den)

    def __truediv__(self,other):
      new_num=self.num*other.den
      new_den=self.den*other.num
      return '{}/{}'.format(new_num,new_den)


fre1 = Fraction(3, 4)
fre2 = Fraction(1, 2)
print(fre1 + fre2)
print(fre1 - fre2)
print(fre1 * fre2)
print(fre1 / fre2)



