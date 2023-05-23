# OU1 C
# Skapa en ruta med två sköldpaddor som flyttar sig slumpmässigt inom rutan
import turtle
import random


def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)
    return t


def rectangle(x, y, width, height, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()


def move_random(t):
    angle = random.randint(-45, 45)     # Slumpar en vinkel mellan -45 och 45 grader
    dist = random.randint(0, 25)    # Slumpar en sträcka mellan 0 och 25
    if abs(t.xcor()) > 250 or abs(t.ycor()) > 250:  # om paddan rör sig utanför kvadraten vänder den till origo och går tillbaka. (om x- eller y-koordinaterna är större än 250)
        t.setheading(t.towards(0, 0))
        t.forward(dist)
    else:       # Annars rör sig paddan slumpmässigt i kvadraten.
        t.left(angle)
        t.forward(dist)


rectangle(-250, -250, 500, 500, 'SkyBlue')  # Skapar en kvadrat med sidorna 500 och centrum i origo
t1 = turtle.Turtle()        # Skapar 2 sköldpaddor t1 och t2
t2 = turtle.Turtle()
t1.hideturtle()
t2.hideturtle()
jump(t1, random.randint(-250, 250), random.randint(-250, 250))   # Paddorna går till en slumpmässig plats inom kvadraten
jump(t2, random.randint(-250, 250), random.randint(-250, 250))
t1.showturtle()
t2.showturtle()
t1.color('green')   # Ger paddorna varsin färg
t2.color('red')
x = 0
for i in range(50):    # 500 anrop till move_random()
    move_random(t1)
    move_random(t2)
    if t2.distance(t1) < 50:    # Padda t2 skriver 'close' om paddorna är nära varandra
        t2.write('close')
        x += 1
print('Hur många gånger paddorna var nära varandra:', x)