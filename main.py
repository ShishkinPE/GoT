from tkinter import *
from math import *
from random import *
from time import *
from consts import *
from Territory import *

BATTLE_TIME = 1


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
            pst = 1
        for t in all_territories:
            t.update_owner(all_houses, all_unites)
            if (pst > stars or self.st == 0) and t.owner == player_status and event.x < t.x + 30 and event.x > t.x - 30  and event.y > t.y - 15 and event.y < t.y + 15 and self.clicked == 1:
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
        self.comp_target = 'niht'

    def doing(self, event):
        global all_commands, all_territories, all_unites, player_status
        if event.widget == self.id and self.owner == player_status:
            for c in all_commands:
                c.clicked = 0
            for u in all_unites:
                u.target = u.place
                u.clicked = 0
            for u in all_unites:
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
        global all_commands, all_territories, all_unites, player_status, all_houses
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
                    for h in all_houses:
                        if (h.tron - 1) % 6 == player_status.tron % 6:
                            comp_doing_fire(h)

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
    def __eq__(self, other):
        return self is other

    def __init__(self, unit_type, place, owner, place_number):
        global h, image_map, images, all_unites
        self.unit_type=unit_type
        if self.unit_type == 'ship' or self.unit_type == 'footman':
            self.power = 1
        elif self.unit_type == 'knight':
            self.power = 2
        elif self.unit_type == 'trembling':
            self.power = 4
        elif self.unit_type == 'test':
            self.power = 0
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
        self.health = 1

    def can_attak(self,target):
        global all_territories, all_unites
        re = 0
        local_sosed = []
        local_sosed += self.place.sosed
        for i in range(7):
            for t in local_sosed:
                for u in all_unites:
                    if u.unit_type == 'ship' and u.place == t and u.owner == self.owner:
                        for t1 in t.sosed:
                            q = 1
                            for t2 in local_sosed:
                                if t2 == t1:
                                    q = 0
                            if q:
                                local_sosed.append(t1)

        for t in local_sosed:
            if t == target:
                re = 1
        if ((self.unit_type == 'knight' or self.unit_type == 'footman' or self.unit_type == 'trembling') and (target.type_cell == 'port' or target.type_cell == 'water'))\
                or (self.unit_type == 'ship' and  (target.type_cell == 'earth')):
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

    def die(self):
        global all_unites
        for u in all_unites:
            if u == self:
                all_unites.remove(u)
        self.place = walhalla
        self.target = walhalla
        self.show()
        self.show_battle(-10, -10)

class house:
    def __init__(self, name, food, castle_num, status, army, territory, tron, sword, voron):
        self.name = name
        self.status = status #'player' or 'comp'
        self.food = food
        self.castle_num = castle_num
        self.money = 5
        self.army = army
        self.tron = tron
        self.sword = sword
        self.voron = voron

    def __eq__(self, other):
        return self is other

    def check_food(self):
        """returns may be or not situation with current targets of this house. Use unites targets"""
        global all_territories
        food = self.food_array()
        for t in all_territories:
            t.update_owner(all_houses, all_unites)
            if t.owner == self:
                u_num = 0
                for u in all_unites:
                    if u.target == t and u.owner == self:
                        u_num += 1
                r = 0
                # r - indicator of existance element of food equal to u_number or bigger
                if u_num > 1:
                    while r == 0:
                        r = 0
                        for f in food:
                            if u_num == f:
                                r = 1
                        if r == 1:
                            food.remove(u_num)
                        else:
                            u_num += 1
                        if u_num > 7:
                            return False
        return True

    def food_array(self):
        if self.food == 0:
            return [2,2]
        if self.food == 1:
            return [3,2]
        if self.food == 2:
            return [3,2,2]
        if self.food == 3:
            return [3,2,2,2]
        if self.food == 4:
            return [3,3,2,2]
        if self.food == 5:
            return [4,3,2,2]
        if self.food >= 6:
            return [4,3,2,2,2]

class leaders:
    def __init__(self, owner, name, power, swords, towers):
        self.owner = owner
        self.swords = swords
        self.towers = towers
        self.name = name
        self.power = power
        self.clicked = 0
        self.usable = 1
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
        return 'choise'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+butShag) and y < SY() * (butY2 + butShag):
        return 'load'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+2*butShag) and y < SY() * (butY2 + 2*butShag):
        return 'help'
    elif x > SX() * butX1 and x < SX() * butX2 and y > SY() * (butY1+3*butShag) and y < SY() * (butY2 + 3*butShag):
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

