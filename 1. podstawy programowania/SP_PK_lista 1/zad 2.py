print("WITAJ W KALKULATORZE")
print("CO CHCESZ ZROBIĆ?")
print("1 - dodać\2 - odjąć\3 - wymnożyć\4 - podzielić\0 - zakończyć pracę")
wybór=int(input ("TWÓJ WYBÓR?:"))
a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
# tu umieść swój kod
if wybór==1:
    print("suma=", a+b)
if wybór==2:
    print("różnica=", a-b)
if wybór==3:
    print("iloczyn=", a*b)
if wybór==4:
    if b!=0:
    print("iloraz=",a/b)
    else:
    print("Dzielisz przez zero!!!")
print("To koniec!")
