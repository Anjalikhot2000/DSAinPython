# Numbers comes in two flavours
# int (Integers) and float (fractional numbers)
i=5
print(i,type(i))
j=5.2
print(j,type(j))


# Basic Operations in Python +,-,*, /
a=10
b=20
print(a+b) #30
print(a-b) #-10
print(a*b) #200
print(a/b) #0.5


# Quotient and remainder: // and %
print(a//b) #0
print(a%b) #10

# Exponentation: **
a=2
b=3
print(a**b) #8

#log(),sqrt(), sin(),cos(), etc are available in python but not by default, need to include math library
from math import *
print(log(a))  #0.6931471805599453
print(sqrt(b))  #1.7320508075688772

