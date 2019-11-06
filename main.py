from tkinter import *
from math import *
from random import *
from time import *
from consts import *
from Territory import *

class command:
    def close(self):
        if self.place == 'niht':
            self.id.place(x=-100, y=-100)

    def show(self):
        global image_map, root, player_status, h, game_proc
        if self.place == 'niht':
            if player_status == self.owner and game_proc == 'phase_plans':
                self.id.place(x = self.x0, y = self.y0 - h)
            else:
                self.id.place(x=-100, y=-100)
        else:
            self.id.place(x = self.place.x - 20, y = self.place.y - 50)

    def give_command(self, event):
        global all_commands, all_territories
        z=0
        if event.widget == self.id:
            for c in all_commands:
                c.clicked = 0
            self.clicked = 1
        for t in all_territories:
            if t.owner(player_status, all_unites) and event.x < t.x + 30 and event.x > t.x - 30  and event.y > t.y - 15 and event.y < t.y + 15 and self.clicked == 1:
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

    def __init__(self, power, owner, x0, y0):
        global  image_map
        self.type = 'attak'
        self.x0 = x0
        self.y0 = y0
        self.clicked = 0
        self.place = 'niht'
        self.power = power
        self.owner = owner
        self.x = -100
        self.y = 100
        self.st=0
        if power == 1:
            self.st = 1
        global h, root
        if power == -1:
            path1 = "media/commands/attak(-1).gif"
        elif power == 0:
            path1 = "media/commands/attak(0).gif"
        elif power == 1:
            path1 = "media/commands/attak(+1).gif"
        self.img = PhotoImage(file = path1)
        self.id = Label(image_map, image = self.img)
        self.show()

    def doing(self, event):
        pass

class boost(command):
    def doing(self, event):
        pass

    def __init__(self, power, owner, x0, y0):
        global  image_map
        self.type = 'boost'
        self.x0 = x0
        self.y0 = y0
        self.clicked = 0
        self.place = 'niht'
        self.power = power
        self.owner = owner
        self.x = -100
        self.y = 100
        self.st = power
        global h, root
        if power == 0:
            path1 = "media/commands/boost.gif"
        elif power == 1:
            path1 = "media/commands/boost(+1).gif"
        self.img = PhotoImage(file = path1)
        self.id = Label(image_map, image = self.img)
        self.show()

class defense(command):
    def doing(self,event):
        pass
    def __init__(self, power, owner, x0, y0):
        global  image_map
        self.type = 'defense'
        self.x0 = x0
        self.y0 = y0
        self.clicked = 0
        self.place = 'niht'
        self.power = power
        self.owner = owner
        self.x = -100
        self.y = 100
        self.st=0
        if power == 2:
            self.st = 1
        global h, root
        if power == 1:
            path1 = "media/commands/defense.gif"
        elif power == 2:
            path1 = "media/commands/defense(+2).gif"
        self.img = PhotoImage(file = path1)
        self.id = Label(image_map, image = self.img)
        self.show()

class fire(command):

    def __init__(self, power, owner, x0, y0):
        global  image_map
        self.type = 'fire'
        self.x0 = x0
        self.y0 = y0
        self.clicked = 0
        self.place = 'niht'
        self.power = power
        self.owner = owner
        self.x = -100
        self.y = 100
        self.st = power
        global h, root
        if power == 0:
            path1 = "media/commands/fire.gif"
        elif power == 1:
            path1 = "media/commands/fire(+1).gif"
        self.img = PhotoImage(file = path1)
        self.id = Label(image_map, image = self.img)
        self.show()

    def doing(self, event):
        global all_commands, all_territories, all_unites, player_status
        if event.widget == self.id and self.owner == player_status:
            for c in all_commands:
                c.clicked = 0
            self.clicked = 1
        if self.clicked == 1:
            for c in all_commands:
                if event.widget == c.id and c.owner != player_status and (c.type == 'boost' or c.type == 'fire'or (c.type == 'defense' and self.st == 1) or c.type == 'money_command'):
                    self.place = 'niht'
                    c.place = 'niht'
                    c.show()
                    self.show()

class money_command(command):
    def doing(self, event):
        pass

    def __init__(self, power, owner, x0, y0):
        global  image_map
        self.type = 'money_command'
        self.x0 = x0
        self.y0 = y0
        self.clicked = 0
        self.place = 'niht'
        self.power = power
        self.owner = owner
        self.x = -100
        self.y = 100
        self.st = power
        global h, root
        if power == 0:
            path1 = "media/commands/money_command.gif"
        elif power == 1:
            path1 = "media/commands/money_command(+1).gif"
        self.img = PhotoImage(file = path1)
        self.id = Label(image_map, image = self.img)
        self.show()

