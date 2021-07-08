def wap_char():
    str1='abc'
    str2='xyz'
    str3= str2[:2] + str1[2] + ' ' + str1[0:2]+ str2[2]

    print(str3)

wap_char()





str1 = 'ing'
str2 = 'ly'







def lenundlang(x):

    if len(x[0]) > len(x[1]):
        return x[0]
    if len(x[1]) > len(x[2]):
        return x[1]

    if len(x[2]) > len(x[3]):
         return x[2]
    if len(x[3]) > len(x[0]):
         return x[3]
    else:
        print(x)



print(lenundlang(['amin', 'ahmad', 'mohamed', 'wolfgang']))


str = 'amin'
n = 1
def remove_char(str, n):
    first_part = str[:n]
    print(first_part)
    last_part = str[n + 1:]
    print(last_part)
    return first_part + last_part


print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))
#-----------------49. Schreiben Sie ein Python-Programm, um die Vokale eines bestimmten Textes zu zählen und anzuzeigen.----------------------------------------------------------------------'''
vowels=['a','e','i','o','u']
text=input('bitte einen text eingeben')
print(text)
count

string = input('bitte einen text eingeben')
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'
y = 'y'
count  = string.count(a)
count1 = string.count(e)
count2 = string.count(i)
count3 = string.count(o)
count4 = string.count(u)


if a or e or i or o or u or y in string:
    if count or count1 or count2 or count3 or count4 > 0:

            print('es sind ',count+count1+count2+count3+count4, 'Vokalen')

            print("a ist ", count, 'mal aufgetaucht')
            print("e ist ", count1, 'mal aufgetaucht')
            print("i ist ", count2, 'mal aufgetaucht')
            print("o ist ", count3, 'mal aufgetaucht')
            print("u ist ", count4, 'mal aufgetaucht')
            
    else:
        print('es sind keine vokalen zu finden')

print('or')
print(["a:", count, 'e:',count1,',i:',count2,',o:',count3,',u:',count4,',y:',count,'insgesamt sind das',count+count1+count2+count3+count4,'Vokalen'])



def sum_digits_string(str1): #aufgabe 62 w3resources
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit


print(sum_digits_string("123abcd45"))
print(sum_digits_string("123"))



# w3recoursec 93 93. Schreiben Sie ein Python-Programm, um Zahlen aus einem gegebenen String zu extrahieren. Gehe zur Redaktion
# Beispielausgabe:
# Originalsaite: rot 12 schwarz 45 grün
# Extrahieren Sie Zahlen aus der genannten Zeichenfolge: [12, 45]























