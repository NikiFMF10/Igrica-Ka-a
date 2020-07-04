from igra import Igra, VELIKOST_PLOSCE
import turtle

# sirina polja v pikslih
SIRINA_POLJA = 20

# kolikokrat na sekundo se kaca premakne
FRAME_RATE = 10

class Vmesnik:
    def __init__(self):
        turtle.hideturtle()
        turtle.clear()
        turtle.pu()
        turtle.color('red')
        turtle.goto(0,0)
        turtle.write('Igraj')
        turtle.title('Igra Kača')
        turtle.onscreenclick(self.nova_igra)

        # slika se posodobi samo vsakih 1000 premikov, ali ko jo posodobimo rocno
        turtle.tracer(n=1000)
        
        turtle.mainloop()

    def nova_igra(self, *_):
        # naredi novo igro
        self.igra = Igra()

        turtle.onscreenclick(None)
        self.okno()

        # zelva ki rise hrano
        self.hrana = turtle.Turtle()
        self.hrana.hideturtle()
        self.hrana.pu()
        self.hrana.speed(0)
        self.hrana.shape('square')
        self.hrana.color('red')

        # zelva ki rise kaco
        self.kaca = turtle.Turtle()
        self.kaca.hideturtle()
        self.kaca.pu()
        self.kaca.speed(1)
        self.kaca.shape('square')
        self.kaca.color('green')

        # zelva ki rise rezultat
        self.rezultat = turtle.Turtle()
        self.rezultat.hideturtle()
        self.rezultat.pu()
        self.rezultat.speed(0)
        self.rezultat.goto(100,-250)

        # poslusaj na pritisk tipke        
        turtle.onkey(self.igra.gor, 'Up')
        turtle.onkey(self.igra.levo, 'Left')
        turtle.onkey(self.igra.desno, 'Right')
        turtle.onkey(self.igra.dol, 'Down')
        turtle.listen()

        self.narisi()

    def okno(self):
        turtle.clear()
        turtle.pu()
        turtle.speed(0)
        turtle.pensize(SIRINA_POLJA)
        turtle.color('black')
        turtle.goto(-VELIKOST_PLOSCE * SIRINA_POLJA, VELIKOST_PLOSCE * SIRINA_POLJA)
        turtle.pd()
        turtle.goto(VELIKOST_PLOSCE * SIRINA_POLJA, VELIKOST_PLOSCE * SIRINA_POLJA)
        turtle.goto(VELIKOST_PLOSCE * SIRINA_POLJA, -VELIKOST_PLOSCE * SIRINA_POLJA)
        turtle.goto(-VELIKOST_PLOSCE * SIRINA_POLJA, -VELIKOST_PLOSCE * SIRINA_POLJA)
        turtle.goto(-VELIKOST_PLOSCE * SIRINA_POLJA, VELIKOST_PLOSCE * SIRINA_POLJA)
        turtle.pu()
        turtle.goto(0,0)

    def narisi(self):
        # premakni kaco
        self.igra.premik()

        # narisi hrano
        self.hrana.clear()
        self.hrana.goto(self.igra.hrana[0] * SIRINA_POLJA, self.igra.hrana[1] * SIRINA_POLJA)
        self.hrana.stamp()

        # narisi vse dele kace
        self.kaca.clear()
        for kos_kace in self.igra.pozicija_kace:
            self.kaca.goto(kos_kace[0] * SIRINA_POLJA, kos_kace[1] * SIRINA_POLJA)
            self.kaca.stamp()
        
        # narisi rezultat
        self.rezultat.clear()
        self.rezultat.write('Rezultat: ' + str(self.igra.rezultat), align='center', font=(10))

        # konco zares narisi vse na zaslon
        turtle.update()

        # konec igre
        if self.igra.konec:      
            self.rezultat.clear()
            self.hrana.clear()
            self.kaca.clear()
            self.konecigre()

        # narisi ponovno cez t milisekund
        turtle.ontimer(self.narisi, t=int(1000 / FRAME_RATE))

    def konecigre(self):
        turtle.onscreenclick(None)
        turtle.speed(0)
        turtle.pu()
        turtle.goto(0,150)
        turtle.color('red')
        turtle.write('Konec igre', align='center', font=(15))
        turtle.goto(0,50)
        turtle.write('Tvoj rezultat: ' + str(self.igra.rezultat), align='center', font = (10))
        turtle.goto(180,-180)
        turtle.write('Poskusi znova', align='right', font=(0.0000001))
        turtle.onscreenclick(self.nova_igra)
        turtle.mainloop()


if __name__ == '__main__':
    vmesnik = Vmesnik()

