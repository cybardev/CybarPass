import random
from tkinter import *
from tkinter.ttk import Combobox

screen = Tk()
screen.title("Password Generator")
screen.geometry("500x400")
screen.configure(background="lightgray")

def gen():
    global sc1
    sc1.set("")
    password=" "
    length=len(c1.get())
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"+lowercase
    mix="0123456789"+uppercase+lowercase+"!@#$%^&*"

    if c1.get()=="Low Strength":
        for i in range(0,length):
            password=password+random.choice(lowercase)
            sc1.set(password)
    elif c1.get()=="Medium Strength":
        for i in range(0,length):
            password=password+random.choice(uppercase)
            sc1.set(password)
    elif c1.get()=="High Strength":
        for i in range(0,length):
            password=password+random.choice(mix)
            sc1.set(password)

sc1=StringVar()
L1 = Label(screen,text="Password Generator", font=("Arial",28),bg="lightgray")
L1.place (x=80,y=10)

L2=Label(screen,text="Password:",font=("Arial",14),bg="lightgray")
L2.place(x=100,y=100)
e1 = Entry(screen,font=("Arial",14),textvariable=sc1)
e1.place(x=210,y=100)

L3=Label(screen,text="Strength:",font=("Arial",14),bg="lightgray")
L3.place(x=113,y=135)
c1=Combobox(screen,font=("Arial",14),width=15)
c1["values"]=("Low Strength","Medium Strength","High Strength")
c1.current(1)
c1.place(x=210,y=135)

bt = Button(screen,text="Generate",font=("Arial",14),bg="white",command=gen)
bt.place(x=200,y=240)
screen.mainloop()