from tkinter import *

def addieren():
    # Übernahme der Daten aus den Eigabefeldern mit der Funktin get()
    zahl1 = int(entry_zahl1.get())
    zahl2 = int(entry_zahl2.get())
    # Addiere beide Zahlen
    erg = zahl1 + zahl2
    # erg in label schreiben
    label_result.config(text = str(erg))

def sub(): #meneeeeeeeeeeeeeeeeeeeeeeeeeeee
    # Übernahme der Daten aus den Eigabefeldern mit der Funktin get()
    zahl1 = int(entry_zahl1.get())
    zahl2 = int(entry_zahl2.get())
    # substrahiere beide Zahlen
    erg = zahl1 - zahl2
    # erg in label schreiben
    label_result.config(text = str(erg))   

def div(): #meneeeeeeeeeeeeeeeeeeeeeeeeeeee
    # Übernahme der Daten aus den Eigabefeldern mit der Funktin get()
    zahl1 = int(entry_zahl1.get())
    zahl2 = int(entry_zahl2.get())
    # substrahiere beide Zahlen
    erg = zahl1 / zahl2
    # erg in label schreiben
    label_result.config(text = str(erg))   
def mult(): #meneeeeeeeeeeeeeeeeeeeeeeeeeeee
    # Übernahme der Daten aus den Eigabefeldern mit der Funktin get()
    zahl1 = int(entry_zahl1.get())
    zahl2 = int(entry_zahl2.get())
    # substrahiere beide Zahlen
    erg = zahl1 * zahl2
    # erg in label schreiben
    label_result.config(text = str(erg))   


# Erstelle das Hauptfenster
fenster = Tk()
# Titel festlegen
fenster.title("Rechner")
# Größe des Fensters
fenster.geometry("600x400")
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
# Eingabefelder
entry_zahl1 = Entry(fenster, bg = "yellow")
entry_zahl1.place(x = 80, y = 10)

label_zahl2 = Label(fenster, text = "Zahl2")
label_zahl2.place(x = 10, y = 40)
entry_zahl2 = Entry(fenster, bg = "skyblue")
entry_zahl2.place(x = 80, y = 40)

label_ergebnis = Label(fenster, text = "Ergebnis",bg="green")
label_ergebnis.place(x = 10, y = 80)

label_result = Label(fenster, text = "")
label_result.place(x = 80, y = 80)
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
# Eingabefelder
entry_zahl1 = Entry(fenster, bg = "yellow")
entry_zahl1.place(x = 80, y = 10)

label_zahl2 = Label(fenster, text = "Zahl2")
label_zahl2.place(x = 10, y = 40)
entry_zahl2 = Entry(fenster, bg = "skyblue")
entry_zahl2.place(x = 80, y = 40)

label_ergebnis = Label(fenster, text = "Ergebnis",bg="green")
label_ergebnis.place(x = 10, y = 80)

label_result = Label(fenster, text = "")
label_result.place(x = 80, y = 80)
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
# Eingabefelder
entry_zahl1 = Entry(fenster, bg = "yellow")
entry_zahl1.place(x = 80, y = 10)

label_zahl2 = Label(fenster, text = "Zahl2")
label_zahl2.place(x = 10, y = 40)
entry_zahl2 = Entry(fenster, bg = "skyblue")
entry_zahl2.place(x = 80, y = 40)

label_ergebnis = Label(fenster, text = "Ergebnis",bg="green")
label_ergebnis.place(x = 10, y = 80)

label_result = Label(fenster, text = "")
label_result.place(x = 80, y = 80)
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
label_zahl1 = Label(fenster, text = "Zahl1")
label_zahl1.place(x = 10, y = 10)
# Eingabefelder
entry_zahl1 = Entry(fenster, bg = "yellow")
entry_zahl1.place(x = 80, y = 10)

label_zahl2 = Label(fenster, text = "Zahl2")
label_zahl2.place(x = 10, y = 40)
entry_zahl2 = Entry(fenster, bg = "skyblue")
entry_zahl2.place(x = 80, y = 40)

label_ergebnis = Label(fenster, text = "Ergebnis",bg="green")
label_ergebnis.place(x = 10, y = 80)

label_result = Label(fenster, text = "")
label_result.place(x = 80, y = 80)

# Aktionen, Buttons, um Aktionen auslösen zu können
button_plus = Button(fenster, text = "+", command = addieren)
button_plus.place(x = 230, y = 10, width = 20, height = 20)
button_minus = Button(fenster, text = "-", command = sub)
button_minus.place(x = 250, y = 40, width = 20, height = 20)
button_div = Button(fenster, text = "/", command = div)
button_div.place(x = 230, y = 40, width = 20, height = 20)
button_mult = Button(fenster, text = "*", command = mult)
button_mult.place(x = 250, y = 10, width = 20, height = 20)


fenster.mainloop()


# Übung:
# Implementieren Sie die restlichen drei Button ( button_minus, button_mult und button_div)