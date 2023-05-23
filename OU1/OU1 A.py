# OU1 A
# Rita 10 stjärnor och franska flaggan i mitten
import turtle
import random


def jump(t, x, y):  # Funktionen flyttar paddan till en punkt utan att rita
    t.penup()
    t.goto(x, y)
    t.pendown()


def make_turtle(x, y, visible = True):  # Skapar en sköldpadda vid position (x, y) genom att anropar jump()
    t = turtle.Turtle()     # Skapar paddan
    if not visible:     # Om visible = false, ska paddan döljas och högsta hastigheten
        t.hideturtle()
        t.speed(0)
    jump(t, x, y)       # Anropar jump till position (x, y)
    return t


def rectangle(x, y, width, height, color):  # Ritar en rektangel, användaren väljer storlek, position och färg
    t = make_turtle(x, y)   # Anropar make_turtle() till en viss position
    t.hideturtle()      # Döljer paddan
    t.fillcolor(color)  # Väljer vilken färg rektangeln ska fyllas med
    t.begin_fill()
    for dist in [width, height, width, height]: # För varje värde på bredd och höjd i listan ska:
        t.forward(dist)     # paddan röra sig fram det värdet
        t.left(90)      # Svänga vänster 90 grader
    t.end_fill()


def tricolore2(x, y, h):    # Ritar franska flaggan med höjden h och proportionerna 3:2
    w = h/2     # Beräknar bredden för varje liten rektangel (w = (3*h)/(2*3) = h/2)
    rectangle(x, y, w, h, 'blue')   # anropar rectangle() för att rita första triangeln med färg blå
    rectangle(x+w, y, w, h, 'white')    # -||-
    rectangle(x+2*w, y, w, h, 'red')    # -||-


def pentagram(x, y, side, color):   # Ritar en stjärna, användaren bestämmer sidlängd, färg och position
    t = make_turtle(x, y)   # anropar make_turtle()
    t.hideturtle()
    t.fillcolor(color)      # väljer färg
    t.begin_fill()
    t.right(72)     # Paddan börjar med riktning (x, 0). Den vrids då höger 72 grader
    for i in range(5):  # ritar triangelns alla sidor
        t.forward(side)
        t.right(144)    # vrider paddan 144 grader för att skapa 36 graders vinkel i triangelns hörn.
    t.end_fill()


def random_turtle(side=500):    # Skapar en kvadrat med sidan 500 om inget annat anges samt placerar en padda i rutan.
    low = -side//2      # Start koordinat för kvadraten (y)
    high = side//2      # Start koordinat för kvadraten (x)
    rectangle(low, low, side, side, 'SkyBlue')
    t = make_turtle(random.randint(low, high),  # Placerar en sköldpadda på slumpmässig plats i kvadraten
                    random.randint(low, high))
    t.setheading(random.randint(0, 359))    # Ger sköldpaddan en slumpad riktning
    return t


for i in [-100, -50, 0, 50, 100]:       # Ritar upp 5 stjärnor över flaggan och 5 stjärnor under flaggan
    pentagram(i, 150, 50, 'yellow')     # Ritar gula stjärnor över flaggan
    pentagram(i, -100, 50, 'yellow')    # Ritar gula stjärnor under flaggan
tricolore2(-100, -66, 132)      # Ritar franska flaggan med bestämda x-, y-koordinater samt bestämd höjd
