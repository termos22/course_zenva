from turtle import *

diameter = 40 # definiuje wielkość początkowego balonu
pop_diameter = 100 # definiuje maksymalną wielkość balonu po osiągnięciu której następuje wybuch 

def draw_balloon(): # definicja funkcji rysowania poczatkowego balonu
    color("red")
    # begin_fill()
    # circle(diameter)
    # end_fill()
    dot(diameter) # zamiast circle, rysuje wypełniony kolorem okrąg o zadanej wielkości

def inflate_balloon(): # definicja funkcji powiększania balonu
    global diameter # definiuje zmienną jako globalną żeby funkcjie jej używające mogły ją zapisywać
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter: # porównuje wielkość balonu z zadaną wartością graniczną
        clear() # czyści ekran
        diameter = 40 # przywraca początkową wartość wielkości balonu
        write("POP!") # wyświetla napis na ekranie 

def deflate_balloon():
    global diameter
    diameter = diameter - 10
    clear()
    draw_balloon()


draw_balloon() # rysuje początkowy balon na ekranie

onkey(inflate_balloon, "Up") # czyta wejścia i uruchamia funkcję, w tym przypadku powiększa balon za pomocą klawisza strzałki w górę
onkey(deflate_balloon, "Down") # czyta wejścia i uruchamia funkcję, w tym przypadku pomniejsza balon za pomocą klawisza strzałki w dół
listen() # utrzymuje program w trybie odczytywania wejść

done()
