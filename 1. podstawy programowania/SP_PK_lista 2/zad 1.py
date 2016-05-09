#Zadanie 1 lista 2

lata = 2016-1626
kwota = 24

#print(lata)

for i in range(lata):
    odsetki = round(kwota * 0.035,2)
    podatek = round(odsetki * 0.19,2)
    kwota = round(kwota + (odsetki - podatek),2)
    print("rok = ", 1626 + i," | odsetki = ", odsetki, " | podatek = ", podatek, " | kwota po roku = ", kwota)
 


# wynik:
# rok =  2015
# odsetki =  44354.96
# odatek =  8427.44
# kwota po roku =  1303212.07
