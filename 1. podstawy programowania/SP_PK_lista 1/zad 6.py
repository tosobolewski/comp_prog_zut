zarobki=float(input("Witaj, chcesz szybko obliczyć pit to podaj swój roczny dochód:"))
if zarobki<85528.0:
    print("To co musisz zapłacić:")
    print(round((0.18*zarobki-556.02),0))
else:
    nadwyzka = zarobki - 85528.0
    print("To co musisz zapłacić:")
    print(round(14839.02+(0.32*nadwyzka)))

