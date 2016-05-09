#Zadanie 5 lista 2

rok = miesiac = dzien = 0

dt = ['niedziela','poniedziałek','wtorek', \
      'środa','czwartek','piątek','sobota']

while (rok < 1 or rok > 9999) \
      or (miesiac < 1 or miesiac > 12) \
      or (dzien < 1 or dzien > 31):

    rok = int(input("Podaj rok : "))
    miesiac = int(input("Podaj miesiąc : "))
    dzien = int(input("Podaj dzień : "))

#1
miesiac -= 2

#2
if miesiac <= 0:
    miesiac += 12
    rok -= 1

#3
w = (miesiac * 83) // 32

#4
w = w + dzien

#5
w = w + rok

#6
w = w + (rok // 4)

#7
w = w - (rok // 100)

#8
w = w + (rok // 400)

#9
w %= 7

#10
print("Otrzymany wynik : ", dt[w])




# interpretacja wyniku:
# brawo! otrzymałeś numer dnia tygodnia w takiej oto konwencji:
# 0 → niedziela, 1 → poniedziałek, 2 → wtorek, , 3 → środa,
# 4 → czwartek, 5 → piątek, 6 → sobota
