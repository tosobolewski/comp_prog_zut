# zad 7 lista 1 programowanie obiektowe

'''
Przygotować klasę reprezentującą figurę geometryczną (na chwilę obecną kla-
sa ma przechowywać nazwę i położenie figury i je wypisywać
'''


class FiguraGeometryczna:

    def __init__(self, nazwa, polozenie):
        self.nazwa = nazwa
        self.polozenie = polozenie

    def nazwapokaz(self):
        print('Nazwa figury = ',self.nazwa)
        return self.nazwa

    def polozeniepokaz(self):
        print('Położenie figury = ',self.polozenie)
        return self.polozenie

def main():
    
    print('Teraz jestem w funkcji main()!')

    f1 = FiguraGeometryczna('kwadrat',[1,2])
    f2 = FiguraGeometryczna('prostokąt' , [5,6])
    f3 = FiguraGeometryczna('trójkąt',[9,8])

    for el in [f1, f2, f3]:
        print('')
        el.nazwapokaz()
        el.polozeniepokaz()

#
#
#

if __name__ == '__main__':
    main()













