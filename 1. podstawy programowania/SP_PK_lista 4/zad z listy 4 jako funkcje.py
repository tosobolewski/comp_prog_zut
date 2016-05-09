import datetime

##    Napisz i przetestuj funkcję o nazwie CzyPrzestępny,
##    która otrzymuje jako parametr liczbę całkowitą reprezentującą rok,
##    zwracającą True jeśli rok jest przestępny i False w przeciwnym przypadku.

##    Uwaga - kalendarz gregoriański obowiązuje w Polsce od 1582 roku.

def CzyPrzestępny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        return True
    else:
        return False


def CzyPrzestępny2(rok):
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def CzyPrzestępny3(rok):
    if rok % 4 != 0:
        return False
    else:
        if rok % 100 != 0:
            return True
        else:
            if rok % 400 != 0:
                return False
            else:
                return True



def DniWMiesiącu(rok, miesiąc):
    dni_miesiąca = ['0',31,28,31,30,31,30,31,31,30,31,30,31]

    if miesiąc < 1 or miesiąc > 12 or miesiąc != int(miesiąc) or rok != int(rok):
        return None

    miesiąc = int(miesiąc)
    rok = int(rok)
    
    if miesiąc == 2 and CzyPrzestępny(rok): # luty w roku przestępnym ma 29 dni
        return 29
    else:
        return dni_miesiąca[miesiąc]

'''
Sprawdzenie poprawności roku, miesiąca i dnia
'''
def PoprawnyRok(rok):
    if  rok == int(rok) and rok >= 1582:
        return True

def PoprawnyMiesiąc(miesiąc):
    if  miesiąc == int(miesiąc) and miesiąc >= 1 and miesiąc <=12:
        return True

def PoprawnyDzień(rok, miesiąc, dzień):
    if  dzień == int(dzień) and dzień >= 1 and dzień <= DniWMiesiącu(rok, miesiąc):
        return True

'''
Napisz i przetestuj funkcję o nazwie DzieńWRoku,
która otrzymuje jako parametry trzy liczby całkowite:
pierwsza reprezentuje rok, druga miesiąc, trzecia dzień miesiąca;
funkcja powinna obliczać, którym dniem w roku jest dzień określony
w parametrach albo zwracać None, jeśli argumenty są niepoprawne.
'''

def DzieńWRoku(rok, miesiąc, dzień):
    # sprawdzenie poprawności danych
    if  rok != int(rok) or miesiąc != int(miesiąc) or dzień != int(dzień):
        return None
    elif rok < 1582:
        return None
    elif miesiąc < 1 or miesiąc > 12:
        return None
    elif dzień < 1 or dzień > DniWMiesiącu(rok, miesiąc):
        return None
    ############ TODO czy dać tu else: obliczenia ... ???

    # obliczenia
    suma_dni=0
    for m in range(1,miesiąc):
        suma_dni += DniWMiesiącu(rok, miesiąc)

    suma_dni = suma_dni + dzień
    return suma_dni

'''
Napisz i przetestuj funkcję o nazwie DzieńTygodnia,
która otrzymuje jako parametry trzy liczby całkowite:
pierwsza reprezentuje rok, druga miesiąc, trzecia dzień miesiąca;
funkcja powinna obliczać jaki dzień tygodnia wypada w podany dzień
i zwracać 0 dla niedzieli, 1 dla poniedziałku, etc.;
zwróć None jeśli argumenty są niepoprawne.
'''

def DzieńTygodnia(rok, miesiąc, dzień):
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

'''
Napisz i przetestuj funkcję o nazwie DniDoKońcaRoku,
która otrzymuje jako parametry trzy liczby całkowite:
pierwsza reprezentuje rok, druga miesiąc, trzecia dzień miesiąca;
funkcja powinna obliczać, ile minie dni do końca roku
począwszy od dnia określonego w parametrach;
zwróć None jeśli argumenty są niepoprawne.
'''

