# Variablen in Python

artikelName = "Adapter" # Zwei Statements in einem: Variablen-Definition und -Initialisierung
geraetName = "Handy"
marke = "Apple"

print("Der Artikel heißt Adapter für ein Video-Anschluß der Marke Sony")
print("Der Artikel heißt Ladegerät für ein Video-Gerät der Marke Pentax")

# print()- anpassen, d. h. mit Platzhaltern versehen
print("Der Artikel heißt {0} für ein {1} der Marke {2}".format(artikelName, geraetName, marke))

marke = "Samsung"
print("Der Artikel heißt {0} für ein {1} der Marke {2}".format(artikelName, geraetName, marke))

geraetName = 'Speichermodul'
# Die Reihenfolge der Variablen entsprechend den Platzhaltern einhalten!
print("Der Artikel heißt {0} für ein {1} der Marke {2}".format(artikelName, geraetName, marke))

# Variable vom Typ integer (ganze Zahl)
alter = 33
print("Die Person ist {} Jahre alt.".format(alter))

preis = 59.10
print("Der Preis beträgt: {0}".format(preis))

volljaehrig = True
print("Ist die Person volljährig?: {0}".format(volljaehrig))
print(f"Ist die Person volljährig?: {volljaehrig}")

gut = True
print("ist mein pc gut:{0}" .format(gut))