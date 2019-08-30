import turtle
import model

def koordinate_hrane (hrana1):
    hrana1.hideturtle()
    hrana1.pu()
    hrana1.shape("square")
    hrana1.color("red")
    hrana1.goto(x * 20, y * 20)
    hrana1.stamp()

igra = model.nova_igra ()