class unit:
    def __init__(self, unit_type, place, owner, place_number):
        global h, image_map, images, all_unites
        self.unit_type=unit_type
        self.place = place
        self.owner = owner
        self.place_number = place_number

        if self.owner == stark:
            path1 = "media/test.gif"
        if self.owner == greydjoy:
            path1 = "media/test-1.gif"
        self.img = PhotoImage(file = path1)
        images.append(self.img)
        self.id = Label(image_map, image = self.img)

        num_unit = 1
        for u in all_unites:
            if self.place == u.place:
                num_unit += 1
        self.id.place(x = (self.place.army_x - 45 * num_unit // 2) + 45 * self.place_number, y = self.place.army_y)

    def replace(self):
        global h, image_map, images, all_unites
        for u in all_unites:
            if self.place == u.place:
                num_unit += 1
        self.id.place(x=(self.place.army_x - 45 * num_unit // 2) + 45 * self.place_number, y=self.place.army_y)

class house:
    def __init__(self, name, food, castle_num, status, army, territory):
        self.name = name
        self.status = status #'player' or 'comp' возможно дальше ветвление числа денег при инициализации в зависимости от статуса
        self.food = food
        self.castle_num = castle_num
        self.money = 5
        self.army = army

    def __eq__(self, other):
        return self is other

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
    """create start unites u == unit s == stark r == greydjoy"""
    global  all_unites
    us1 = unit('knight', winterfall, stark, 1)
    us2 = unit('footman', winterfall, stark, 2)
    us3 = unit('footman', belaya_gavan, stark,1)
    us4 = unit('ship', drozhashee_more, stark, 1)
    ug1 = unit('test', rov_keylin, greydjoy,1)
    all_unites.append(us1)
    all_unites.append(us2)
    all_unites.append(us3)
    all_unites.append(us4)
    all_unites.append(ug1)

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

def phase_plans():
    global game_proc, all_commands, player_status
    game_proc='phase_plans'
    Finish_button.place(x=SX()*0.45, y=SY()*0.9)

def phase_doing():
    global game_proc
    game_proc='phase_doing'

def create_command():
    global all_houses
    for h in all_houses:
        attak_1=attak(-1, h, SX() - 45, 0)
        attak_2=attak(0, h, SX() - 45, 45)
        attak_3=attak(1, h, SX() - 45, 90)
        boost_1=boost(0, h, SX() - 90, 0)
        boost_2=boost(0, h, SX() - 90, 45)
        boost_3=boost(1, h, SX() - 90, 90)
        defense_1=defense(1, h, SX() - 135, 0)
        defense_2=defense(1, h, SX() - 135, 45)
        defense_3=defense(2, h, SX() - 135, 90)
        fire_1=fire(0, h, SX() - 180, 0)
        fire_2=fire(0, h, SX() - 180, 45)
        fire_3=fire(1, h, SX() - 180, 90)
        money_command_1=money_command(0, h, SX() - 225, 0)
        money_command_2=money_command(0, h, SX() - 225, 45)
        money_command_3=money_command(1, h, SX() - 225, 90)
        all_commands.append(attak_1)
        all_commands.append(attak_2)
        all_commands.append(attak_3)
        all_commands.append(boost_1)
        all_commands.append(boost_2)
        all_commands.append(boost_3)
        all_commands.append(defense_1)
        all_commands.append(defense_2)
        all_commands.append(defense_3)
        all_commands.append(fire_1)
        all_commands.append(fire_2)
        all_commands.append(fire_3)
        all_commands.append(money_command_1)
        all_commands.append(money_command_2)
        all_commands.append(money_command_3)

def motion(event):
    global h, game_proc, all_commands
    if game_proc != 'menu' and game_proc != 'choise':
        if (event.x < 50)  and (event.y < 50 - h):
            show_track()
        else:
            close_track()

    if game_proc == 'phase_plans':
        if (event.x > SX() - 50)  and (event.y < 50 - h):
            for c in all_commands:
                c.show()
        elif (event.x < SX() - 330)  or (event.y > 135 - h):
            for c in all_commands:
                c.close()

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
    global game_proc, h, all_commands, all_unites
    if game_proc =='menu':
        menu_1(event.x, event.y)
    elif game_proc =='choise':
        game_proc=choise_house_click(event.x, event.y)
        start_game()
    elif game_proc == 'phase_plans':
        for c in all_commands:
            c.give_command(event)
    elif game_proc == 'phase_doing':
        for c in all_commands:
            c.doing(event)

def finish_button_click():
    if game_proc=='phase_plans':
        phase_doing()
        print('Хтанол')
        comp_plans()

def comp_plans():
    global all_commands
    for c in all_commands:

        if c.owner == greydjoy and c.type == 'defense' and c.st == 1:
            c.place = rov_keylin
            c.show()
            print('0')



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
image_map.bind('<Button-4>', scroll_down)
image_map.bind('<Button-5>', scroll_up)
image_map.bind('<Motion>', motion)
Finish_button=Button(root, text = 'Дима мокеев петух', command = finish_button_click)
root.mainloop()
