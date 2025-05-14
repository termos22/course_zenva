from turtle import *
from random import randint

def losowy_kolor():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red / 255.0, green / 255.0, blue / 255.0)

#ekran = turtle.Screen()


# Wywołaj funkcję losowy_kolor() i użyj wyniku jako koloru kropki
kolor = losowy_kolor()
dot(50, kolor) # 50 to rozmiar kropki

done()