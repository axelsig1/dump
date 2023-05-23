# OU1 B
# Rita upp Vietnams flagga
import turtle


def jump(t, x, y):  # Funktionen flyttar paddan till en punkt utan att rita
    t.penup()
    t.goto(x, y)
    t.pendown()


def make_turtle(x, y, visible = True):      # Skapar en sköldpadda vid position (x, y) genom att anropar jump()
    t = turtle.Turtle()
    if not visible:
        t.hideturtle()
        t.speed(0)
    jump(t, x, y)
    return t


def pentagram(x, y, side, color):   # Stjärna utan sträck i mitten, användaren bestämmer sidlängd, färg och position
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    t.right(72)
    for i in range(5):      # Ritar omkretsen av en stjärna
        t.forward(side // 3)    # Paddan rör sig 1/3 del av sidlängden och svänger 72 grader mot nästa hörn
        t.left(72)
        t.forward(side // 3)    # Paddan rör sig 1/3 del av sidlängden och svänger 144 grader mot nästa hörn
        t.right(144)
    t.end_fill()


def rectangle(x, y, width, height, color):  # Ritar en rektangel
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()


def vietnamese_flag(x, y, height):      # Ritar den Vietnams flagga
    rectangle(x, y, height, height*2/3, 'red')      # Anropar rectangle() för att göra den röda rektangeln
    pentagram(0, 50, 150, 'yellow')     # Anropar pentagram() för att göra stjärnan i mitten


vietnamese_flag(-200, -150, 400)     # Anropar vietnamese_flag för att rita flaggan
