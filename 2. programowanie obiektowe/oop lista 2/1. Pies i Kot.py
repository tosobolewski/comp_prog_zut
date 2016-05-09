# zad 1 lista 2
# SP Programiowaine komputerów ZUT
# programowanie obiektowe
# @ Tomasz Sobolewski
# zajęcia 20.02.2016 r.

class Zwierze:
    def __init__(self, imie):
        self.imie = imie
        
    def odglos(self):
        print (self.zwierze, self.imie, 'mówi ', self.glos)
        

class Pies(Zwierze):
    def __init__(self, imie):
        super().__init__(imie)
        self.zwierze = 'Pies'
        self.glos = 'hau, hau ...'
        pass


class Kot(Zwierze):
    def __init__(self, imie):
        super().__init__(imie)
        self.zwierze = 'Kot'
        self.glos = 'miau ...'
        pass

x = []

x.append(Pies('Reksio'))
x.append(Kot('Mruczek'))
x.append(Pies('Pikuś'))
x.append(Kot('Czaruś'))
x.append(Pies('Irasiad'))
x.append(Kot('Kitka'))

for el in x:
    el.odglos()
    print()


