   
def DługośćBoku(bok = None):
    # TODO poprawić wejście - wyjątki dla liter itd...
    try:
        while bok == None or bok % 2 == 0 or bok < 1 or bok > 32:
            bok = int(input('''Podaj bok spirali (liczba nieparzysta z zakresu od 1 do 31, wartość 0 - sam wiesz co) : '''))
            if bok == 0:
                return 0
        return bok
    except ValueError:
        print('Wprowadzono nieprawidłową wartość. Przyjęto bok spirali równy 9.\n')
        return 9
    except:
        print('Wprowadzono nieprawidłową wartość. Przyjęto bok spirali równy 5.')
        print('Nie zasłużyłeś na więcej :)\n')
        return 5
        

def PoleDoGóry(wsp):
    global X, Y
    wsp = [wsp[X]-1, wsp[Y]]
    return wsp

def PoleWPrawo(wsp):
    global X, Y
    wsp = [wsp[X], wsp[Y]+1]
    return wsp

def PoleWDół(wsp):
    global X, Y
    wsp = [wsp[X]+1, wsp[Y]]
    return wsp

def PoleWLewo(wsp):
    global X, Y
    wsp = [wsp[X], wsp[Y]-1]
    return wsp

def WypełnijPole(wsp):
    global X, Y
    global spirala
    global wypełnienie
    wypełnienie += 1
    spirala[wsp[X]][wsp[Y]] = str(wypełnienie).center(3)    
    return None




def ProgramSpiralaGraficznie(bok = None):
    '''Program wypełnia pola tablicy w kolejności opisanej kształtem spirali.

    Parametrem wejściowym jest bok wypełnianej tablicy. Bok tablicy jest
    liczbą naturalną nieparzystą z zakresu 1 do 31.
    '''
    # deklaracje i definicje
    global X,Y
    global spirala
    global wypełnienie    
    X,Y = 0,1
    spirala = [[0 for i in range(bok)] for i in range(bok)] # tablica bok x bok
    wypełnienie = 0

    # obliczenie współrzędnych srodka (początek spirali)
    srodek_x = srodek_y = bok // 2
    wsp = [srodek_x, srodek_y]
    

    # główna petla wypełniania spirali
    for bok_i in range(1,bok+1,2): # range od 1 do (bok) co 2
        
        if bok_i == 1:
            WypełnijPole(wsp)
            continue
            
        wsp = PoleDoGóry(wsp)
        WypełnijPole(wsp)

        for n in range(bok_i - 2):
            wsp = PoleWPrawo(wsp)
            WypełnijPole(wsp)

        for n in range(bok_i - 1):
            wsp = PoleWDół(wsp)
            WypełnijPole(wsp)

        for n in range(bok_i - 1):
            wsp = PoleWLewo(wsp)
            WypełnijPole(wsp)

        for n in range(bok_i - 1):
            wsp = PoleDoGóry(wsp)
            WypełnijPole(wsp)
            
    #wypisanie danych na ekran
    for x in range(bok):
        for y in range(bok):
            print(spirala[x][y], end=' ')
        print()
    print('\n')
    
    return None


def main():
    '''Funkcja uruchamiająca wykonanie ProgramSpiralaGraficznie().

    '''
    #intro
    ProgramSpiralaGraficznie(31)

    # ciągle pytaj o długość boku i wyświetlaj wynik
    while True:
        bok = None
        bok = DługośćBoku(bok)
        if bok == 0:
            print('\nKoniec programu.\n\nDZIĘKUJĘ !\n')
            break
        else:
            ProgramSpiralaGraficznie(bok)
    
    return None


def testy(test=None):
    '''Testy do funkcji ProgramSpiralaGraficznie().

    '''
    if test != None:
        ProgramSpiralaGraficznie()
        ProgramSpiralaGraficznie(-1)
        ProgramSpiralaGraficznie('a')
        ProgramSpiralaGraficznie([1])
        ProgramSpiralaGraficznie(0)
        ProgramSpiralaGraficznie(1)
        ProgramSpiralaGraficznie(5)
        ProgramSpiralaGraficznie(7)
        ProgramSpiralaGraficznie(9)
        ProgramSpiralaGraficznie(None)


'''
    Główne wywołania funkcji
'''
testy(None)
main()

