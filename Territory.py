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

    def owner(self, smb, all_unites):
        r = 0
        for u in all_unites:
            if u.place == self and u.owner == smb:
                r = True
        return r
        
winterfall=cell('winterfall', 1, 1, 2, [], 'earth', 530, 420, 780,300)
winterfall_port=cell('winterfall_port', 0, 0, 0, [], 'port', 360, 280, 360, 280)
rov_keylin=cell('rov_keylin',0,0,1,[],'earth', 600, 850, 577, 923)
belaya_gavan=cell('belaya_gavan',0,0,1,[],'earth',800, 500, 750, 570)
white_port=cell('belaya_gavan',0,0,0,[],'port',807, 755, 807, 768)
cherniy_zamok=cell('cherniy_zamok',0,1,0,[],'earth',785, 50, 630, 160)
karhold=cell('karhold',0,1,0,[],'earth', 965, 205, 1010, 340)
drozhashee_more=cell('drozhashee_more',0,0,0,[],'water', 1218, 499, 1175, 584)
vdoviy_dozor=cell('vdoviy_dozor',1,0,0,[],'earth',950,577,879,624)
uzkoe_more=cell('uzkoe_more',0,0,0,[],'water',1221,773,1015,761)
ledoviy_zaliv=cell('ledyanoy_zaliv',0,0,0,[],'water',67,179,127,350)
kamenniy_bereg=cell('kamenniy_bereg',1,0,0,[],'earth',304,511,304,628)
serovodye=cell('serovodye',1,0,0,[],'earth',441,817, 438,855)
kremen=cell('kremen', 0, 0, 1, [], 'earth', 299, 852, 256, 893)
zakatnoe_more=cell('zakatnoe more',0,0,0,[],'water',71,837,101,1590)
zaliv_zheleznyh_ludey=cell('zaliv_zheleznyh_ludey',0,0,0,[],'water',225,973,110,1222)
payk=cell('payk',1,1,2,[],'earth',165,1045,229,1118)
sigard=cell('sigard',1,1,2,[],'earth',440,976,499,1063)
bliznetsy=cell('blizhetsy',0,1,0,[],'earth',661,1017,657,1069)
persti=cell('persti',1,0,0,[],'earth', 900, 957, 865, 1017)
lunnie_gori=cell('lunnie_gori',1,0,0,[],'earth',810,1115, 759, 1172)
orlinoe_gnezdo=cell('orlinoe_gnezdo',1,1,1,[],'earth',990,1229,972,1191)
riveran=cell('riveran',1,1,2,[],'earth',547,1235,600,1177)
harenhall=cell('harenhall',0,1,1,[],'earth',659,1341,715,1385)
kleshnya=cell('kleshnya',0,0,1,[],'earth', 862, 1416, 861, 1375)
pidortown=cell('lannisport',2,0,1,[],'earth', 377, 1282, 360, 1337)
kamennaya_septa=cell('kamennaya_septa',0,1,0,[],'earth', 535, 1390, 500, 1447)
chernovodnaya=cell('chernovodnaya',2,0,0,[],'earth', 579, 1574, 505, 1622)
king_gavan=cell('king_gavan',0,2,2,[],'earth', 830, 1602, 839, 1517)
primorskie_marki=cell('primorskie_marki',1,0,0,[],'earth', 317, 1559, 303, 1633)
prostor=cell('prostor',0,0,1,[],'earth', 635, 1777, 561, 1717)
king_les=cell('king_les',1,1,0,[],'earth', 1001, 1663, 827, 1752)
storm_predel=cell('storm_predel',0,0,1,[],'earth', 941, 1890, 900, 1815)
higarden=cell('higarden',2,0,2,[],'earth', 291, 1739, 361, 1819)
dorn_marks=cell('dorn_marks',0,1,0,[],'earth', 546, 1880, 455, 1910)
kostanoy_put=cell('kostanoy_put',0,1,0,[],'earth', 793, 1904, 695, 1940)
staromest=cell('staromest',0,0,2,[],'earth', 302, 1967, 239, 2016)
three_bashni=cell('three_bashni',1,0,0,[],'earth', 392, 2078, 349, 2137)
prince_pereval=cell('',1,1,0,[],'earth', 559, 1984, 523, 2015)
ayronvud=cell('',0,0,1,[],'earth', 643, 2122, 659, 2134)
sun_kopyo=cell('',1,1,2,[],'earth', 1018, 2108, 1019, 2136)
soleniy_bereg=cell('',1,0,0,[],'earth', 837, 2204, 724, 2191)
starfall=cell('',1,0,1,[],'earth', 513, 2250, 533, 2176)
arbor=cell('',0,1,0,[],'earth', 115, 2269, 116, 2295)
dragonstone=cell('',1,1,2,[],'earth', 1224  , 1338, 1215, 1364)
dragonstone_port=cell('',0,0,0,[],'port', 1231, 1529, 1232, 1539)
sun_port=cell('',0,0,0,[],'port', 1184, 2177, 1184, 2187)
storm_port=cell('', 0, 0, 0, [], 'port', 1039, 1839, 1039, 1849)
payk_port=cell('', 0, 0, 0, [], 'port', 317, 1040, 316, 1072)
pidor_port=cell('',0,0,0,[],'port', 254, 1365, 254 , 1366)
staromest_port=cell('',0,0,0,[],'port', 177, 1963, 177, 1973)
gold_proliv=cell('',0,0,0,[],'water', 94, 1491, 126, 1402)
west_summer_more=cell('',0,0,0,[],'water', 393, 2379, 82, 1699)
proliv_redvin=cell('',0,0,0,[],'water', 146, 2166, 161, 2181)
east_summer_more=cell('',0,0,0,[],'water', 979, 2381, 975, 2291)
dorn_more=cell('',0,0,0,[],'water', 902, 2026, 904, 2041)
gubitelnie_vali=cell('',0,0,0,[],'water', 1217, 1663, 1184, 1678)
chernovod_zaliv=cell('',0,0,0,[],'water', 1003, 1501, 968, 1527)

