from tkinter import *
from math import *
from random import *
from time import *
from consts import *

butX1=0.4
butX2=0.6
butY1=0.3
butY2=0.35
butShag=0.15


def menu_draw(canv):
    canv.create_rectangle(0, 0, SX(), SY(), fill='green') # Фон меню
    canv.create_rectangle(0.4*SX(), 0.3*SY(), 0.6*SX(), 0.35*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.45*SY(), 0.6*SX(), 0.5*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.6*SY(), 0.6*SX(), 0.65*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.75*SY(), 0.6*SX(), 0.8*SY(), fill='blue')

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
    
def choise_house_draw(canv):
    canv.create_rectangle(0, 0, SX(), SY(), fill='green') # Фон меню
    canv.create_rectangle(0.4*SX(), 0.3*SY(), 0.6*SX(), 0.35*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.45*SY(), 0.6*SX(), 0.5*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.6*SY(), 0.6*SX(), 0.65*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.75*SY(), 0.6*SX(), 0.8*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.85*SY(), 0.6*SX(), 0.9*SY(), fill='blue')
    canv.create_rectangle(0.4*SX(), 0.95*SY(), 0.6*SX(), 1.0*SY(), fill='blue')

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