def DniDoKońcaRoku(rok, miesiąc, dzień):
    # sprawdzenie poprawności danych TODO
                ## czy trzeba TU sprawdzać poprawność danych ?
                ## Czy wystarczy jak będą sprawdzone w innej funkcji,
                ## która zwraca None, np. w DzieńWRoku(dzień, miesiąc, rok)

    # obliczeia
    if CzyPrzestępny(rok) == None or DzieńWRoku(rok,miesiąc, dzień) == None:
        return None

    if CzyPrzestępny(rok):
        return 366 - DzieńWRoku(rok, miesiąc, dzień)
    else:
        return 365 - DzieńWRoku(rok, miesiąc, dzień)
    
'''
Napisz i przetestuj funkcję o nazwie DniMiędzyDatami,
która otrzymuje jako parametry sześć liczb całkowitych:
pierwsze trzy reprezentują rok, miesiąc i dzień pierwszej daty,
kolejne trzy - drugiej daty; funkcja powinna obliczać,
ile dni mija pomiędzy podanymi datami;
rozważ zachowania funkcji we wszystkich możliwych przypadkach.
'''

def DniMiędzyDatami(rok1=None, miesiąc1=None, dzień1=None, \
                    rok2=None, miesiąc2=None, dzień2=None):
    ''' oblicza ile dni mija pomiędzy podanymi datami'''
    # sprawdzenie poprawności danych TODO
    # rozważ zachowania funkcji we wszystkich możliwych przypadkach. TODO
    if DzieńWRoku(rok1, miesiąc1, dzień1) == None \
    or DzieńWRoku(rok2, miesiąc2, dzień2) == None:
        return None
    
    # obliczenia
    dwr1 = DzieńWRoku(rok1, miesiąc1, dzień1)
    dwr2 = DzieńWRoku(rok2, miesiąc2, dzień2)

    r = rok1
    while r < rok2:
        if CzyPrzestępny(r) == None:
            return None
        else:
            if CzyPrzestępny(r) == True:
                dwr2 += 366
            else:
                dwr2 += 365
        r += 1
        
    return dwr2 - dwr1



def IleDniŻyjesz(rok, miesiąc, dzień):
    # sprawdzenie poprawności danych TODO
    dziś = datetime.datetime.now()

    if DzieńWRoku(rok, miesiąc, dzień) == None:
        return None

    if DzieńWRoku(dziś.year, dziś.month, dziś.day) == None:
        return None

    if rok > dziś.year:
        return None
    if rok == dziś.year and miesiąc > dziś.month:
        return None
    if rok == dziś.year and miesiąc == dziś.month and dzień > dziś.day:
        return None
    
    # obliczenia
    wynik = DniMiędzyDatami(rok, miesiąc, dzień, dziś.year, dziś.month, dziś.day)

    print('Przeżyłeś już '+ str(wynik) + ' dni!')


'''
Napisz i przetestuj funkcję o nazwie TydzieńWRoku,
która otrzymuje jako parametry trzy liczby całkowite:
pierwsza reprezentuje rok, druga miesiąc, trzecia dzień miesiąca;
funkcja powinna obliczać numer tygodnia w roku odpowiadającego temu dniu;
zwróć None jeśli argumenty są niepoprawne.
Załóż, że tydzień zaczyna się w poniedziałek oraz że pierwszy tydzień roku
zaczyna się 1 stycznia i kończy w pierwszą niedzielę roku.
'''

def TydzieńWRoku(rok, miesiąc, dzień):
    # sprawdzenie poprawności danych TODO

    # obliczenia
    dwr = DzieńWRoku(rok, miesiąc, dzień)
    i = 1
    dt = 7
    while dt > 0:   # 0 -> Niedziela
        dt = DzieńTygodnia(rok, 1, i)
        dzieńKońcaPierwszegotygodnia = i
        i += 1

    LiczbaTygodni = 1 + (dwr - dzieńKońcaPierwszegotygodnia - 1) // 7 +1
    return LiczbaTygodni

