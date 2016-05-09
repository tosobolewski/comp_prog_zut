# zad 6 lista 1

'''
Kalendarz
'''

class Kalendarz:
    def __init__(self,rok, miesiąc):
        self.rok = rok
        self.miesiąc = miesiąc
            
    def CzyPrzestępny(self):    # czy tak mozna >> self.rok ?
        rok = self.rok
        if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
            return True
        else:
            return False        

    def DniWMiesiącu(self):
        rok = self.rok
        miesiąc = self.miesiąc
        dni_miesiąca = ['0',31,28,31,30,31,30,31,31,30,31,30,31]

        if miesiąc < 1 or miesiąc > 12 or miesiąc != int(miesiąc) or rok != int(rok):
            return None

        miesiąc = int(miesiąc)
        rok = int(rok)
        
        if miesiąc == 2 and self.CzyPrzestępny(): # luty w roku przestępnym ma 29 dni
            return 29
        else:
            return dni_miesiąca[miesiąc]

    def DzieńTygodnia(self, rok, miesiąc, dzień = 1):
        rok = self.rok
        miesiąc = self.miesiąc
        dzień = 1
        # sprawdzenie poprawności danych TODO
        
        # obliczenia
        miesiąc -= 2
        if miesiąc <= 0:
            miesiąc += 12
            rok -= 1
        miesiąc *= 83
        miesiąc //=32
        wynik = miesiąc + dzień
        wynik += rok
        wynik += rok//4
        wynik -= rok//100
        wynik += rok//400
        wynik %= 7
        # 0 → niedziela, 1 → poniedziałek, 2 → wtorek, , 3 → środa,
        # 4 → czwartek, 5 → piątek, 6 → sobota
        return wynik


    def WypiszNaKonsolę(self, szer = 4):

        if szer < 4:
            szer = 4
        
        listaDniTygodnia = 'pn wt śr czw pt so nie'.split()
        listaMiesięcy = 'styczeń luty marzec kwiecień maj czerwiec lipiec sierpień wrzesień październik listopad grudzień'.split()
        lista = self.MiesiącDoKalendarza()
        
        # nagłówek 0
        nagłówek0 = listaMiesięcy[self.miesiąc-1]+' '+str(self.rok)
        nagłówek0 = nagłówek0.center(7*szer)
    
        # nagłówek
        nagłówek = ''
        for el in listaDniTygodnia:
            nagłówek += el.rjust(szer)
            
        #wiersze kalendarza
        wiersze_kalendarza = []
        w = ''
        i = 0
        for el in lista:
            if el == 0:
                el = '' # zastąp zera spacjami
            w += str(el).rjust(szer)            
            if i < 6:
                i += 1
            else:   # dla 7-go dnia
                wiersze_kalendarza.append(w)
                w = ''
                i = 0


        # wydruk na konsolę
        print(nagłówek0)
        print(nagłówek)
        for el in wiersze_kalendarza:
            print(el)

    def MiesiącDoKalendarza(self):
        n = self.DniWMiesiącu()
        
        # przeliczenie 'dzień_pierwszy' tak, aby niedziela była ostatnim dniem tygodnia
        # tj. 0 → poniedziałek, ... , 6 → niedziela
        dzień_pierwszy = self.DzieńTygodnia(self.rok, self.miesiąc) # 1 dzień miesiąca
        dzień_pierwszy = (dzień_pierwszy + 6)% 7

        lista = []

        ig = i2 = i3 = 0 # indeks graficzny; indeks dni bież. mies.; indeks dni nast. mies.
        while True:
            if ig < dzień_pierwszy:
                lista.append(0)                     # zero => '   ' 
                ig += 1
            elif ig == dzień_pierwszy:
                i2 = 1
                lista.append(1)
                i2 += 1
                ig += 1
            else:   # ig > dzień_pierwszy:
                if i2 <= n:
                    lista.append(i2)
                    i2 += 1
                    ig += 1
                elif (ig % 7 != 0):
                    i3 += 1
                    lista.append(0)                 # zero => '   ' 
                    ig += 1 
                else:
                    break
   
        return lista            

        
k = Kalendarz(2015, 12)
k.WypiszNaKonsolę(szer=6)

                
