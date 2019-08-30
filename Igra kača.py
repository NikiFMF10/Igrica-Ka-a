import turtle
import random


glava = [0]

#rezultat
a = [0]
b = [0]

#koordinate hrane 
koordhrane = [0, 0, 0]

#pozicija kače
pozicija_kače = []


def začetni(x, y):                       
    x = 0
    y = 0
    a [0] = 0
    b [0] = 0
    glava [0] = 0
    koordhrane [2] = 0
    pozicija_kače [:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("red")
    turtle.goto(0,0)
    turtle.write("Igraj")
    turtle.title("Igra Kača")
    turtle.onscreenclick(start)
    turtle.mainloop()

def okno():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color("black")
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)

def start(x,y):
    turtle.onscreenclick(None)

    okno()

    hrana1 = turtle.Turtle()
    hrana1.hideturtle()
    hrana1.pu()
    hrana1.speed(0)
    hrana1.shape("square")
    hrana1.color("red")

    rezultat = turtle.Turtle()
    rezultat.hideturtle()
    rezultat.pu()
    rezultat.speed(0)
    rezultat.goto(100,-250)
    rezultat.write("Rezultat:" + str(a [0]), align = "center", font = (10))
    
    while x > -210 and x < 210 and y > -210 and y < 210:
        if koordhrane [2] == 0:
            hrana (hrana1)
            koordhrane [2] = 1
        turtle.onkey(gor,"Up")
        turtle.onkey(levo,"Left")
        turtle.onkey(desno,"Right")
        turtle.onkey(dol,"Down")
        turtle.listen()
        premikanje()
        x = turtle.xcor()
        y = turtle.ycor()        
        if x > koordhrane [0] * 20 - 5 and x < koordhrane [0] * 20 + 5 and y > koordhrane [1] * 20 - 5 and y < koordhrane [1] * 20 + 5:
            koordhrane [2] = 0
            hrana1.clear()
            a [0] += 1
            rezultat.clear()
            rezultat.write("Rezultat: " + str(a [0]), align = "center", font = (10))
        
        if len(pozicija_kače) > 1:
            for i in range(1, len(pozicija_kače)):
                if x < pozicija_kače [i][0] + 5 and x > pozicija_kače [i][0] - 5 and y < pozicija_kače [i][1] + 5 and y > pozicija_kače [i][1] - 5:
                        rezultat.clear()
                        hrana1.clear()
                        konecigre()
    rezultat.clear()
    hrana1.clear()
    konecigre()


#Hrana
def hrana (hrana1):
    x = random.randrange(-8 , 8, 1)
    y = random.randrange(-8, 8, 1)
    koordhrane [0] = x
    koordhrane [1] = y
    hrana1.hideturtle()
    hrana1.pu()
    hrana1.shape("square")
    hrana1.color("red")
    hrana1.goto(x * 20, y * 20)
    hrana1.stamp()

#Gor   
def gor ():
    if glava [0] == 270:
        pass
    else:
        glava [0] = 90
#Dol
def dol ():
    if glava [0] == 90:
        pass
    else:
        glava [0] = 270
#Levo
def levo ():
    if glava [0] == 0:
        pass
    else:
        glava [0] = 180
#Desno 
def desno ():
    if glava [0] == 180:
        pass
    else:
        glava [0] = 0

def premikanje ():
    turtle.pensize(1)
    turtle.color("green")
    turtle.pu()
    turtle.speed(3)
    turtle.setheading(glava [0])
    turtle.shape("square")
    turtle.stamp()
    turtle.fd(20)
    x = turtle.xcor()
    y = turtle.ycor()
    if b [0] > a [0]:     
        turtle.clearstamps(1)
        pozicija_kače.insert(0, [round(x), round(y)])
        pozicija_kače.pop(-1)
    else:
        pozicija_kače.insert(0, [round(x), round(y)])       
        b [0] += 1    
    
def konecigre ():
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0,150)
    turtle.color("red")
    turtle.write("Konec igre", align = "center", font = (15))
    turtle.goto(0,50)
    turtle.write("Tvoj rezultat: " + str(a [0]), align = "center", font = (10))
    turtle.goto(200,-200)
    turtle.write("Vrni se nazaj", align = "right", font = (0.0000001))
    turtle.onscreenclick(začetni)
    turtle.mainloop()
    
        
if __name__ == '__main__':
    začetni(0,0)