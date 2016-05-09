# zad 2 lista 3

import random

# ========================== Gracz =========================
class Gracz():
    def __init__(self):
        self.listaprzedmiotów = []
        self.x = 0 # wstępnie, będzie losowane TODO
        self.y = 0

    def move(where):      
        if where == 'o':
            self.up()
        elif where == 'l':
            self.down()
        elif where == 'a':
            self.left()
        elif where == 's':
            self.right()
        else:
            pass

    def up(self):
        self.x = x - 1
        self.y = y

    def down(self):
        self.x = x + 1
        self.y = y

    def left(self):
        self.x = x
        self.y = y - 1

    def right(self):
        self.x = x
        self.y = y + 1

    def ustawgracza(self):
        pass

    def pokażprzedmioty(self):
        for el in self.listaprzedmiotów:
            print(el)
        print()


#=========================== Mapa ===========================
class Mapa(Gracz):
    
    def __init__(self, wymiar):
        self.wymiar = wymiar
        self.plan = \
            [[ 0 for el in range(wymiar)] for el in range(wymiar)]

        self.gracz = Gracz()
        
        self.ustawpolaprzejściowe()
        self.ustawpolanieprzejściowe()
        self.ustawprzedmioty()
    pass

    def pokaż(self):
        for el in self.plan:
            for pok in el:
                if pok != 0:
                    print(pok.pokaż(),end = ' ')
            
            print()
            
    def ustawpolaprzejściowe(self):
        for i in range(self.wymiar):
            for j in range(self.wymiar):
                self.plan[i][j] = Pokój(True) 

    def ustawpolanieprzejściowe(self):
        for i in range(2*self.wymiar): # 2 x więcej pól zakrytych niż wymiar mapy
            x = random.randint(0,self.wymiar-1)
            y = random.randint(0,self.wymiar-1)
            self.plan[x][y] = Pokój(False)

    def ustawprzedmioty(self):
        for i in range(self.wymiar):
            for j in range(self.wymiar):
                if self.plan[i][j].jaki() == True: # jeżeli pokój przejściowy
                    r = random.randint(0,1)
                    if r == 1:
                        self.plan[i][j].przedmiot = Wartościowy()
                    else:
                        self.plan[i][j].przedmiot = Śmieć()
                        
                       
        
        jaki = random.randint(0,1)
        

# ========================== Przedmiot =========================
class Przedmiot:
    def __init__(self,wartośćprzedmiotu, nazwa = ''):
        self.nazwa = nazwa
        self.wartośćprzedmiotu = wartośćprzedmiotu # 1/0 = wartościowy, smieć
        pass

class Wartościowy(Przedmiot):
    def __init__(self):
        self.jaki = 'wartościowy'

    def pokaż(self):
        return '+'
        pass

class Śmieć(Przedmiot):
    def __init__(self):
        self.jaki = 'śmieć'
        pass

    def pokaż(self):
        return '.'
        pass

# ============================= Pokój ===========================
class Pokój():
    def __init__(self, rodzaj, przedmiot = None):
        
        self.rodzaj = rodzaj #zamurowany = False, przejściowy = True
        self.przedmiot = przedmiot
        self.jestgracz = None
        pass

    def jaki(self):
        return self.rodzaj

    def pokaż(self):
        if self.jestgracz == True:
            return 'G'
        
        if self.rodzaj == True:
            if self.przedmiot.jaki == 'wartościowy':
                return '+'
            elif self.przedmiot.jaki == 'śmieć':
                return '.'
            else:
                return '?'
        else:
            return 'X'
    


    
        
# ====================== main ===========================

m = Mapa(20)

m.pokaż()