cherniy_zamok.sosed=[karhold, winterfall,drozhashee_more, ledoviy_zaliv]
winterfall.sosed=[karhold, belaya_gavan ,drozhashee_more, ledoviy_zaliv, winterfall_port, kamenniy_bereg, rov_keylin, cherniy_zamok]
karhold.sosed=[winterfall,cherniy_zamok, drozhashee_more]
kamenniy_bereg.sosed=[winterfall, ledoviy_zaliv]
belaya_gavan.sosed=[winterfall, white_port, vdoviy_dozor,drozhashee_more, rov_keylin]
drozhashee_more.sosed = [winterfall, cherniy_zamok, uzkoe_more, karhold, vdoviy_dozor, belaya_gavan]
rov_keylin.sosed = [winterfall, belaya_gavan, uzkoe_more, serovodye, sigard, bliznetsy]
uzkoe_more.sosed = [belaya_gavan, white_port, rov_keylin, bliznetsy, persti, drozhashee_more, vdoviy_dozor, orlinoe_gnezdo, lunnie_gori, kleshnya, gubitelnie_vali]
white_port.sosed = [belaya_gavan, uzkoe_more]
winterfall_port.sosed = [winterfall, ledoviy_zaliv]
vdoviy_dozor.sosed = [belaya_gavan, drozhashee_more, uzkoe_more]
ledoviy_zaliv.sosed = [cherniy_zamok, winterfall, winterfall_port, kamenniy_bereg, serovodye, kremen, zakatnoe_more]
serovodye.sosed = [rov_keylin, ledoviy_zaliv, kremen, sigard, zaliv_zheleznyh_ludey]
kremen.sosed = [ledoviy_zaliv, zakatnoe_more, zaliv_zheleznyh_ludey, serovodye]
zakatnoe_more.sosed = [zaliv_zheleznyh_ludey, kremen, primorskie_marki, gold_proliv, ledoviy_zaliv, west_summer_more]
zaliv_zheleznyh_ludey.sosed = [payk, kremen, serovodye, zakatnoe_more, gold_proliv, sigard, riveran, payk_port]
payk.sosed = [payk_port, zaliv_zheleznyh_ludey]
payk_port.sosed = [payk, zaliv_zheleznyh_ludey]
sigard.sosed = [zaliv_zheleznyh_ludey, serovodye, rov_keylin, bliznetsy, riveran]
bliznetsy.sosed = [lunnie_gori, persti, uzkoe_more, rov_keylin, sigard]
persti.sosed = [lunnie_gori, bliznetsy, uzkoe_more]
riveran.sosed = [pidortown, gold_proliv, zaliv_zheleznyh_ludey, sigard, harenhall, kamennaya_septa]
all_territories=[winterfall, rov_keylin, cherniy_zamok, belaya_gavan, drozhashee_more, winterfall_port,
                 uzkoe_more, white_port, karhold, vdoviy_dozor, ledoviy_zaliv, kamenniy_bereg, serovodye,
                 kremen, zakatnoe_more, zaliv_zheleznyh_ludey, payk, payk_port, sigard, bliznetsy, persti,
                 riveran]
