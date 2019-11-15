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
        stars = 0
        for c in all_commands:
            if c.st == 1 and c.place != 'niht':
                stars += 1
        pst = 0
        if player_status.voron == 1 or player_status.voron == 2:
            pst = 3
        if player_status.voron == 3:
            pst = 2
        if player_status.voron == 4:
            pst == 1
        if player_status == lannister:
            exit()
        for t in all_territories:
            if (pst > stars or self.st == 0) and t.owner(player_status, all_unites) and event.x < t.x + 30 and event.x > t.x - 30  and event.y > t.y - 15 and event.y < t.y + 15 and self.clicked == 1:
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

    def show_battle(self, type):
        self.id2.place(x = 20 + type * 96, y = 260)

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
        self.id2 = Label(battle_window, image=self.img)
        self.show()

    def doing(self, event):
        global all_commands, all_territories, all_unites, player_status
        if event.widget == self.id and self.owner == player_status:
            for c in all_commands:
                c.clicked = 0
            for u in all_unites:
                u.clicked = 0
                u.show()
            self.clicked = 1
        if self.clicked == 1:
            for u in all_unites:
                if event.widget == u.id and u.owner == self.owner and u.place == self.place:
                    if u.clicked == 0:
                        u.clicked = 1
                    else:
                        u.clicked = 0
                    u.show()
        for t in all_territories:
            if event.x < t.x + 30 and event.x > t.x - 30  and event.y > t.y - 15 and event.y < t.y + 15:
                for u in all_unites:
                    if u.clicked == 1 and u.can_attak(t):
                        u.target = t
                        u.clicked = 0
                    u.show()

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
        self.id2 = Label(battle_window, image=self.img)
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
        self.id2 = Label(battle_window, image=self.img)
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
        self.id2 = Label(battle_window, image=self.img)
        self.show()

    def doing(self, event):
        global all_commands, all_territories, all_unites, player_status
        if event.widget == self.id and self.owner == player_status:
            for c in all_commands:
                c.clicked = 0
            self.clicked = 1
        if self.clicked == 1:
            for c in all_commands:
                if event.widget == c.id and c.owner != self.owner and (c.type == 'boost' or c.type == 'fire'or (c.type == 'defense' and self.st == 1) or c.type == 'money_command'):
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
        self.id2 = Label(battle_window, image=self.img)
        self.show()

