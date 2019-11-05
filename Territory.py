class cell:
    def __init__(self, place, food, money, castles, sosed, type_cell, x, y, army_x, army_y):
        self.place=place
        self.food=food
        self.money=money
        self.castles=castles
        self.sosed=sosed
        self.type_cell=type_cell
        self.x=x
        self.y=y
        self.r=40 #radius knopki
        self.army_x=army_x
        self.army_y=army_y

    def __eq__(self, other):
        return  self is other
        
winterfall=cell('winterfall', 1, 1, 2, [], 'earth', 530, 420, 780,300)
winterfall_port=cell('winterfall_port', 0, 0, 0, [], 'port', 360, 280, 360, 280)
rov_keylin=cell('rov_keylin',0,0,1,[],'earth', 600, 850, 577, 923)
belaya_gavan=cell('belaya_gavan',0,0,1,[],'earth',800, 500, 750, 570)
white_port=cell('belaya_gavan',0,0,0,[],'port',807, 755, 807, 755)
cherniy_zamok=cell('cherniy_zamok',0,1,0,[],'earth',785, 50, 630, 160)
karhold=cell('karhold',0,1,0,[],'earth', 965, 205, 1010, 340)
drozhashee_more=cell('drozhashee_more',0,0,0,[],'whater', 1200, 580,1175,584)
vdoviy_dozor=cell('vdoviy_dozor',1,0,0,[],'earth',950,577,879,624)
uzkoe_more=cell('uzkoe_more',0,0,0,[],'whater',1221,773,1015,761)
ledoviy_zaliv=cell('ledyanoy_zaliv',0,0,0,[],'whater',67,179,98,368)
kamenniy_bereg=cell('kamenniy_bereg',1,0,0,[],'earth',304,511,304,628)
# nexn need add coords
serovodye=cell('serovodye',1,0,0,[],'earth',0,0,0,0)
kremen=cell('kremen',0,0,1,[],'earth',0,0,0,0)
zakatnoe_more=cell('zakatnoe more',0,0,0,[],'whater',0,0,0,0)
zaliv_zheleznyh_ludey=cell('zaliv_zheleznyh_ludey',0,0,0,[],'whater',0,0,0,0)
payk=cell('payk',1,1,2,[],'earth',0,0,0,0)
sigard=cell('sigard',1,1,2,[],'earth',0,0,0,0)
bliznetsy=cell('blizhetsy',0,1,0,[],'earth',0,0,0,0)
pesti=cell('persti',1,0,0,[],'earth',0,0,0,0)
lunnie_gori=cell('lunnie_gori',1,0,0,[],'earth',0,0,0,0)
orlinoe_gnezdo=cell('orlinoe_gnezdo',1,1,1,[],'earth',0,0,0,0)
riveran=cell('riveran',1,1,2,[],'earth',0,0,0,0)
harenhall=cell('harenhall',0,1,1,[],'earth',0,0,0,0)
kleshnya=cell('kleshnya',0,0,1,[],'earth',0,0,0,0)
pidortown=cell('lannisport',2,0,1,[],'earth',0,0,0,0)
kamennaya_septa=cell('kamennaya_septa',0,1,0,[],'earth',0,0,0,0)
chernovodnaya=cell('chernovodnaya',2,0,0,[],'earth',0,0,0,0)
king_gavan=cell('king_gavan',0,2,2,[],'earth',0,0,0,0)
primorskie_marki=cell('primorskie_marki',1,0,0,[],'earth',0,0,0,0)
prostor=cell('prostor',0,0,1,[],'earth',0,0,0,0)
king_les=cell('king_les',1,1,0,[],'earth',0,0,0,0)
storm_predel=cell('storm_predel',0,0,1,[],'earth',0,0,0,0)
higarden=cell('higarden',2,0,2,[],'earth',0,0,0,0)
dorn_marks=cell('dorn_marks',0,1,0,[],'earth',0,0,0,0)
kostanoy_put=cell('kostanoy_put',0,1,0,[],'earth',0,0,0,0)
staromest=cell('staromest',0,0,2,[],'earth',0,0,0,0)
three_bashni=cell('three_bashni',1,0,0,[],'earth',0,0,0,0)
prince_pereval=cell('',1,1,0,[],'earth',0,0,0,0)
ayronvud=cell('',0,0,1,[],'earth',0,0,0,0)
sun_kopyo=cell('',1,1,2,[],'earth',0,0,0,0)
soleniy_bereg=cell('',1,0,0,[],'earth',0,0,0,0)
starfall=cell('',1,0,1,[],'earth',0,0,0,0)
arbor=cell('',0,1,0,[],'earth',0,0,0,0)
dragonstone=cell('',1,1,2,[],'earth',0,0,0,0)
dragonstone_port=cell('',0,0,0,[],'port',0,0,0,0)
sun_port=cell('',0,0,0,[],'port',0,0,0,0)
storm_port=cell('',0,0,0,[],'port',0,0,0,0)
payk_port=cell('',0,0,0,[],'port',0,0,0,0)
pidor_port=cell('',0,0,0,[],'port',0,0,0,0)
staromest_port=cell('',0,0,0,[],'port',0,0,0,0)
gold_proliv=cell('',0,0,0,[],'whater',0,0,0,0)
west_summer_more=cell('',0,0,0,[],'whater',0,0,0,0)
proliv_redvin=cell('',0,0,0,[],'whater',0,0,0,0)
east_summer_more=cell('',0,0,0,[],'whater',0,0,0,0)
dorn_more=cell('',0,0,0,[],'whater',0,0,0,0)
gubitelnie_vali=cell('',0,0,0,[],'whater',0,0,0,0)
chernovod_zaliv=cell('',0,0,0,[],'whater',0,0,0,0)
cherniy_zamok.sosed=[karhold, winterfall,drozhashee_more, ledoviy_zaliv]
winterfall.sosed=[karhold, belaya_gavan ,drozhashee_more, ledoviy_zaliv, winterfall_port, kamenniy_bereg, rov_keylin, cherniy_zamok]
karhold.sosed=[winterfall,cherniy_zamok, drozhashee_more]
kamenniy_bereg.sosed=[winterfall, ledoviy_zaliv]
belaya_gavan.sosed=[winterfall,white_port,vdoviy_dozor,drozhashee_more]

all_territories=[winterfall, rov_keylin, cherniy_zamok,belaya_gavan]
winterfall.sosed.append(winterfall_port)
