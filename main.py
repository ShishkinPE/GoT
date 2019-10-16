from tkinter import *
from math import *
from random import *
from time import *
from menu import*
from consts import *
from Territory import*
from Grapica import*
from BaseGame import*

game_proc='menu'

class army:
    def __init__(self, people_num, knight_num, ship_num, mashine_num, place):
        self.people_num = people_num
        self.knight_num = knight_num
        self.ship_num = ship_num
        self.mashine_num = mashine_num
        self.place = place

class house:
    def __init__(self, name, food, castle_num, money, status, army, territory):
        self.name = name
        self.status = status #'player' or 'computer' возможно дальше ветвление числа денег при инициализации в зависимости от статуса
        self.food = food
        self.castle_num = castle_num
        self.money = 5
        self.army = army #это !!массив!! с элементами по количеству отрядов в армиях, нужен для расчёта снабжения


        
def main_click(event):
    global game_proc
    
    if game_proc=='choise':
        game_proc=choise_house_click(event.x, event.y)
        
    if game_proc=='menu':
        game_proc=menu_click(event.x, event.y)
        if game_proc=='choise':
            menu_house_draw(canv)
        if game_proc=='load':
            pass
        
    if game_proc=='help':
        pass

    if game_proc=='barateon':
        game_proc='start_game'
        show_map(canv)
    
    print(game_proc)


root=Tk()
root.geometry(str(SX())+'x'+str(SY()))
canv = Canvas(root,bg='white')
canv.pack(fill = BOTH, expand = 1)

menu_draw(canv)
root.bind('<Button-1>', main_click)

print('hello Vesteros')








mainloop()
