# -*- coding: utf-8 -*-
'''temp=[0.0,0.0,0.0,0.0,0.0]
for i in range(0,5):
    temp[i]=float(input(str(i+1)+"te Temperatur:  "))
summe = 0
for i in range(0,5):
    summe+=temp[i]
mittelwert=summe/5.0
print("Mittlere Temperatur: "+ str(mittelwert))
for i in range(0,5):
    print(str(temp[i]), end="")
    if temp[i]>mittelwert:
       print(" über dem Durchschnitt.")
    elif temp[i]<mittelwert:
        print(" unter dem Durchschnitt.")
    else:
        print(" entspricht dem Durchschnitt.")'''

#Write a Python function to find the Max of three numbers.

'''def max1(a,b):
    if a > b:
        return a
    return b
def maxtotal(a,b,c):
    return max1(a,max1(b,c))

print(maxtotal(3,3,3))'''

#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)

'''def add(numbers):
    total =0
    for x in numbers:
        total += x
    return total
print(add((5,6,-2,9,1,5)))
'''

#Write a Python function to multiply all the numbers in a list.

#

'''def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((8, 2, 3, -1, 7)))
'''
#Write a Python program to reverse a string. Go to the editor
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

'''def rev(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(rev(input('bitte string eingeben')))
'''


#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument

'''def faktoriel(x):

    if x==0:
        return 1
    else:
        return x * faktoriel(x-1)
x=int(input("zahl eingeben bitte : "))
print(faktoriel(x))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * faktoriel(n)
n=int(input("fak von zahl : "))
print(factorial(n))'''

#Schreiben Sie eine Python-Funktion, um zu überprüfen, ob eine Zahl in einen bestimmten Bereich fällt.

def frange(n):
    if n in range(0,10):
        print( " %s ist in dem bereich"%str(n))
    else :
        print("Die nummer ist nicht in diesem bereich")
frange(5)
