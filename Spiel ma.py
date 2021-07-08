# -*- coding: utf-8 -*-

from random import randint

a = randint(1,20)
b = randint(1,20)

print("Additionsaufgabe:")
print(str(a) + " * " + str(b) + " = ")
c = int(input())

if c==a*b:
    print("Richtig! Super!")
else:
    print("Leider falsch. :o(")