def create_unites():
    global all_unites
    """create start unites u == unit s == stark r == greydjoy"""
    us1 = unit('knight', winterfall, stark, 1)
    us2 = unit('footman', winterfall, stark, 2)
    us3 = unit('footman', belaya_gavan, stark,1)
    us4 = unit('ship', drozhashee_more, stark, 1)
    ug1 = unit('knight', payk, greydjoy, 1)
    ug2 = unit('footman', payk, greydjoy, 2)
    ug3 = unit('footman', serovodye, greydjoy, 1)
    ug4 = unit('ship', zaliv_zheleznyh_ludey, greydjoy, 1)
    ug5 = unit('ship', payk_port, greydjoy, 1)
    ub1 = unit('ship', gubitelnie_vali, barateon, 1)
    ub2 = unit('ship', gubitelnie_vali, barateon, 2)
    ub3 = unit('footman', king_les, barateon, 1)
    ub4 = unit('footman', dragonstone, barateon, 1)
    ub5 = unit('knight', dragonstone, barateon, 1)
    um1 = unit('footman', sun_kopyo, martell, 1)
    um2 = unit('knight', sun_kopyo, martell, 1)
    um3 = unit('footman', soleniy_bereg, martell, 1)
    um4 = unit('ship', dorn_more, martell, 1)
    ut1 = unit('footman', higarden, tirrel, 1)
    ut2 = unit('footman', dorn_marks, tirrel, 1)
    ut3 = unit('knight', higarden, tirrel, 1)
    ut4 = unit('ship', proliv_redvin, tirrel, 1)
    ul1 = unit('footman', kamennaya_septa, lannister,1)
    ul2 = unit('footman', pidortown, lannister,1)
    ul3 = unit('ship', gold_proliv, lannister,1)
    ul4 = unit('knight', pidortown, lannister,1)
    ul5 = unit('ship', pidor_port, lannister,1)

    all_unites = [us1, us2, us3, us4, ug1, ug2, ug3, ug4, ug5, ub1, ub2, ub3, ub4, ub5, um1, um2, um3, um4, ut1, ut2, ut3, ut4, ul1, ul2, ul3, ul4, ul5]

    for u in all_unites:
        u.show()

    for t in all_territories:
        t.update_owner(all_houses, all_unites)

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
        attak_1=attak(0, h, SX() - 45, 0)
        attak_2=attak(-1, h, SX() - 45, 45)
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
        all_commands.append(attak_3)
        all_commands.append(attak_1)
        all_commands.append(attak_2)
        all_commands.append(boost_3)
        all_commands.append(boost_1)
        all_commands.append(boost_2)
        all_commands.append(defense_3)
        all_commands.append(defense_1)
        all_commands.append(defense_2)
        all_commands.append(fire_3)
        all_commands.append(fire_1)
        all_commands.append(fire_2)
        all_commands.append(money_command_3)
        all_commands.append(money_command_1)
        all_commands.append(money_command_2)

def create_leaders():
    #sum power = 15
    #sum k + s = 14
    leader=leaders(stark, 'Ruse', 2, 1, 0)
    all_leaders.append(leader)
    leader = leaders(stark, 'Katya', 0, 0, 2)
    all_leaders.append(leader)
    leader = leaders(stark, 'Robb', 3, 3, 0)
    all_leaders.append(leader)
    leader = leaders(stark, 'Bran', 3, 0, 3)
    all_leaders.append(leader)
    leader = leaders(stark, 'Eddard', 4, 2, 0)
    all_leaders.append(leader)
    leader = leaders(stark, 'John', 2, 1, 0)
    all_leaders.append(leader)
    leader = leaders(stark, 'Ser', 1, 0, 2)
    all_leaders.append(leader)
    leader = leaders(stark, 'stark', 0, 0, 0)
    all_leaders.append(leader)
    leader = leaders(lannister, 'lannister', 0, 0, 0)
    all_leaders.append(leader)
    leader = leaders(lannister, 'ser', 3, 3, 0)
    all_leaders.append(leader)
    leader = leaders(lannister, 'kivan', 1, 1, 0)
    all_leaders.append(leader)
    leader = leaders(lannister, 'pes', 2, 0, 2)
    all_leaders.append(leader)
    leader = leaders(lannister, 'djeime', 2, 1, 0)
    all_leaders.append(leader)
    leader = leaders(lannister, 'tirion', 3, 0, 1)
    all_leaders.append(leader)
    leader = leaders(lannister, 'tayvin', 4, 0, 3)
    all_leaders.append(leader)
    leader = leaders(lannister, 'serseya', 0, 3, 0)
    all_leaders.append(leader)
    leader = leaders(martell, 'martell', 0, 0, 0)
    all_leaders.append(leader)
    leader = leaders(martell, 'areo', 3, 1, 1) #FIXME : gif image not balanced need add sword to image
    all_leaders.append(leader)
    leader = leaders(martell, 'arianna', 3, 0, 2)
    all_leaders.append(leader)
    leader = leaders(martell, 'doran', 0, 0, 3)
    all_leaders.append(leader)
    leader = leaders(martell, 'gerold', 2, 1, 0)
    all_leaders.append(leader)
    leader = leaders(martell, 'nimeria', 1, 1, 1)
    all_leaders.append(leader)
    leader = leaders(martell, 'obara', 2, 1, 0)
    all_leaders.append(leader)
    leader = leaders(martell, 'oberin', 4, 2, 1)
    all_leaders.append(leader)
    leader = leaders(barateon, 'barateon', 0, 0, 0)
    all_leaders.append(leader)
    leader = leaders(barateon, 'stannis', 4, 5, 0) #it is not a bug. 5 swords is OK
    all_leaders.append(leader)
    leader = leaders(barateon, 'ser', 3, 2, 1)
    all_leaders.append(leader)
    leader = leaders(barateon, 'renly', 3, 0, 0)
    all_leaders.append(leader)
    leader = leaders(barateon, 'brienna', 2, 1, 1)
    all_leaders.append(leader)
    leader = leaders(barateon, 'melisa', 1, 1, 0)
    all_leaders.append(leader)
    leader = leaders(barateon, 'salador', 1, 1, 1)
    all_leaders.append(leader)
    leader = leaders(barateon, 'pestryak', 1, 0, 1)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'beylon', 4, 3, 0)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'wictorian', 4, 3, 0)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'euron', 4, 3, 0)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'asha', 1, 2, 0)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'dagmer', 1, 2, 0)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'wethead', 1, 0, 1)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'teon', 0, 0, 0)
    all_leaders.append(leader)
    leader = leaders(greydjoy, 'greydjoy', 0, 0, 0)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'tirrel', 0, 0, 0)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'tarly', 4, 0, 2)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'meys', 3, 0, 2)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'ser2', 3, 2, 0)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'ser', 3, 3, 0)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'margery', 1, 0, 1)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'alester', 1, 0, 1)
    all_leaders.append(leader)
    leader = leaders(tirrel, 'koroleva', 0, 2, 1)
    all_leaders.append(leader)
    #check_balance()

