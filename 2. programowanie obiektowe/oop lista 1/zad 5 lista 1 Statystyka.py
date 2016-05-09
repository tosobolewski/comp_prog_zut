# zad 5 lista 1

'''
klasa Statystyka
'''


class Statystyka():
    def __init__(self, lista = None):

        self.lista = []
        if lista:
            self.lista = lista

     
    def suma(self):
        suma = 0
        for el in self.lista:
            suma += el
        return suma


    def średnia(self):
        if len(self.lista) > 0:
            return self.suma()/len(self.lista)
        else:
            return None


    def mediana(self):
        l = self.lista[:]
        l.sort()
        if len(l)% 2 == 0:
            a = l[(len(l)-1)//2]
            b = l[(len(l)+1)//2]
            return (a + b )/ 2  # długość listy parzysta
        else:
            return l[len(l)//2] # długość listy nieparzyst
        

    def minimum(self):
        minimum = None
        for el in self.lista:
            if minimum == None:
                minimum = el
            else:    
                if el < minimum:
                    minimum = el
                else:
                    pass

        return minimum


    def maksimum(self):
        maksimum = None
        for el in self.lista:
            if maksimum == None:
                maksimum = el
            else:    
                if el > maksimum:
                    maksimum = el
                else:
                    pass

        return maksimum
    


l1 = [1,2,3,4,5,6]
l2 = [1,2,3,4,5,6,7]

s = Statystyka(l1)
s2 = Statystyka(l2)

print(s.suma())
print(s.średnia())
print(s.minimum())
print(s.maksimum())

print()
#print(sum(l1))

print(s.mediana())
print(s2.mediana())

