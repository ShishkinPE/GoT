from tkinter import *
from math import *
from random import *
from time import *
from consts import *


def show_map(canv):
    path = "media/map0.gif"
    img = PhotoImage(file=path)
    print(help('PhotoImage'))
    print(type(img))
    image_map=Label(canv, image=img)
    image_map.place(x = 0,y = 0)
    

def picture_money():
    pass
