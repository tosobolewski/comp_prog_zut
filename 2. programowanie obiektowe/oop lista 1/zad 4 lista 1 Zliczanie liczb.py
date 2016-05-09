# zad 4 lista 1

'''
Klasa do zliczania liczb (dodawanie i odejmowanie)
'''


class KontenerLiczb:
    def __init__(self):
        self.suma = 0

    def dodaj(self, p):
        self.suma += p

    def odejmij(self, p):
        self.suma -= p


k = KontenerLiczb() 

for i in range(0,100, 10):
    k.dodaj(10)
    print(i, k.suma)


for i in range(0,100, 10):
    k.odejmij(10)
    print(i, k.suma)
