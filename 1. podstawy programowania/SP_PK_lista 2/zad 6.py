#Zadnie 6 lista 2

godzina = minuta = podane_minuty = -1

while (godzina < 0 or godzina > 23) \
      or (minuta < 0 or minuta > 59) \
      or (podane_minuty < 0 or podane_minuty > 43200):

    godzina = int(input("Podaj godzinę : "))
    minuta = int(input("Podaj minutę : "))
    podane_minuty = int(input("Podaj ile dodać minut : "))

podane_minuty = minuta + podane_minuty

obl_godz = (godzina + podane_minuty // 60) % 24
obl_min = podane_minuty % 60

print(obl_godz,":",obl_min)
