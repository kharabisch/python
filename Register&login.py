# DAs nächste mal print login and print password error and print user not found als funktionen erstellen und in gui umwandeln

from tkinter import *

import os

def register_user():
    username_info = username.get()
    password_info = password.get()

    file= open(username_info+'.txt', 'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text='reg', fg='green', font=('calibri, 11')).pack()
def Login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username == list_of_files:
        file1=open(username1, 'r')
        verify = file1.read().splitlines()
        if password1 in verify :
            print('Login Success')
        else:
            print('password has not been recognized')
    else:
        print('user not found')
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Register')
    screen1.geometry('300x250')

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text='Bitte geben Sie Ihre Daten ein').pack()
    Label(screen1, text='').pack()
    Label(screen1, text='username *').pack()


    username_entry = Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text='password *').pack()

    password_entry = Entry(screen1,textvariable= password)
    password_entry.pack()
    Label(screen1, text='').pack()
    Button(screen1,text='register',width=10,height=1, command=register_user).pack()





def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title('Login')
    screen2.geometry('300x250')
    Label(screen2, text = ' Biite enter die Daten').pack()
    Label(screen2,text='').pack()

    global username_verify
    global password_verify
    username_verify= StringVar()
    password_verify= StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text='username *').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2,text='').pack()

    Label(screen2, text='password *').pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text='').pack

    Button(screen2, text='Login', width=10, Height=1, command= Login_verify).pack()
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('First 1.0')
    Label(text = 'first 1.0', bg = 'skyblue', width ='300', height ='2').pack()
    Label(text='').pack()
    Button(text = 'login', width ='30', height ='2', command=login).pack()
    Label(text='').pack()
    Button(text = ' register',width ='30', height ='2', command =register).pack()

    screen.mainloop()

main_screen()