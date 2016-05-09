# Zadanie 2 lista 3

pesel = input("Podaj PESEL :")

pesel = pesel.strip()

# jeżeli PESEL nie ma 11 znaków lub nie są to cyfry 
if (len(pesel) != 11) or (pesel.isdigit != True):
    print("Nie podałeś prawidłowego numeru PESEL!")
else:
    # kod dla PESEL który ma 11 znaków i wszystkie są cyframi
    if int(pesel[-2]) % 2 == 0:
        print("Jesteś kobietą!")
    else:
        print("Jesteś mężczyzną!")