def check_balance():
    for h in all_houses:
        power = 0
        s = 0
        for l in all_leaders:
            if l.owner == h:
                power += l.power
                s += l.swords + l.towers
        print(h.name + ' have ' + str(s) + ' swords + towers and ' + str(power) + ' power')

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
    global game_proc, player_status, all_unites, images, money_label
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

    money_label = Label(text = 'Kоличесто жетонов власти в вашем распоряжении: ' + str(player_status.money))
    money_label.place(x=0, y=(SY() - 19))

def phase_plans():
    global game_proc, all_commands, player_status
    for c in all_commands:
        c.place = 'niht'
    game_proc='phase_plans'
    Finish_button.place(x=SX()*0.45, y=SY()*0.9)
    Finish_button.config(text='Приказы отданы.')
    title_label.place(x=SX()*0.4, y= SY()*0.05)
    title_label.config(text='Фаза замыслов', font="Arial 30")
    root.after(2000, delete_title)

def phase_doing():
    global game_proc, all_commands, player_status, all_houses, number_doing
    if game_proc == 'phase_plans':
        number_doing = 18
        title_label.place(x=SX()*0.34, y=SY()*0.05)
        title_label.config(text='Фаза действий: набеги')
        root.after(3000, delete_title)
        game_proc='phase_doing_fire'
        for h in all_houses:
            if h.tron == 1 and h != player_status:
                comp_doing_fire(h)
        Finish_button.config(text='Набеги завершены')
    elif game_proc == 'phase_doing_attak':
        Finish_button.config(text='В поход!')
        title_label.place(x=SX() * 0.34, y=SY() * 0.05)
        title_label.config(text='Фаза действий: походы')
        number_doing = 18
        root.after(3000, delete_title)
        z = 0
        for c in all_commands:
            if c.place != 'niht' and c.type == 'attak' and c.owner == player_status:
                z = 1
        if z == 0:
            game_proc = 'phase_doing_money'
            phase_doing()
        for h in all_houses:
            if h.tron == 1 and h != player_status:
                comp_doing_attak(h)
    elif game_proc == 'phase_doing_money':
        title_label.place(x=SX() * 0.34, y=SY() * 0.05)
        title_label.config(text='Фаза действий: сбор власти')
        root.after(3000, delete_title)
        Finish_button.config(text='Завершить сбор власти')

def phase_vesteros():
    #FIXME here add phases of vesteros
    for c in all_commands:
        c.place = 'niht'
        c.clicked = 0
    for u in all_unites:
        u.health = 1
        u.clicked = 0
    phase_plans()

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
                if z == 1 and l.owner == player_status and l.usable == 1:
                    l.clicked = 1
                    LeaderA.config(image = l.img)
                    z = -1
                if l.owner == player_status and l.clicked == 1 and z == 0 and l.usable == 1:
                    z = 1
                    l.clicked = 0
            for l in all_leaders:
                if z == 1 and l.owner == player_status and l.usable == 1:
                    l.clicked = 1
                    LeaderA.config(image = l.img)
                    z = -1
        if event.widget == LeaderD and player_role == 'defense':
            z = 0
            for l in all_leaders:
                if z == 1 and l.owner == player_status and l.usable == 1:
                    l.clicked = 1
                    LeaderD.config(image=l.img)
                    z = -1
                if l.owner == player_status and l.clicked == 1 and z == 0 and l.usable == 1:
                    z = 1
                    l.clicked = 0
            for l in all_leaders:
                if z == 1 and l.owner == player_status and l.usable == 1:
                    l.clicked = 1
                    LeaderD.config(image=l.img)
                    z = -1