'''
#9
Napisz i przetestuj funkcję o nazwie IleLiter,
która otrzymuje łańcuch jako argument i liczy zawarte w nim litery.
'''
def IleLiter(napis=''):
    lista = [0] * (1+ord('Z')-ord('A'))
    napis = napis.upper()
    
    for litera in napis:
        if litera < 'A' or litera > 'Z':
            pass
        else:
            lista[ord(litera)-ord('A')] += 1

    return lista

def ProgramIleLiter():
    napis = input('wprowadź przykładowy napis :')
    wynik = IleLiter(napis)
    print(wynik)
    for i in range(0,len(wynik)):
        if wynik[i] != 0:
            print(chr(i + ord('A')), '...', wynik[i])


def ProgramIleLiterTest(test = True):
    if test == True:
        print('-----PROGRAM ILE LITER TEST ------')
        str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print(IleLiter(str))
        print(IleLiter(str+str))
        print(IleLiter(str+str.lower()))
        print('----------------------------------')

ProgramIleLiter()
ProgramIleLiterTest(None)

'''
#14
Pewien nierozsądny łańcuszek, zbyt często rozsyłany w Internecie, twierdzi,
że "miesiąc z 5 pełnymi weekendami przypada raz na 823 lata!
Chińczycy nazywają to kieszenią pełną srebra, a każdy kto usłyszał tę nowinę,
winien ją - według Feng Shui - przekazać dalej, w przeciwnym wypadku
zostanie nędzarzem". Przez grzeczność pominiemy fakt, że słowo weekend
raczej nie było znane w starożytnych Chinach i zajmiejmy się wyłącznie
arytmetyczną stroną tego zagadnienia. Przeanalizuj, jakie warunki musi
spełniać miesiąc, aby było w nim 5 weekendów, a wiedząc to, napisz program,
który odpytuje użytkownika o numer roku i wskazuje te miesiące owego roku,
które szczycą się tą błogosławioną cechą.
'''
def CzyPięćWeekendówWMiesiącu(rok, miesiąc):
    if DniWMiesiącu(rok, miesiąc) < 30:
        return False
    elif DzieńTygodnia(rok, miesiąc, 1) == 6: # 6 -> sobota
        return True
    elif DzieńTygodnia(rok, miesiąc, 1) >= 5 and DniWMiesiącu(rok, miesiąc) == 31:
        return True
    else:
        return None
    
def ProgramPięćWeekendów():
    print('Program sprawdza, czy w danym miesiącu w roku występuje 5 pełnych weekendów.')
    rok = int(input('Podaj rok :'))
    miesiąc = int(input('Podaj miesiąc :'))
    print(CzyPięćWeekendówWMiesiącu(rok, miesiąc))

def ProgramPięćWeekendówTest(test = True):
    if test == True:
        print('-----PROGRAM 5 WEEKENDÓW TEST ------')
        suma = 0
        for i in range(1582,2017):
            for j in range(1,12+1):
                if CzyPięćWeekendówWMiesiącu(i, j):
                    print(i, j)
                    suma +=1
        print('Zliczono łącznie', suma, 'przypadków wystąpienia 5 weekendów w miesiacu')
        print('------------------------------------')

ProgramPięćWeekendówTest(None)

'''
#15
Napisz program, który odpytuje kolejno użytkownika o:
- datę płatności pewnej faktury
- kwotę tejże faktury
a następnie oblicza kwotę karnych odsetek od przeterminowanej zaległości
od dnia następnego po terminie płatności do dzisiaj.
Załóż, że odsetki oblicza się tylko za dni robocze
dla uproszczenia przyjmiemy, że są to dni od poniedziałku do piątku
i nie będziemy oglądać się na święta) i że wynoszą one 8% rocznie.
Pamiętaj, że kwotę odsetek zaokrągla sie do 50 gr.
'''
def DzieńNastępny(rok, miesiąc, dzień):
    if dzień < DniWMiesiącu(rok, miesiąc):
        return [rok, miesiąc, dzień+1]
    elif miesiąc < 12:
        return [rok, miesiąc+1, 1]
    elif miesiąc == 12:
        return [rok+1, 1,1]
    else:
        return None

