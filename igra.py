import turtle
import random

# smeri kot (x, y) koordinate
DESNO = (1, 0)
GOR = (0, 1)
LEVO = (-1, 0)
DOL = (0, -1)

# velikost plosce (to je polovica velikosti),
# celotna plosca ima (VELIKOST_PLOSCE * 2) ** 2 polj
VELIKOST_PLOSCE = 10

class Igra:
    def __init__(self):
        # zacetna smer kace
        self.smer = DESNO
        # dovolimo samo eno spremembo smeri na premik
        self.smer_spremenjena = False

        # koliko hrane je pojedla kača
        self.rezultat = 0

        # koordinate hrane 
        self.nova_hrana()

        # pozicija kače, zacetek seznama zacetek kace, 
        # konec seznama konec kace
        # naredi novo kačo dolgo 1 v točki (0,0)
        self.pozicija_kace = [(0, 0)]

        # ali je igre konec
        self.konec = False

    # naredi novo hrano na nakljucni poziciji
    # (mogoce bi bilo smiselno preveriti ce ni pod trenutno pozicijo kace)
    def nova_hrana(self):
        x = random.randint(-VELIKOST_PLOSCE + 1, VELIKOST_PLOSCE - 1)
        y = random.randint(-VELIKOST_PLOSCE + 1, VELIKOST_PLOSCE - 1)
        self.hrana = (x, y)

    # preveri ali se kaca lahko premakne v to polje
    # vrne True ce je veljavno sicer False
    def preveri_veljavnost(self, x, y):
        # preveri ali se je kaca zaletela sama vase
        for kos_kace in self.pozicija_kace:
            kos_kace_x, kos_kace_y = kos_kace


            if kos_kace_x == x and kos_kace_y == y:
                # na tem mestu je ze kaca
                return False

        # preveri ali je kaca cez rob
        if x <= -VELIKOST_PLOSCE or y <= -VELIKOST_PLOSCE or x >= VELIKOST_PLOSCE or y >= VELIKOST_PLOSCE:
            return False

        # sicer je vse vredu
        return True

    # premakne kaco za eno polje naprej v njeni trenutni smeri
    def premik(self):
        # trenutna lokacija glave
        x, y = self.pozicija_kace[0]

        # novo polje dobimo tako da pristejemo smer
        dx, dy = self.smer
        novi_x, novi_y = x + dx, y + dy

        # preveri ali se je kaca zaletela v rob ali sama vase
        if not self.preveri_veljavnost(novi_x, novi_y):
            # ni veljavno, koncaj igro saj se je kaca zaletela
            self.konec = True

        # dodaj glavo
        self.pozicija_kace = [(novi_x, novi_y)] + self.pozicija_kace

        # ali je kaca pojedla hrano
        if novi_x == self.hrana[0] and novi_y == self.hrana[1]:
            # dodaj tocke in naredi novo hrano
            self.rezultat += 1
            self.nova_hrana()
        else:
            # pobrisemo rep
            self.pozicija_kace.pop()

        # dovoljena nova sprememba smeri
        self.smer_spremenjena = False

    # funkcije ki obrnejo kaco v neko smer
    def desno(self):
        if self.smer == LEVO or self.smer_spremenjena:
            pass  # kaca se ne obraca za 180 stopinj ali smer je ze bila spremenjena
        else:
            self.smer = DESNO
            self.smer_spremenjena = True

    def gor(self):
        if self.smer == DOL or self.smer_spremenjena:
            pass
        else:
            self.smer = GOR
            self.smer_spremenjena = True

    def levo(self):
        if self.smer == DESNO or self.smer_spremenjena:
            pass
        else:
            self.smer = LEVO
            self.smer_spremenjena = True

    def dol(self):
        if self.smer == GOR or self.smer_spremenjena:
            pass
        else:
            self.smer = DOL
            self.smer_spremenjena = True

    # trenutna smer zelve v stopinjah
    def smer_v_stopinjah(self):
        if self.smer == DESNO:
            return 0
        elif self.smer == GOR:
            return 90
        elif self.smer == LEVO:
            return 180
        else:
            return 270
            