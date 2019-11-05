from tkinter import *
from math import *
from random import *
from time import *
from consts import *
from Territory import *

def menu_draw(canv):
    global images, image_menu
    path="media/menu.gif"
    img = PhotoImage(file=path)
    image_menu = Label(canv, image=img)
    images.append(img)
    image_menu.place(x = 0,y = 0)

def menu_house_draw(canv):
    global images, image_house
    path="media/menu-house.gif"
    img = PhotoImage(file=path)
    images.append(img)
    image_house=Label(canv, image=img)
    image_house.place(x = 0,y = 0)

def create_unites():
    pass

def create_track():
    global images, image_track
    path = "media/track.gif"
    img = PhotoImage(file=path)
    images.append(img)
    image_track = Label(root, image=img)

def show_track():
    global image_track
    image_track.place(x=0, y=0)

def close_track():
    global image_track
    image_track.place(x=700, y=-900)

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
    global image_map, images, Pasha, image_menu, image_house
    image_map.place(x=0, y=0)
    image_menu.place(x=-10000, y=0)
    image_house.place(x=-10000, y=0)
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

class command:


    def show(self):
        global image_map, root
        if self.place == 'niht':
            self.id.place(x = 100, y = 100)
        else:
            self.id.place(x = self.place.x, y = self.place.y)

    def give_command(self, event):
        global all_commands, all_territories
        z=0
        if event.widget == self.id:
            for c in all_commands:
                c.clicked = 0
            self.clicked = 1
        for t in all_territories:
            if event.x < t.x + 30 and event.x > t.x - 30  and event.y > t.y - 15 and event.y < t.y + 15 and self.clicked==1:

                for c in all_commands:
                    if c.place == t:
                        tt = self.place
                        c.place = tt
                        self.place = t
                        c.show()
                        z = 1
                if z == 0:
                    self.place = t
                self.show()



class attak(command):

    def __init__(self, power, owner):
        global  image_map
        self.clicked = 0
        self.place = 'niht'
        self.power = power
        self.owner = owner
        self.x = 100
        self.y = 100
        if power == 1:
            self.st = 1
        global h, root
        path1 = "media/test.gif"
        self.img = PhotoImage(file = path1)
        self.id = Label(image_map, image = self.img)
        self.show()




class unit:
    def __init__(self, unit_type, place, owner, place_number):
        self.unit_type=unit_type
        self.place = place
        self.owner = owner
        self.place_number = place_number

        global h, image_map
        path1 = "media/test.gif"
        self.img = PhotoImage(file = path1)
        self.id = Label(image_map, image = self.img)
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

    def __eq__(self, other):
        return self is other

def phase_vesteros():
    pass

def phase_plans():
    global game_proc, all_commands, player_status
    show_commands(player_status)

def phase_doing():
    pass

def create_command():
    global all_houses
    for h in all_houses:
        attak_1=attak(-1, h)
        attak_2=attak(0, h)
        attak_3=attak(1, h)
        all_commands.append(attak_1)
        all_commands.append(attak_2)
        all_commands.append(attak_3)

def battle():
    pass

def motion(event):
    global h, game_proc
    if game_proc != 'menu' and game_proc != 'choise':
        if (event.x < 50)  and (event.y < 50 - h):
            show_track()
        else:
            close_track()

def scroll_up(event):
    map_up()

def scroll_down(event):
    map_down()

def menu_1(x,y):
    global game_proc
    game_proc = menu_click(x, y)
    if game_proc == 'choise':
        menu_house_draw(canv)
    elif game_proc == 'load':
        exit()
    elif game_proc == 'help':
        exit()
    elif game_proc == 'exit':
        exit()

def start_game():
    global game_proc, player_status
    create_unites()
    if game_proc=='barateon':
        barateon.status='player'
        show_map(canv)
        create_track()

        player_status=barateon
        phase_plans()

    if game_proc=='martell':
        martell.status='player'
        show_map(canv)
        create_track()
        player_status=martell
        phase_plans()

    if game_proc=='tirrel':
        tirrel.status='player'
        show_map(canv)
        create_track()
        player_status=tirrel
        phase_plans()

    if game_proc=='lannister':
        #lannisters == pidors
        lannister.status='player'
        show_map(canv)
        create_track()
        player_status=lannister
        phase_plans()

    if game_proc=='greydjoy':
        greydjoy.status='player'
        show_map(canv)
        create_track()
        player_status=greydjoy
        phase_plans()

    if game_proc=='stark':
        stark.status='player'
        show_map(canv)
        create_track()
        player_status=stark
        phase_plans()

def main_click(event):
    global game_proc, h, all_commands
    create_unites()
    for c in all_commands:
        c.give_command(event)
    if game_proc =='menu':
        menu_1(event.x, event.y)

    elif game_proc =='choise':
        game_proc=choise_house_click(event.x, event.y)
        start_game()
    elif game_proc == 'plane_phase':
        pass

def show_commands(player):
    global all_commands
    for c in all_commands:
        if c.owner == player:
            c.show()



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
global images, images_arm, track_status
track_status = 0
images = []

path = "media/map0.gif"
img = PhotoImage(file=path)
images.append(img)
image_map = Label(canv, image=img)

game_proc='menu'
player_status='niht'

h = 0
all_unites=[]
all_commands=[]
all_houses=[stark, greydjoy, lannister, martell, tirrel, barateon]
map_y=0

create_command()

menu_draw(canv)
root.bind('<Button-1>', main_click)
root.bind('<Button-4>', scroll_down)
root.bind('<Button-5>', scroll_up)
image_map.bind('<Motion>', motion)
root.mainloop()