def finish_button_click():
    global game_proc, all_unites, all_houses, all_commands, player_status
    if game_proc == 'phase_plans':
        comp_plans()
        phase_doing()
    elif game_proc == 'phase_doing_fire':
        game_proc='phase_doing_attak'
        for h in all_houses:
            if (h.tron - 1) % 6 == player_status.tron % 6:
                comp_doing_fire(h)
        phase_doing()
    elif game_proc == 'phase_doing_attak':
        z = 0
        # if z = some unit target -> battle on place = target
        # if z = 0 -> simple attack
        # if z = 1 -> uncorrect attack <=> no effect of click
        if not player_status.check_food():
            z = 1
        for u1 in all_unites:
            for u2 in all_unites:
                if u1.target == u2.place and u1.owner != u2.owner:
                    if z == 0 or z == u1.target:
                        z = u1.target
                    else:
                        z = 1
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
        z2 = 0
        for c in all_commands:
            if c.place != 'niht' and c.type == 'attak' and c.owner == player_status:
                z2 = 1
        if z2 == 0:
            game_proc = 'phase_doing_money'
            for h in all_houses:
                if (h.tron - 1) % 6 == player_status.tron % 6:
                    comp_doing_attak(h)
            phase_doing()
        if z == 0:
            for h in all_houses:
                if (h.tron - 1) % 6 == player_status.tron % 6:
                    comp_doing_attak(h)
    elif game_proc == 'battle':
        for l in all_leaders:
            if l.clicked == 1 and l.owner == player_status and l.name != player_status.name:
                game_proc = 'phase_doing_attak'
                end_battle()
    elif game_proc == 'phase_doing_money':
        collect_money()
        game_proc = 'phase_vesteros'
        phase_vesteros()

