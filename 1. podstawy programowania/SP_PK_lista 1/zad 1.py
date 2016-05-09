from math import pi
x=float(input("Podaj zmienną x:"))
kwadratx=x*x
kwadratpi=pi*pi
wynik=(kwadratx/(kwadratpi*(kwadratx+0.5)))*(1+(kwadratx/(kwadratpi*(kwadratx-0.5)**2)))
print("Wynik działania to:",wynik)
