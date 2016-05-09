# zad 1 lista 3

class Kształt:
    def __init__(self, a = None):
        self.a = a
        pass

class Rozmiar:
    def zmień(self, wsp):
        self.a *= wsp
        print('Zmiana rozmiaru, wsp = x', wsp)

class Kwadrat(Rozmiar, Kształt):
    def pokaż(self):
        print('Jestem kwadratem o boku a =', self.a)

class Koło(Rozmiar, Kształt):
    def pokaż(self):
        print('Jestem kołem o promieniu r =', self.a)


# koło 
koło = Koło(10)
koło.pokaż()
koło.zmień(10)
koło.pokaż()
print()


# kwadrat
kwadrat = Kwadrat(10)
kwadrat.pokaż()
kwadrat.zmień(5)
kwadrat.pokaż()
print()