def comp_plans():
    global all_commands, all_territories, all_houses, all_unites, player_status
    for t in all_territories:
        z_enemy = 0
        for u in all_unites:
            if u.place != 'niht' and u.owner == player_status:
                if u.can_attak(t):
                    z_enemy = z_enemy + 1
        t.under_attak = z_enemy
    for h in all_houses:
        for t in all_territories:
            t.comp_choose_change(all_houses, h, 0)
            t.command_have = 0
        for c in all_commands:
            c.comp_target = 0
        if h != player_status:
            if h.voron == 1 or h.voron == 2:
                stars = 3
            if h.voron == 3:
                stars = 2
            if h.voron == 4:
               stars = 1
            if h.voron > 4:
                stars = 0
            for c in all_commands:
                if c.owner == h and c.type == 'attak':
                    for t in all_territories:
                        allow_put = 0
                        local_units = []
                        for u in all_unites:
                            if u.place == t and u.owner == h and c.place == 'niht' and t.command_have == 0:
                                allow_put = 1
                                local_units.append(u)
                        if t.type_cell == 'earth' and allow_put == 1:
                            for t2 in all_territories:
                                if t2.owner == player_status and local_units[0].can_attak(t2) and allow_put == 1 and t2.castles > 0 and t2.comp_choose_return(all_houses, h) == 0:
                                    if stars > 0 and c.st == 1:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        t2.comp_choose_change(all_houses, h, 1)
                                        stars = stars - 1
                                        c.comp_target = t2
                                        t.command_have = 1
                                    elif c.st == 0:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        t2.comp_choose_change(all_houses, h, 1)
                                        c.comp_target = t2
                                        t.command_have = 1
                    for t in all_territories:
                        allow_put = 0
                        local_units = []
                        for u in all_unites:
                            if u.place == t and u.owner == h and c.place == 'niht' and t.command_have == 0:
                                allow_put = 1
                                local_units.append(u)
                        if t.type_cell == 'earth' and allow_put == 1:
                            for t2 in all_territories:
                                if t2.owner != h and local_units[0].can_attak(t2) and allow_put == 1 and t2.castles > 0 and t2.comp_choose_return(all_houses, h) == 0:
                                    if stars > 0 and c.st == 1:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        t2.comp_choose_change(all_houses, h, 1)
                                        stars = stars - 1
                                        c.comp_target = t2
                                        t.command_have = 1
                                    elif c.st == 0:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        t2.comp_choose_change(all_houses, h, 1)
                                        c.comp_target = t2
                                        t.command_have = 1
                        elif t.type_cell != 'earth' and allow_put == 1:
                            for s in t.sosed:
                                if s.type_cell != 'earth' and allow_put == 1:
                                    z_enemy = 0
                                    z_owner = 0
                                    for u in all_unites:
                                        if u.owner != h and u.place == s:
                                            z_enemy = z_enemy + 1
                                        if u.owner == h and u.place == t:
                                            z_owner = z_owner + 1
                                    if z_enemy < z_owner and z_owner > 1 and allow_put == 1:
                                        if stars > 0 and c.st == 1:
                                            allow_put = 0
                                            c.place = t
                                            c.show()
                                            stars = stars - 1
                                            t.command_have = 1
                                        elif c.st == 0:
                                            allow_put = 0
                                            c.place = t
                                            c.show()
                                            t.command_have = 1
            for c in all_commands:
                if c.owner == h and c.type == 'fire':
                    for t in all_territories:
                        allow_put = 0
                        local_units = []
                        for u in all_unites:
                            if u.place == t and u.owner == h and c.place == 'niht' and t.command_have == 0:
                                allow_put = 1
                                local_units.append(u)
                        if allow_put == 1:
                            for s in t.sosed:
                                z_enemy = 0
                                for u in all_unites:
                                    if u.place == s and u.owner != h:
                                        z_enemy = z_enemy + 1
                                if allow_put == 1 and z_enemy > 0:
                                    if stars > 0 and c.st == 1:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        stars = stars - 1
                                        t.command_have = 1
                                    elif c.st == 0:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        t.command_have = 1
            for c in all_commands:
                if c.owner == h and c.type == 'boost':
                    for t in all_territories:
                        allow_put = 0
                        local_units = []
                        for u in all_unites:
                            if u.place == t and u.owner == h and c.place == 'niht' and t.command_have == 0:
                                allow_put = 1
                                local_units.append(u)
                        if allow_put == 1:
                            for s in t.sosed:
                                if allow_put == 1 and s.under_attak > 0 and s.owner == h:
                                    if stars > 0 and c.st == 1:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        stars = stars - 1
                                        t.command_have = 1
                                    elif c.st == 0:
                                        allow_put = 0
                                        c.place = t
                                        c.show()
                                        t.command_have = 1
            for c in all_commands:
                if c.owner == h and c.type == 'defense':
                    for t in all_territories:
                        allow_put = 0
                        local_units = []
                        for u in all_unites:
                            if u.place == t and u.owner == h and c.place == 'niht' and t.command_have == 0:
                                allow_put = 1
                                local_units.append(u)
                        if allow_put == 1:
                            if allow_put == 1 and t.under_attak > 0:
                                if stars > 0 and c.st == 1:
                                    allow_put = 0
                                    c.place = t
                                    c.show()
                                    stars = stars - 1
                                    t.command_have = 1
                                elif c.st == 0:
                                    allow_put = 0
                                    c.place = t
                                    c.show()
                                    t.command_have = 1
            for c in all_commands:
                if c.owner == h and c.type == 'money_command' and c.st == 1 and stars > 0:
                    for t in all_territories:
                        allow_put = 0
                        local_units = []
                        for u in all_unites:
                            if u.place == t and u.owner == h and c.place == 'niht' and t.command_have == 0:
                                allow_put = 1
                                local_units.append(u)
                        if t.type_cell == 'earth' and allow_put == 1 and t.castles > 0:
                            allow_put = 0
                            c.place = t
                            c.show()
                            stars = stars - 1
                            t.command_have = 1
            for c in all_commands:
                if c.owner == h and c.type == 'money_command':
                    for t in all_territories:
                        allow_put = 0
                        local_units = []
                        for u in all_unites:
                            if u.place == t and u.owner == h and c.place == 'niht' and t.command_have == 0:
                                allow_put = 1
                                local_units.append(u)
                        if t.type_cell == 'earth' and allow_put == 1 and c.st == 0:
                            allow_put = 0
                            c.place = t
                            c.show()
                            t.command_have = 1

def comp_doing_fire(fire_owner):
    global all_commands, player_status, all_houses, number_doing
    number_doing = number_doing - 1
    z = 0
    for c in all_commands:
        if c.owner.name == fire_owner.name and c.type == 'fire' and z == 0 and c.place != 'niht':
            z = 1
            z2 = 0
            for c2 in all_commands:
                if c2.owner != fire_owner and z2 == 0:
                    for s in c.place.sosed:
                        if c2.place != 'niht':
                            if c2.place == s and (c2.type == 'fire' or c2.type == 'boost' or c2.type == 'money_command' or (c2.type == 'defense' and c.st == 1)):
                                c2.place = 'niht'
                                c.place = 'niht'
                                c.show()
                                c2.show()
                                z2 = 1
    for h in all_houses:
        if (h.tron - 1) % 6 == fire_owner.tron % 6 and h != player_status and number_doing > 0:
            comp_doing_fire(h)
        elif game_proc != 'phase_doing_fire' and (h.tron - 1) % 6 == fire_owner.tron % 6 and h == player_status:
            for h2 in all_houses:
                if (h2.tron - 1) % 6 == h.tron % 6 and number_doing > 0:
                    comp_doing_fire(h2)

