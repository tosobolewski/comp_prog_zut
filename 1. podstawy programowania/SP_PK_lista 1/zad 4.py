print ("Witaj, sprawdźmy, czy Twój rok jest rokiem przestępnym? ;)")
rok=int(input("Podaj ten rok, pamiętaj muszą być to lata od 1582!"))

if rok<1582:
    print ("Oj, głuptasku mówiłem po 1582!")
else:
    if rok % 4 !=0:
           print("nieprzestępny")
    elif rok % 100 !=0:
            print ("przestępny")
    elif rok % 400 !=0:
            print ("nieprzestępny")
print ("koniec")    
    
               

