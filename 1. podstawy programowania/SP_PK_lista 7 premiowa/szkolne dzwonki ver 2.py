# Szkolne dzwonki

godzina_startu = int(input())   #'Podaj godzinę : '
minuty_startu = int(input())    #'Podaj minuty : '

LEKCJA = 45
GODZINA = 60
DOBA = 24*60

# wczytaj czasy przerw dopóki nie zostanie wprowadzone 0 ; t: t >0 i t<=10080)
t = None
przerwy = [0]                   # brak przerwy przed pierwszą lekcją -> 0min
                                # nie wymaga pobrania danych od użytkownika
while t != 0:
    t = int(input())            # podaj czas przerwy
    if t > 0 and t <= 10080:
        przerwy.append(t)

# minuty, które upłynęły od godz. 0:00 dla każdego kolejnego dzwonka
dzwonek = []
dzwonek.append(godzina_startu * GODZINA + minuty_startu)    # przed I lekcją  
for przerwa in przerwy:
    if przerwa != 0:              
        dzwonek.append(dzwonek[-1] + przerwa)    
    dzwonek.append(dzwonek[-1] + LEKCJA)

# wypisz zamieione minuty w liście 'dzwonek' na godziny w formacie [g:m]
for minuty in dzwonek:
    m = minuty % GODZINA
    g = (minuty % DOBA) // GODZINA
    print((str(g)+':'+str(m)))


####    Przykład:
####    Wejście:
####    8
####    0
####    15
####    15
####    15
####    0
####    Wyjście
####
####    8:0
####    8:45
####    9:0
####    9:45
####    10:0
####    10:45
####    11:0
####    11:45
####                    15 min ->1455 min
