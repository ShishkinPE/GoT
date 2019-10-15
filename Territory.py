class cell:
    def __init__(self, place, food, money, castles, sosed, type_cell, x, y):
        self.place=place
        self.food=food
        self.money=money
        self.castles=castles
        self.sosed=sosed
        self.type_cell=type_cell
        self.x=x
        self.y=y
        self.r='?'
        
winterfall=cell('winterfall', 1, 1, 2, [], 'earth', 0, 0)
winterfall_port=cell('winterfall_port', 0, 0, 0, [], 'port', 0, 0)

winterfall.sosed.append(winterfall_port)