def comp_doing_attak(attak_owner):
    global number_doing
    number_doing = number_doing -1
    z2 = 1
    for c in all_commands:
        if c.owner == attak_owner and c.place != 'niht' and c.type == 'attak' and z2 == 1 and c.place.type_cell == 'earth':
            z2 = 0
            z = 0
            local_units = []
            for u in all_unites:
                if u.place == c.place and u.owner == attak_owner:
                    local_units.append(u)
                    u.clicked == 0
                    z = 1
            for t in all_territories:
                if t.comp_choose_return(all_houses, attak_owner) == 1 and z == 1:
                    afraid = 0;
                    z_enemy = 0
                    for u in all_unites:
                        if u.place == t and u.owner != attak_owner:
                            afraid = 1
                            enemy = u.owner
                            z_enemy = z_enemy + 1
                    if afraid == 1:
                        if local_units[0].can_attak(t) and c.place != 'niht' and len(local_units) > z_enemy - 1:
                            for u in local_units:
                                u.target = t
                                u.clicked = 1
                                c.clicked = 1
                                sleep(0.5)
                                c.place = 'niht'
                                t.comp_choose_change(all_houses, c.owner, 0)
                                global battle_place
                                battle_place = t
                            if enemy == player_status:
                                global game_proc
                                game_proc = 'battle'
                                battle_graphic()
                            else:
                                end_battle()
                        elif z_enemy - 1 > len(local_units) - 0.5:
                            afraid = 2
                    if afraid != 1:
                        if local_units[0].place == c.place and local_units[0].can_attak(t) and afraid == 0:
                            local_units[0].place = t
                            local_units[0].target = t
                            local_units[0].clicked = 1
                            t.comp_choose_change(all_houses, c.owner, 0)
                            t.update_owner(all_houses, all_unites)
                            c.show()
                        for u in local_units:
                            for t2 in all_territories:
                                if u.can_attak(t2) and u.place == c.place and t2.owner != attak_owner:
                                    is_anybody_at_home = 0
                                    for u2 in all_unites:
                                        if u2.place == t2:
                                            is_anybody_at_home = 1
                                    if is_anybody_at_home == 0:
                                        u.place = t2
                                        u.target = t2
                                        u.show()
                                        t2.update_owner(all_houses, all_unites)
                        for u in local_units:
                            if u.place == c.place and u.can_attak(t) and afraid == 0:
                                u.place = t
                                u.target = t
                                u.clicked = 1
                                t.comp_choose_change(all_houses, c.owner, 0)
                                t.update_owner(all_houses, all_unites)
                                c.show()
                        c.place = 'niht'
                        c.show()
        if c.owner == attak_owner and c.place != 'niht' and c.type == 'attak' and z2 == 1 and c.place.type_cell != 'earth':
            z = 0
            local_units = []
            for u in all_unites:
                if u.place == c.place:
                    local_units.append(u)
                    u.clicked == 0
                    z = z + 1

    for u in all_unites:
        u.clicked = 0
        u.show()
    for h in all_houses:
        if (h.tron - 1) % 6 == attak_owner.tron % 6 and h != player_status and number_doing > 0:
            comp_doing_attak(h)
        elif game_proc != 'phase_doing_attak' and (h.tron - 1) % 6 == attak_owner.tron % 6 and h == player_status:
            for h2 in all_houses:
                if (h2.tron - 1) % 6 == h.tron % 6 and number_doing > 0:
                    comp_doing_attak(h2)

def comp_choose_leader(owner, status, with_who):
    global LeaderD, LeaderA
    l_can_use=[]
    lpower = 0
    for l in all_leaders:
        if l.owner == owner and l.usable == 1:
            l_can_use.append(l)
            if l.power > lpower:
                lpower = l.power
    if with_who == 'with_comp':
        l_use = choice(l_can_use)
    else:
        for l in all_leaders:
            if l.owner == owner and l.power == lpower and l.usable == 1:
                l_use = l
    for l in all_leaders:
        if l == l_use:
            l.clicked = 1
            if status == 'attak':
                LeaderA.config(image = l.img)
            if status == 'defense':
                LeaderD.config(image = l.img)

def delete_title():
    title_label.place(x=-1000, y=0)

