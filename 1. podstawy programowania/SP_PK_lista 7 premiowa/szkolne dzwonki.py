# Szkolne dzwonki

godzina_startu = int(input())   #'Podaj godzinę : '
minuty_startu = int(input())    #'Podaj minuty : '

LEKCJA = 45
godzina = 60
doba = 24*60

# wczytaj czasy przerw dopóki nie zostanie wprowadzone 0 ; t: t >0 i t<=10080)
t = None
przerwy = []
while t != 0:
    t = int(input())            # podaj czas przerwy
    przerwy.append(t)

# lista z ilością minut dla dzwonka, które upłynęły od godz. 0:00
dzwonek = []
dzwonek.append(godzina_startu * godzina + minuty_startu)
for przerwa in przerwy:
    dzwonek.append(dzwonek[-1] + LEKCJA)
    dzwonek.append(dzwonek[-1] + przerwa)

'''#usuń dzwonek kończący przerwę po ostatniej lekcji'''
del dzwonek[-1]

# wypisz zamieione minuty w liście 'dzwonek' na godziny w formacie [g:m]
for minuty in dzwonek:
    m = minuty % godzina
    g = (minuty % doba) // godzina
    print((str(g)+':'+str(m)))

