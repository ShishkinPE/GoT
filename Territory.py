class cell:
    def __init__(self, place, food, money, castles, sosed, type_cell, x, y,x1,y1):
        self.place=place
        self.food=food
        self.money=money
        self.castles=castles
        self.sosed=sosed
        self.type_cell=type_cell
        self.x=x
        self.y=y
        self.r=40 #radius knopki
        self.army_x=x1
        self.army_y=y1
        
winterfall=cell('winterfall', 1, 1, 2, [], 'earth', 530, 420, 780,300)
winterfall_port=cell('winterfall_port', 0, 0, 0, [], 'port', 360, 280, 360, 280)
rov_keylin=cell('rov_keylin',0,0,1,[],'earth', 600, 850, 577, 923)
belaya_gavan=cell('belaya_gavan',0,0,1,[],'earth',800, 500, 750, 570)
cherniy_zamok=cell('cherniy_zamok',0,1,0,[],'earth',785, 50, 630, 160)
karhold=cell('karhold',0,1,0,[],'earth', 965, 205, 1010, 340)
drozhashee_more=cell('drozhashee_more',0,0,0,[],'whater', 1200, 580,1175,584)
vdoviy_dozor=cell('vdoviy_dozor',1,0,0,[],'earth',950,577,879,624)

winterfall.sosed.append(winterfall_port)