class unit:
    def __init__(self, unit_type, place, owner, place_number):
        global h, image_map, images, all_unites
        self.unit_type=unit_type
        self.place = place
        self.target = place
        self.owner = owner
        self.place_number = place_number
        self.clicked = 0
        path1 = "media/unitы/" + self.owner.name + "-" + self.unit_type + ".gif"
        self.img = PhotoImage(file = path1)
        images.append(self.img)
        self.id = Label(image_map, image = self.img)
        self.id2 = Label(battle_window, image=self.img)

    def can_attak(self,target):
        global all_territories, all_unites
        re = 0
        q=1
        local_sosed = self.place.sosed
        for i in range(7):
            for t in local_sosed:
                for u in all_unites:
                    if u.unit_type == 'ship' and u.place == t:
                        for t1 in t.sosed:
                            local_sosed.append(t1)
        for t in local_sosed:
            if t == target:
                re = 1
            if (self.unit_type == 'knight' or self.unit_type == 'footman' or self.unit_type == 'trembling') and (target.type_cell == 'port' or target.type_cell == 'water'):
                re = 0
        if self.place == target:
            re = 1
        return re

    def show(self):
        global h, image_map, images, all_unites
        i=0
        for u in all_unites:
            if self.target == u.target:
                u.place_number = i
                i += 1
        self.id.place(x=(self.target.army_x - 45 * i // 2) + 45 * self.place_number, y=self.target.army_y - self.clicked * 5)

    def show_battle(self, number, type):
        self.id2.place(x = 20 + type * 96, y = 310 + number * 65)

class house:
    def __init__(self, name, food, castle_num, status, army, territory, tron, sword, voron):
        self.name = name
        self.status = status #'player' or 'comp' возможно дальше ветвление числа денег при инициализации в зависимости от статуса
        self.food = food
        self.castle_num = castle_num
        self.money = 5
        self.army = army
        self.tron = tron
        self.sword = sword
        self.voron = voron

    def __eq__(self, other):
        return self is other

class leaders:
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
        self.clicked = 0
        if self.owner.name == self.name:
            self.clicked = 1
        self.id = Label(root)
        path = 'media/food/' + self.owner.name + '/' + self.name + '.gif'
        self.img=PhotoImage(file = path)
        self.id.config(image = self.img)

def menu_draw(canv):
    global images, image_menu
    path="media/menu.gif"
    img = PhotoImage(file=path)
    image_menu = Label(canv, image=img)
    images.append(img)
    image_menu.place(x = 0,y = 0)

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

def menu_house_draw(canv):
    global images, image_house
    path="media/menu-house.gif"
    img = PhotoImage(file=path)
    images.append(img)
    image_house=Label(canv, image=img)
    image_house.place(x = 0,y = 0)

def map_up(event):
    global h
    if h > -1742:
        h = h - 15
    image_map.place(x=0, y=h)

def map_down(event):
    global h
    if h < 0:
        h = h + 15
    image_map.place(x=0, y=h)

def show_map(canv):
    global image_map, images, image_menu, image_house
    image_map.place(x=0, y=0)
    image_menu.place(x=-10000, y=0)
    image_house.place(x=-10000, y=0)

def show_track():
    global image_track, all_houses, track_images
    image_track.place(x=0, y=0)
    for i in range(6):
        track_images[3*i].place(x=157 + (all_houses[i].tron - 1) * 93, y=45)
        track_images[3*i+1].place(x=157 + (all_houses[i].sword - 1) * 93, y=136)
        track_images[3*i+2].place(x=157 + (all_houses[i].voron - 1) * 93, y=226)

def close_track():
    global image_track, track_images
    image_track.place(x=700, y=-900)
    for i in range(6):
        track_images[3*i-2].place(x=157 + (all_houses[i].tron - 1) * 93, y=-45)
        track_images[3*i-1].place(x=157 + (all_houses[i].sword - 1) * 93, y=-134)
        track_images[3*i].place(x=157 + (all_houses[i].voron - 1) * 93, y=-225)

def create_unites(all_unites):
    """create start unites u == unit s == stark r == greydjoy"""
    us1 = unit('knight', winterfall, stark, 1)
    ustest2 = unit('knight', winterfall, stark, 3)
    us2 = unit('footman', winterfall, stark, 2)
    us3 = unit('footman', belaya_gavan, stark,1)
    us4 = unit('ship', drozhashee_more, stark, 1)
    ustest = unit('ship', uzkoe_more, stark, 1)
    ug1 = unit('test', rov_keylin, greydjoy, 1)
    all_unites.append(us1)
    all_unites.append(ustest)
    all_unites.append(ustest2)
    all_unites.append(us2)
    all_unites.append(us3)
    all_unites.append(us4)
    all_unites.append(ug1)

    for u in all_unites:
        u.show()

def create_track():
    global images, image_track, all_houses, track_images, all_houses
    # 0 0 = 157, 45
    # dh = 90 dx = 95
    path = "media/track-test.gif"
    img = PhotoImage(file = path)
    images.append(img)
    image_track = Label(root, image = img)
    for h in all_houses:
        path = "media/houses/" + h.name + ".gif"
        image = PhotoImage(file = path)
        l1 = Label(root, image = image, width = 38, height = 38)
        l2 = Label(root, image = image, width = 38, height = 38)
        l3 = Label(root, image = image, width = 38, height = 38)
        track_images.append(l1)
        track_images.append(l2)
        track_images.append(l3)
        images.append(image)

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

def start_game():
    global game_proc, player_status, all_unites, images
    create_unites(all_unites)
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
        # DO NOT FIX!!! I need this part of cod
        for i in range(15):
            x = randint(100, SX() - 100)
            y = randint(100, SY() - 100)
            l = Label(text = 'дима мокеев петух')
            l.place(x = x, y =y)
        ########################################
        player_status = lannister
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

def phase_plans():
    global game_proc, all_commands, player_status
    game_proc='phase_plans'
    Finish_button.place(x=SX()*0.45, y=SY()*0.9)
    Finish_button.config(text='Приказы отданы.')
    title_label.place(x=SX()*0.4, y= SY()*0.05)
    title_label.config(text='Фаза замыслов', font="Arial 30")
    root.after(2000, delete_title)

def phase_doing():
    global game_proc
    if game_proc == 'phase_plans':
        title_label.place(x=SX()*0.34, y=SY()*0.05)
        title_label.config(text='Фаза действий: набеги')
        root.after(3000, delete_title)
        game_proc='phase_doing_fire'
        Finish_button.config(text='Набеги завершены')
    if game_proc == 'phase_doing_attak':
        Finish_button.config(text='В поход!')
        title_label.place(x=SX() * 0.34, y=SY() * 0.05)
        title_label.config(text='Фаза действий: походы')
        root.after(3000, delete_title)

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

def main_click(event):
    global game_proc, h, all_commands, all_unites, battle_place
    if game_proc =='menu':
        menu_1(event.x, event.y)
    elif game_proc =='choise':
        game_proc=choise_house_click(event.x, event.y)
        if game_proc != 'choise':
            start_game()
    elif game_proc == 'phase_plans':
        for c in all_commands:
            c.give_command(event)
    elif game_proc == 'phase_doing_fire':
        print('in')
        for c in all_commands:
            if c.type == 'fire':
                c.doing(event)
    elif game_proc == 'phase_doing_attak':
        for c in all_commands:
            if c.type == 'attak':
                c.doing(event)
    elif game_proc == 'battle':
        for u in all_unites:
            if u.owner == player_status and u.target == battle_place and u.place != battle_place:
                player_role = 'attak'
            if u.owner == player_status and u.place == battle_place:
                player_role = 'defense'
        if event.widget == LeaderA and player_role == 'attak':
            z = 0
            for l in all_leaders:
                if z == 1 and l.owner == player_status:
                    l.clicked = 1
                    LeaderA.config(image = l.img)
                    z = -1
                if l.owner == player_status and l.clicked == 1 and z == 0:
                    z = 1
                    l.clicked = 0
            for l in all_leaders:
                if z == 1 and l.owner == player_status:
                    l.clicked = 1
                    LeaderA.config(image = l.img)
                    z = -1
        if event.widget == LeaderD and player_role == 'defense':
            z = 0
            for l in all_leaders:
                if z == 1 and l.owner == player_status:
                    l.clicked = 1
                    LeaderD.config(image=l.img)
                    z = -1
                if l.owner == player_status and l.clicked == 1 and z == 0:
                    z = 1
                    l.clicked = 0
            for l in all_leaders:
                if z == 1 and l.owner == player_status:
                    l.clicked = 1
                    LeaderD.config(image=l.img)
                    z = -1

def finish_button_click():
    global game_proc, all_unites
    if game_proc == 'phase_plans':
        phase_doing()
        comp_plans()
    elif game_proc == 'phase_doing_fire':
        game_proc='phase_doing_attak'
        phase_doing()
    elif game_proc == 'phase_doing_attak':
        z=0
        for u1 in all_unites:
            for u2 in all_unites:
                if u1.target == u2.place and u1.owner != u2.owner:
                    if z==0 or z==u1.target:
                        z=u1.target
                    else:
                        z=1
        if z != 0 and z != 1:
            game_proc='battle'
            global battle_place
            battle_place = z
            battle_graphic()
        if z == 0:
            for u in all_unites:
                u.place = u.target
                u.clicked = 0

            for c in all_commands:
                if c.clicked == 1:
                    c.clicked = 0
                    c.place = 'niht'
                    c.show()
    elif game_proc == 'battle':
        end_battle()
        game_proc == 'phase_doing_attak'

def comp_plans():
    global all_commands
    for c in all_commands:

        if c.owner == greydjoy and c.type == 'defense' and c.st == 1:
            c.place = rov_keylin
            c.show()
            print('0')

def delete_title():
    title_label.place(x=-1000, y=0)

def battle_graphic():
    global battle_place, all_leaders
    Finish_button.config(text = 'Битва!')
    battle_window.place(x=SX()//10, y=SY()//10)
    for u in all_unites:
        if u.target == battle_place and u.place != battle_place:
            attak_player = u.owner
        if u.place == battle_place:
            defense_player = u.owner
    for l in all_leaders:
        if l.owner == player_status and l.clicked == 1:
            LeaderA.config(image = l.img)
    LeaderA.place(x = SX()*0.1, y = SY()*0.1)
    LeaderD.place(x = SX()*0.9-161, y = SY()*0.1)
    number_A=0
    number_D=0
    for u in all_unites:
        if u.place == battle_place:
            u.show_battle(number_D, 10)
            number_D = number_D+1
        if u.target == battle_place and u.place != battle_place:
            u.show_battle(number_A, 0)
            number_A = number_A + 1
    for c in all_commands:
        if c.place == battle_place:
            c.show_battle(10)
        if c.clicked == 1:
            c.show_battle(0)
    def_help = 9
    att_help = 1
    for t in  battle_place.sosed:
        for c in all_commands:
            if c.place == t and c.type == 'boost' and defense_player == c.owner:
                c.show_battle(def_help)
                number_D = 0
                for u in all_unites:
                    if u.place == c.place:
                        u.show_battle(number_D, def_help)
                        number_D += 1
                def_help -= 1
            if c.place == t and c.type == 'boost' and attak_player == c.owner:
                c.show_battle(att_help)
                number_A = 0
                for u in all_unites:
                    if u.place == c.place:
                        u.show_battle(number_A, att_help)
                        number_A += 1
                def_help -= 1
                att_help += 1

def end_battle():
    exit()


def create_leaders():
    leader=leaders(stark, 'Ruse')
    all_leaders.append(leader)
    leader = leaders(stark, 'Katya')
    all_leaders.append(leader)
    leader = leaders(stark, 'Robb')
    all_leaders.append(leader)
    leader = leaders(stark, 'Bran')
    all_leaders.append(leader)
    leader = leaders(stark, 'Eddard')
    all_leaders.append(leader)
    leader = leaders(stark, 'John')
    all_leaders.append(leader)
    leader = leaders(stark, 'Ser')
    all_leaders.append(leader)
    leader = leaders(stark, 'stark')
    all_leaders.append(leader)

root=Tk()
root.geometry(str(SX())+'x'+str(SY()))
canv = Canvas(root,bg='white')
canv.pack(fill = BOTH, expand = 1)

barateon = house('barateon', 2, 1, 'comp', [], [], 1, 5, 4)
martell = house('martell', 2, 1, 'comp', [], [], 5, 4, 3)
tirrel = house('tirrel', 2, 1, 'comp', [], [], 6, 2, 5)
lannister = house('lannister', 2, 1, 'comp', [], [], 2, 6, 1)
greydjoy = house('greydjoy', 2, 1, 'comp', [], [], 4, 1, 6)
stark = house('stark', 1, 2, 'comp', [], [], 3, 3, 2)

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
track_images = []
all_unites = []
all_commands = []
all_leaders=[]
all_houses = [stark, greydjoy, lannister, martell, tirrel, barateon]
menu_draw(canv)

root.bind('<Button-1>', main_click)
image_map.bind('<Button-4>', map_down)
image_map.bind('<Button-5>', map_up)
image_map.bind('<Motion>', motion)

Finish_button=Button(root, text = 'дима мокеев петух', command = finish_button_click)
title_label=Label(root, text='дима мокеев петух')
path = "media/test.gif"
img2 = PhotoImage(file=path)
battle_img = PhotoImage(file = "media/battle.gif")
battle_window = Label(root, width = SX() * 8 // 10, heigh = SY() * 8 // 10, image = battle_img)
LeaderD=Label(root)
LeaderA=Label(root)
create_command()
create_leaders()

root.mainloop()
