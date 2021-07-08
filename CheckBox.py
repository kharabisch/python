# was sind CheckBoxen in tkinter ( in GUI-Anwendungen)?
# Diese sogenannten Kontrollkästchen sind dafür da, um aus einer Reihe
# von Möglichkeiten eine od einige zu wählen

from tkinter import *

class Checkbar(Frame):
    def __init__(self, parent = None, auswahls = [], side = LEFT, anchor = W):
        Frame.__init__(self, parent)
        self.vars = []
        for auswahl in auswahls:
            var = IntVar()
            chk = Checkbutton(self, text = auswahl, variable = var)
            chk.pack(side = side, expand = YES)
            self.vars.append(var)


root = Tk()
root.geometry('400x200')
sportarten = Checkbar(root, ['Joggen', 'Fussball', 'Schwimmen', 'Radfahren'])
sportarten.pack(side = TOP, fill = X)

# Hier kann dem command-Attribut auch die vordefinierte Methode quit übergeben werden
button_beenden = Button(root, text = 'Beenden', command = root.destroy, width = 100)
button_beenden.pack(side = BOTTOM, padx = 20, pady = 20)

# Einige Checkboxen
'''
# Bei dieser Art der Erzeugung würde die Checkbuttons untereinander stehen
check1 = Checkbutton(root, text = 'Deutsch').pack()
check2 = Checkbutton(root, text = 'Französisch').pack()
check3 = Checkbutton(root, text = 'Englisch').pack()
'''



root.mainloop()