from turtle import *

def move_and_turn(angle):
    forward(50)
    right(angle)

ile_katow = int(input("Podaj liczbę kątów: "))

for i in range(ile_katow):
    move_and_turn(360 / ile_katow)

done()