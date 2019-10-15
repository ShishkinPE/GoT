from tkinter import *
from math import *
from random import *
from time import *
from menu import*
from consts import *

game_proc='menu'


def main_click(event):
    global game_proc
    if game_proc=='choise':
        game_process=choise_home_click()
    if game_proc=='menu':
        game_proc=menu_click(event.x, event.y)
        if game_proc=='choise':
            choise_home_draw(canv)
        if game_proc=='load':
            pass
    if game_proc=='help':
        pass
    print(game_proc)


root=Tk()
root.geometry(str(SX())+'x'+str(SY()))
canv = Canvas(root,bg='white')
canv.pack(fill = BOTH, expand = 1)

menu_draw(canv)
canv.bind('<Button-1>', main_click)

print('hello Vesteros')








mainloop()
