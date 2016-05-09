# zad. 4 lista 3 oop
# SP Programiowaine komputerów ZUT
# programowanie obiektowe
# @ Tomasz Sobolewski
# zajęcia 21.02.2016 r.

class Figura:
    def __init__(self, pole):
        if czy_dobre_dane(pole):
            self.kolumna = pole[0]  # a..h  (x)
            self.wiersz = pole[1]   # 1..8  (y)

    def przesunięcie_względne(self, pole_docelowe):
        ''' zwraca wektor przesunięcia względem bieżacej pozycji figury'''
        mov_x = chr(pole_docelowe[0]) - chr(self.kolumna)
        mov_y = int(pole_docelowe[1]) - int(self.wiersz)
        return [mov_x, mov_y]

    def czy_można_ruch(self, pole_docelowe):    # trzeba tu sprawdzić czy pole jest wolne
        if czy_dobre_dane(pole_docelowe):
            mov_vec = przesunięcie_względne(pole_docelowe)    
            if mov_vec in self.dozwolone:
                return True
        return False

    def wykonaj_ruch(self, pole_docelowe):
        if czy_można_ruch(pole_docelowe):
            self.kolumna = pole_docelowe[0]  
            self.wiersz = pole_docelowe[1]

    def notacjaXY(self, pole):
        ''' zwraca wsp. [x, y] gdzie [1,1] w lewym dolnym rogu (pole 'a1')'''
        x = chr(pole[0]) - chr('a') +1
        y = int(pole[1])
        return [x, y]

    def czy_dobre_dane(self, pole):    # trzeba tu sprawdzić czy pole jest wolne
        if pole[0] < 'a' or pole[0] > 'h'\
           or pole[1] < '1' or pole[1] > '8':
            return False
        return True
    
class Pion(Figura):
    def __init__(self, pole):
        super().__init__(pole)
        self._dozwolone = [[0,0], [0,1], [0,2]] # vect [0,2] będzie usunięty po wyk. pierwsz. ruchu
        self.pierwszy_ruch = True
        
    def wykonaj_ruch(self, pole_docelowe): 
        if czy_można_ruch(pole_docelowe):
            self.kolumna = pole_docelowe[0]
            self.wiersz = pole_docelowe[1]
            if self.pierwszy_ruch == True:  # specjalnie dla Pion warunek pierwszego ruchu
                self._dozwolone = [[0,0], [0,1]]     # del vect [0,2]
                self.pierwszy_ruch = False
      
class Wieża(Figura):
    def __init__(self, pole):
        super().__init__(pole)
        self._dozwolone = [[0,0],
                           [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7],
                           [0,-1], [0,-2], [0,-3], [0,-4], [0,-5], [0,-6], [0,-7],
                           [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0],
                           [-1,0], [-2,0], [-3,0], [-4,0], [-5,0], [-6,0], [-7,0]]    

class Skoczek(Figura):
    def __init__(self, pole):
        super().__init__(pole)
        self._dozwolone = [[0,0],
                           [-1,2], [1,2], [-1,-2], [1,-2],
                           [-2,-1], [-2,1], [2,-1], [2,1]]

class Goniec(Figura):
    def __init__(self, pole):
        super().__init__(pole)
        self._dozwolone = [[0,0],
                           [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7],
                           [-1,-1], [-2,-2], [-3,-3], [-4,-4], [-5,-5], [-6,-6], [-7,-7],
                           [1,-1], [2,-2], [3,-3], [4,-4], [5,-5], [6,-6], [7,-7],
                           [-1,1], [-2,2], [-3,3], [-4,4], [-5,5], [-6,6], [-7,7]]

class Hetman(Figura):
    def __init__(self, pole):
        super().__init__(pole)
        self._dozwolone = [[0,0],
                           [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7],
                           [0,-1], [0,-2], [0,-3], [0,-4], [0,-5], [0,-6], [0,-7],
                           [1,0], [2,0], [3,0], [4,0], [5,0], [6,0], [7,0],
                           [-1,0], [-2,0], [-3,0], [-4,0], [-5,0], [-6,0], [-7,0],
                           [1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7],
                           [-1,-1], [-2,-2], [-3,-3], [-4,-4], [-5,-5], [-6,-6], [-7,-7],
                           [1,-1], [2,-2], [3,-3], [4,-4], [5,-5], [6,-6], [7,-7],
                           [-1,1], [-2,2], [-3,3], [-4,4], [-5,5], [-6,6], [-7,7]]

class Król(Figura):
    def __init__(self, pole):
        super().__init__(pole)
        self._dozwolone = [[0,0],
                           [-1,-1], [-1,0], [-1,1], [0,1],
                           [1,1], [1,0], [1,-1], [0,-1]]
        

# ----------------------------------------- main ------------------------------------------
f = Figura('a1')
print(f.kolumna)
print(f.wiersz)


##a = [(1,2),(2,3),(4,5)]
##a.remove((0,2))
##
##a = [[1,2],[2,3],[4,5]]
##a.remove([0,2])


