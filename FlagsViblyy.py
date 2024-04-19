from struct import pack
from tkinter import *
from tkinter import font
from turtle import width # vajalik teksti fondi muutmiseks
import random

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=300, background="white")
tahvel.grid()

#Bahamas lipp
def joonista_bahamas():
    tahvel.delete("all")
    bahamas_ = Toplevel()
    bahamas_.title("Bahamas lipp")
    bahamas__ = Canvas(bahamas_, width=600, height=300, background="white")
    bahamas__.grid()
    bahamas__.create_rectangle(0, 0, 600, 100, fill='#00ABE7')
    bahamas__.create_rectangle(0, 200, 600, 300, fill='#00ABE7')
    bahamas__.create_rectangle(0, 100, 600, 200, fill='#FFC72C')
    bahamas__.create_polygon(0, 0, 0, 300, 300, 150, fill='black')
#Estonia lipp
def joonista_estonia():
    tahvel.delete("all")
    estonia_ = Toplevel()
    estonia_.title("Eesti lipp")
    estonia__ = Canvas(estonia_, width=600, height=300, background="white")
    estonia__.grid()
    estonia__.create_rectangle(0, 0, 600, 100, fill='#0072CE')
    estonia__.create_rectangle(0, 100, 600, 200, fill='black')
    estonia__.create_rectangle(0, 200, 600, 300, fill='white')

#Japan lipp
def joonista_japan():
    tahvel.delete("all")
    japan_ = Toplevel()
    japan_.title("Jaapani lipp")
    japan__ = Canvas(japan_, width=600, height=300, background="white")
    japan__.grid()
    japan__.create_rectangle(0, 0, 600, 300, fill='white')
    japan__.create_oval(250, 75, 350, 175, fill='#BC002D')


def ruut_ja_ring():
    tahvel.delete("all")
    ruut_ja_ring_ = Toplevel()
    ruut_ja_ring_.title("Jaapani lipp")
    ruut_ja_ring__ = Canvas(ruut_ja_ring_, width=600, height=600, background="white")
    ruut_ja_ring__.grid()
    x0=0
    y0=0
    x1=600
    y1=600
    p=0
    x_=600
    y_=600 
    for i in range(20):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        ruut_ja_ring__.create_rectangle(x0,y0,x1,y1, fill="yellow")
        ruut_ja_ring__.create_oval(x0,y0,x1,y1, fill="magenta")
        x_-=2*p
        y_-=2*p
        p=int(((x_**2+y_**2)**(1/2)-x_)/2)
        p=int(((p**2)/2)**(1/2))
def ring():
    ring_ = Toplevel()
    ring_.title("Värvi ring")
    ring__ = Canvas(ring_, width=600, height=600, background="white")
    ring__.grid()
    colors=["black","cyan","magenta","red","blue","gray","yellow","green","lightblue","pink","gold"]
    x0=0
    y0=0
    x1=600
    y1=600
    p=2
    for i in range(150):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        ring__.create_oval(x0,y0,x1,y1, fill=random.choice(colors))
def malelaud():
    tahvel.delete("all")
    malelaud_ = Toplevel()
    malelaud_.title("Malelaud")
    malelaud__ = Canvas(malelaud_, width=800, height=800, background="black")
    malelaud__.grid()
    x=100
    y=100
    x_=0
    y_=0
    for i in range(8):
        for j in range(4):
            malelaud__.create_rectangle(x_, y_, x, y, fill='white')
            x_+=200
            x+=200

        if i%2==0:
            x_=100      
            x=100+x_
            y+=100
            y_+=100
        else:
            x_=0      
            x=100
            y+=100
            y_+=100

#nuppud
bahamas_nupp=Button(raam, text="Bahama saarte lipp", font="Algerian", heigh=3, width=10, relief=RAISED, command=joonista_bahamas, bg="yellow")
eesti_nupp=Button(raam, text="Eesti lipp", font="Algerian", heigh=3, width=10, relief=RAISED, command=joonista_estonia, bg="blue")
japan_nupp=Button(raam, text="Jaapani lipp", font="Algerian", heigh=3, width=10, relief=RAISED, command=joonista_japan, bg="blue")
ruut_ja_ring_nupp=Button(raam, text="Ruut ja ring", font="Algerian", heigh=3, width=10, relief=RAISED, command=ruut_ja_ring, bg="red")
ring_nupp=Button(raam, text="Ring", font="Algerian", heigh=3, width=10, relief=RAISED, command=ring, bg="red")
malelaud_nupp=Button(raam, text="Malelaud", font="Algerian", heigh=3, width=10, relief=RAISED, command=malelaud, bg="pink")

bahamas_nupp.place(x=0,y=260)
eesti_nupp.place(x=100,y=260)
japan_nupp.place(x=200,y=260)
ruut_ja_ring_nupp.place(x=300,y=260)
ring_nupp.place(x=400,y=260)
malelaud_nupp.place(x=500,y=260)
raam.mainloop()

