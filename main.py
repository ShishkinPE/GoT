from tkinter import *
from math import *
from random import *
from time import *
from consts import *
from Territory import *

def menu_draw(canv):
    global images
    path="media/menu.gif"
    img = PhotoImage(file=path)
    image_map = Label(canv, image=img)
    images.append(img)
    image_map.place(x = 0,y = 0)

def menu_house_draw(canv):
    global images
    path="media/menu-house.gif"
    img = PhotoImage(file=path)
    images.append(img)
    image_map=Label(canv, image=img)
    image_map.place(x = 0,y = 0)

def menu_click(x, y):
    if x > SX() * butX1 and x < SX() * butX2 and y > SY() * butY1 and y < SY() * butY2:
        print('start')
        return 'choise'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+butShag) and y < SY() * (butY2 + butShag):
        print('загрузить')
        return 'load'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+2*butShag) and y < SY() * (butY2 + 2*butShag):
        print('help')
        return 'help'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+3*butShag) and y < SY() * (butY2 + 3*butShag):
        print('Выход')
        exit()
    else:
        return 'menu'

def choise_house_click(x, y):
    if x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1-butShag) and y < SY() * (butY2-butShag):
        return 'barateon'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1) and y < SY() * (butY2):
        return 'martell'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+butShag) and y < SY() * (butY2 + butShag):
        return 'tirrel'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+2*butShag) and y < SY() * (butY2 + 2*butShag):
        return 'lannister'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+3*butShag) and y < SY() * (butY2 + 3*butShag):
        return 'greydjoy'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+4*butShag) and y < SY() * (butY2 + 4*butShag):
        return 'stark'
    else:
        return 'choise'

def show_map(canv):
    global image_map, images
    path = "media/map0.gif"
    img = PhotoImage(file=path)
    images.append(img)
    print(help('y'))  # наш любимый костыль
    image_map = Label(canv, image=img)
    image_map.place(x=0, y=0)
    Pasha = unit('test', winterfall, stark, 1)

def map_up():
    global h
    if h > -1742:
        h = h - 15
    image_map.place(x=0, y=h)

def map_down():
    global h
    if h < 0:
        h = h + 15
    image_map.place(x=0, y=h)

def picture_money():
    pass

class unit:
    def __init__(self, unit_type, place, owner, place_number):
        self.unit_type=unit_type
        self.place = place
        self.owner = owner
        self.place_number=place_number

        global h, image_map
        path1 = "media/test.gif"
        self.img = PhotoImage(file=path1)
        self.id = Label(image_map, image=self.img)
        self.id.place(x = self.place.army_x, y = self.place.army_y-h)

    def move(self):
        global h, image_map, images
        self.id.place(x = self.place.army_x, y = self.place.army_y-h)

class house:
    def __init__(self, name, food, castle_num, status, army, territory):
        self.name = name
        self.status = status #'player' or 'comp' возможно дальше ветвление числа денег при инициализации в зависимости от статуса
        self.food = food
        self.castle_num = castle_num
        self.money = 5
        self.army = army #это !!массив!! с элементами по количеству отрядов в армиях, нужен для расчёта снабжения

def Phase_Vesteros():
    pass

def Phase_Plans():
    pass

def Phase_doing():
    pass

def battle():
    pass

def scroll_up(event):
    map_up()
    for u in all_unites:
        u.move()

def scroll_down(event):
    map_down()
    for u in all_unites:
        u.move()
        
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
        barateon.status='player'
        show_map(canv)

        player_status=barateon
        Phase_Plans()

    if game_proc=='martell':
        game_proc='start_game'
        martell.status='player'
        show_map(canv)
        player_status=martell
        Phase_Plans()

    if game_proc=='tirrel':
        game_proc='start_game'
        tirrel.status='player'
        show_map(canv)
        player_status=tirrel
        Phase_Plans()

    if game_proc=='lannister':
        #lannisters == pidors
        game_proc='start_game'
        lannister.status='player'
        show_map(canv)
        player_status=lannister
        Phase_Plans()

    if game_proc=='greydjoy':
        game_proc='start_game'
        greydjoy.status='player'
        show_map(canv)
        player_status=greydjoy
        Phase_Plans()

    if game_proc=='stark':
        game_proc='start_game'
        stark.status='player'
        show_map(canv)
        player_status=stark
        Phase_Plans()
    
    print(game_proc)

root=Tk()
root.geometry(str(SX())+'x'+str(SY()))
canv = Canvas(root,bg='white')
canv.pack(fill = BOTH, expand = 1)

barateon = house('barateon', 2, 1, 'comp', [], [])
martell = house('martell', 2, 1, 'comp', [], [])
tirrel = house('tirrel', 2, 1, 'comp', [], [])
lannister = house('lannister', 2, 1, 'comp', [], [])
greydjoy = house('gredjoy', 2, 1, 'comp', [], [])
stark = house('stark', 1, 2, 'comp', [], [])

butX1=0.4
butX2=0.6
butY1=0.3
butY2=0.35
butShag=0.15
global images, images_arm
images = []

game_proc='menu'
player_status='niht'

h = 0
all_unites=[]
map_y=0



menu_draw(canv)

root.bind('<Button-1>', main_click)
root.bind('<Button-4>', scroll_down)
root.bind('<Button-5>', scroll_up)

root.mainloop()