def battle_graphic():
    global battle_place, all_leaders, all_unites
    Finish_button.config(text = 'Битва!')
    battle_window.place(x=SX()//10, y=SY()//10)
    for u in all_unites:
        u.show_battle(-1,-1)
        if u.target == battle_place and u.place != battle_place:
            attak_player = u.owner
        if u.place == battle_place:
            defense_player = u.owner
    path_a = 'media/food/' + attak_player.name + '/' + attak_player.name + '.gif'
    path_d = 'media/food/' + defense_player.name + '/' + defense_player.name + '.gif'
    img_a = PhotoImage(file = path_a)
    img_d = PhotoImage(file = path_d)
    images.append(img_a)
    images.append(img_d)
    LeaderA.config(image = img_a)
    LeaderD.config(image = img_d)
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
    attak_swords = 0
    attak_towers = 0
    defence_swords = 0
    defence_towers = 0
    power_attak = 0
    power_defense = 0
    global battle_place, all_leaders, all_unites, all_commands, player_status, game_proc
    for u in all_unites:
        if u.target == battle_place and u.place != battle_place:
            attak_place = u.target
    for u in all_unites:
        if u.target == battle_place and u.place != battle_place and u.unit_type != 'trembling':
            power_attak = power_attak + u.power * u.health
        if u.target == battle_place and u.place != battle_place and u.unit_type == 'trembling' and battle_place.castles > 0:
            power_attak = power_attak + u.power * u.health
        if u.place == battle_place and u.unit_type != 'trembling':
            power_defense = power_defense + u.power * u.health
        if u.target == battle_place and u.place != battle_place:
            attak_player = u.owner
        if u.place == battle_place:
            defense_player = u.owner
    if defense_player != player_status:
        if attak_player == player_status:
            comp_choose_leader(defense_player, 'defense', 'with_player')
        else:
            comp_choose_leader(defense_player, 'defense', 'with_comp')
    if attak_player != player_status:
        if defense_player == player_status:
            comp_choose_leader(attak_player, 'attak', 'with_player')
        else:
            comp_choose_leader(attak_player, 'attak', 'with_comp')
    for c in all_commands:
        if c.clicked == 1 and c.type == 'attak' and c.owner == attak_player:
            power_attak += c.power
        if c.place == battle_place and c.type == 'defence':
            power_defense += c.power
    for t in battle_place.sosed:
        for c in all_commands:
            if c.place == t and c.type == 'boost':
                if c.owner == attak_player:
                    power_attak += c.power
                if c.owner == defense_player:
                    power_defense += c.power
                for u in all_unites:
                    if u.owner == attak_player and u.unit_type != 'trembling':
                        power_attak = power_attak + u.power * u.health
                    if u.owner == attak_player and u.unit_type == 'trembling' and battle_place.castles > 0:
                        power_attak = power_attak + u.power * u.health
                    if u.owner == defense_player and u.unit_type != 'trembling':
                        power_defense = power_defense + u.power * u.health
    for l in all_leaders:
        if l.clicked == 1 and l.owner == attak_player:
            power_attak = power_attak + l.power
            l.usable = 0
            attak_swords = l.swords
            attak_towers = l.towers
        if l.clicked == 1 and l.owner == defense_player:
            power_defense = power_defense + l.power
            l.usable = 0
            defence_swords = l.swords
            defence_towers = l.towers
    power_attak += (6 - attak_player.sword) * 0.1
    power_defense += (6 - defense_player.sword) * 0.1

    #next part of cod to spin leaders ceards
    att_l_unusable = 0
    def_l_unusable = 0
    for l in all_leaders:
        if l.owner == attak_player and l.usable == 0:
            att_l_unusable += 1
        if l.owner == defense_player and l.usable == 0:
            def_l_unusable += 1
    if att_l_unusable >= 6:
        for l in all_leaders:
            if l.owner == attak_player:
                l.usable = 1
    if def_l_unusable >= 6:
        for l in all_leaders:
            if l.owner == defense_player:
                l.usable = 1
    for l in all_leaders:
        l.clicked = 0
        if l.name == player_status.name:
            l.clicked = 1
    if defense_player == player_status or attak_player == player_status:
        root.update()
        root.after(BATTLE_TIME*1000, unshow_battle)
        sleep(BATTLE_TIME)

    for c in all_commands:
        if c.clicked == 1 and (defense_player == player_status or attak_player == player_status):
            c.clicked = 0
            c.place = 'niht'
            c.show()
    z = 0
    for c in all_commands:
        if c.place != 'niht' and c.type == 'attak' and c.owner == player_status:
            z = 1
    if z == 0:
        game_proc = 'phase_doing_money'
        phase_doing()
    if power_attak > power_defense:
        local_all_unites = []
        def_unites = []
        local_all_unites += all_unites
        for u in local_all_unites:
            if u.place == battle_place:
                def_unites.append(u)
        died_u = attak_swords - defence_towers
        if died_u < 0:
            died_u = 0
        for i in range(died_u):
            if def_unites and died_u:
                u = choice(def_unites)
                def_unites.remove(u)
                u.die()
        while def_unites:
            u = def_unites[0]
            t_run = []
            for t in all_territories:
                t.update_owner(all_houses, all_unites)
                if u.can_attak(t) and (t.owner == 0 or t.owner == u.owner) and u.health > 0 and t != battle_place:
                    t_run += [t]
            if t_run != []:
                run_place = choice(t_run)
                u.place = run_place
                u.target = run_place
                u.show()
                u.health = 0
                def_unites.remove(u)
            else:
                def_unites.remove(u)
                u.die()

        for u in all_unites:
            if u.target == battle_place:
                u.place = battle_place
        battle_place.update_owner(all_houses, all_unites)
        for c in all_commands:
            if c.place == battle_place:
                c.place ='niht'
                c.show()
    else: #if defence player win battle
        local_all_unites = []
        att_unites = []
        local_all_unites += all_unites
        for u in local_all_unites:
            if u.target == battle_place and u.place != battle_place:
                att_unites.append(u)
        died_u = defence_swords - attak_towers
        if died_u < 0:
            died_u = 0
        for i in range(died_u):
            if att_unites and died_u:
                u = choice(att_unites)
                att_unites.remove(u)
                u.die()
        for u in all_unites:
            if u.target != u.place:
                u.target = u.place
                u.health = 0
    for u in all_unites:
        u.place = u.target
        u.show()
        u.clicked = 0
    for c in all_commands:
        c.clicked = 0
    if attak_player == player_status or defense_player == player_status:
        for h in all_houses:
            if (h.tron - 1) % 6 == player_status.tron % 6:
                comp_doing_attak(h)

def unshow_battle():
    global  battle_window, LeaderD, LeaderA, Finish_button
    battle_window.place(x = -2000, y = 0)
    LeaderD.place(x = -1000, y = 0)
    LeaderA.place(x = -1000, y = 0)
    Finish_button.config(text = 'В поход!')

def sl5():
    sleep(5)

def collect_money():
    global  money_label
    for c in all_commands:
        if c.place != 'niht':
            if c.type == 'money_command' and c.owner == player_status and c.place.castles > 0:
                collect_army()
            if c.type == 'money_command' and c.owner == player_status and c.place.castles > 0:
                comp_collect_army()
            if c.type == 'money_command' and c.place != 'niht':
                c.owner.money += 1 + c.place.money
        money_label.config(text = 'Kоличесто жетонов власти в вашем распоряжении: ' + str(player_status.money))

def collect_army():
    pass

def comp_collect_army():
    print('типа что-то делает')

def test_button():
    for c in all_commands:
        if c.place == 'niht':
            print(c.type + c.owner.name+ c.place)
        else:
            print(c.type + c.owner.name+ c.place.place)

def update_screen():
    for c in all_commands:
        if c.place != 'niht':
            c.show()
        if c.place == 'niht' and game_proc != 'phase_plans':
            c.close()
    for u in all_unites:
        u.show()
    root.after(2000, update_screen)

root=Tk()
root.geometry(str(SX()) + 'x' + str(SY()))
canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

barateon = house('barateon', 2, 1, 'comp', [], [], 1, 5, 4)
martell = house('martell', 2, 1, 'comp', [], [], 5, 4, 3)
tirrel = house('tirrel', 2, 1, 'comp', [], [], 6, 2, 5)
lannister = house('lannister', 2, 1, 'comp', [], [], 2, 6, 1)
greydjoy = house('greydjoy', 2, 1, 'comp', [], [], 4, 1, 6)
stark = house('stark', 1, 2, 'comp', [], [], 3, 3, 2)

butX1 = 0.4
butX2 = 0.6
butY1 = 0.3
butY2 = 0.35
butShag = 0.15
global images, images_arm, track_status
track_status = 0
images = []

path = "media/map0.gif"
img = PhotoImage(file = path)
images.append(img)
image_map = Label(canv, image = img)

game_proc='menu'
player_status='niht'

h = 0
all_territories = [] + import_cells()
track_images = []
all_unites = []
all_commands = []
all_leaders = []
all_houses = [stark, greydjoy, lannister, martell, tirrel, barateon]
menu_draw(canv)

root.bind('<Button-1>', main_click)
image_map.bind('<Button-4>', map_down)
image_map.bind('<Button-5>', map_up)
image_map.bind('<Motion>', motion)

Finish_button=Button(root, text = 'дима мокеев петух', command = finish_button_click)
Test_button=Button(root, text = 'дима мокеев петух', command = test_button)
Test_button.place(x=200, y=50)
title_label=Label(root, text='дима мокеев петух')
path = "media/test.gif"
img2 = PhotoImage(file=path)
battle_img = PhotoImage(file = "media/battle.gif")
battle_window = Label(root, width = SX() * 8 // 10, heigh = SY() * 8 // 10, image = battle_img)
LeaderD=Label(root)
LeaderA=Label(root)
create_command()
create_leaders()

update_screen()

root.mainloop()