def PoliczOdsetki(rok1, miesiąc1, dzień1, rok2, miesiąc2, dzień2, kwota, odsetki):
    rok1, miesiąc1, dzień1 = int(rok1), int(miesiąc1), int(dzień1)
    rok2, miesiąc2, dzień2 = int(rok2), int(miesiąc2), int(dzień2)
    kwota = float(kwota)
    odsetki = (odsetki/100) / (365*(5/7))      # odsetki 8% tylko za dni robocze 5 dni/tydz.

    if rok1 > rok2:
        return None
    if rok1 == rok2 and miesiąc1 > miesiąc2:
        return None
    if rok1 == rok2 and miesiąc1 == miesiąc2 and dzień1 > dzień2:
        return None


    dmd = DniMiędzyDatami(rok1, miesiąc1, dzień1, rok2, miesiąc2, dzień2)
    dn = [rok1, miesiąc1, dzień1]
    dniroboczeodsetkowe = 0
    #print('dmd=', dmd)
    while dmd != 0:
        dn = DzieńNastępny(dn[0], dn[1], dn[2])
        dt = DzieńTygodnia(dn[0], dn[1], dn[2]) # 0 -> niedziela, 1 -> pon.
        #print('dt=',dt)
        if dt > 0 and dt < 6:       # 1..5 -> poniedziałek .. piątek
            dniroboczeodsetkowe += 1
        dmd -= 1
    #print('dniroboczeodsetkowe=',dniroboczeodsetkowe)

    ods = odsetki * dniroboczeodsetkowe * kwota
    złotówki = int(ods)
    grosze = int((ods - złotówki)*100)
    if grosze < 50:
        return złotówki
    else:
        return złotówki + 1

def ProgramOdsetki():
    data = input('Podaj datę w formacie rrrr mm dd :')
    kwota = float(input('Podaj kwotę faktury :'))

    data_lista = data.split()
    dziś = datetime.datetime.now()

    ods = PoliczOdsetki(data_lista[0], data_lista[1], data_lista[2], \
                  dziś.year, dziś.month, dziś.day, kwota, 8)
    
    print('Obliczono odsetki w kwocie :', ods, 'zł')


def ProgramOdsetkiTest(test = True):
    if test == True:
        print('-----PROGRAM ODSETKI TEST ------')
        dn = DzieńNastępny(2000,12,31)
        print(dn)

        print(PoliczOdsetki(2016,2,1,2016,2,14,100, 8))
        print(PoliczOdsetki(2016,2,1,2016,12,14,100, 8))
        print(PoliczOdsetki(2014,2,1,2016,2,14,100, 8))
        print(PoliczOdsetki(2017,2,1,2016,2,14,100, 8))
        print('--------------------------------')
    
ProgramOdsetkiTest(None)


'''  
for i in range(1582,2400+1,1):
    if CzyPrzestępny(i) == CzyPrzestępny3(i):
        pass
    else:
        print(i, CzyPrzestępny(i), CzyPrzestępny2(i))
'''

'''
##    Aby ustalić, czy rok jest to rok przestępny, wykonaj następujące kroki:
##    1 Jeśli rok jest podzielny przez 4, przejdź do kroku 2. W przeciwnym razie przejdź do kroku 5.
##    2 Jeśli rok jest podzielny przez 100, przejdź do kroku 3. W przeciwnym razie przejdź do kroku 4.
##    3 Jeśli rok jest podzielny przez 400, przejdź do kroku 4. W przeciwnym razie przejdź do kroku 5.
##    4 Rok jest to rok przestępny (ma 366 dni).
##    5 Rok nie jest to rok przestępny (ma 365 dni).
'''


'''
#print(DzieńTygodnia(2016,2,3)) # środa -> 3

IleDniŻyjesz(2011,1,1)


for i in range(1,13):
    print(i,'\t\t', DzieńWRoku(2016,1,i),'\t',TydzieńWRoku(2016,1,i))
    
'''
