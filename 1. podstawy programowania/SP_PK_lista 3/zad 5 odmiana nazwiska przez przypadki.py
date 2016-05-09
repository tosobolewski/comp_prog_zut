#Zadanie 5 lista 3

nazwisko = input("Podaj nazwisko : ")
nazwisko = nazwisko.capitalize()

lista_przypadkow = [

'Mianownik      M.      Kto? Co?                     :   ',
'Dopełniacz     D.      Kogo? Czego? (nie ma)        :   ', 
'Celownik       C.      Komu? Czemu? (się przyglądam):   ',	
'Biernik        B.      Kogo? Co? (widzę)            :   ',
'Narzędnik      N.      (Z) kim? (Z) czym? (idę)     :   ',
'Miejscownik    Ms.      O kim? O czym? (mówię)      :   ',
'Wołacz W.      zwrot do kogoś lub czegoś            :   ',]

                    

lista_koncówek_1 = ['ski', 'skiego', 'skiemu', 'skiego', 'skim', 'skim', 'ski']
lista_koncówek_2 = ['ska', 'skiej', 'skiej', 'ską', 'ską', 'skiej', 'ska']



if not (nazwisko.endswith("ski") or nazwisko.endswith("ska")):
    print("Niestety w tym przypadku nie mogę Ci pomóc!")
else:
    if nazwisko.endswith('ski'):
        baza = nazwisko.rstrip("ski")
        for i in range(len(lista_przypadkow)):
            print(lista_przypadkow[i], baza, lista_koncówek_1[i], sep='', end='\n' )
    else:
        if nazwisko.endswith("ska"):
            baza = nazwisko.rstrip("ska")
            for i in range(len(lista_przypadkow)):
                print(lista_przypadkow[i], baza, lista_koncówek_2[i], sep='' )

    

        
