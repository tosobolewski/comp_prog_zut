#Zadanie 3 lista 2

n = int(input("podaj liczbe wyrazów ciągu Leibniza : "))

suma = 0
wyraz = 1
wsp = 1

if n == 0:
    print("suma wyrazów wynosi", suma)
else:
    while wyraz <= n:
        if wyraz % 2 == 0:
            suma = suma - (1/wsp)
        else:
            suma = suma + (1/wsp)
        wsp += 2
        wyraz +=1
        #print(wyraz, wsp)
    print("obliczona wartośc PI : ", suma * 4)
        
#PI = 3.14159
