import random

glava = [0]

#rezultat
a = [0]
b = [0]

#koordinate hrane 
koordhrane = [0, 0, 0]

#pozicija kače
pozicija_kače = []

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

class Igra:
    
    def __init__ (self, hrana, premikanje, konec_igre):
        self.hrana = hrana

    def hrana (hrana1):
    x = random.randrange(-8 , 8, 1)
    y = random.randrange(-8, 8, 1)
    koordhrane [0] = x
    koordhrane [1] = y

    def premikanje ()