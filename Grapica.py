from tkinter import *
from math import *
from random import *
from time import *
from consts import *

h=0

def show_map(canv):
    global image_map
    path = "media/map0.gif"
    img = PhotoImage(file=path)
    print(help('PhotoImage'))
    print(type(img))
    image_map=Label(canv, image=img)
    image_map.place(x = 0,y = 0)

def map_up():
    global h
    if h > -1742:
        h=h-15
    image_map.place(x=0, y=h)
    
def map_down():
    global h
    if h < 0:
        h=h+15
    image_map.place(x=0, y=h)
    

def picture_money():
    pass
