# lista 3 zad 3

class CKomentarz:
    def __init__(self, komentarz, użytkownik):
        self.komentarz = komentarz
        self.użytkownik = użytkownik
        pass

    def pokaż(self):
        print(self.użytkownik.imię, self.użytkownik.nazwisko,\
              '<' + self.użytkownik.status + '>')
        print(self.komentarz)
        print()
        pass

    def zmień(self,nowykomentarz, użytkownik):
        print('===================== zmiana komentarza =======================')
        if użytkownik.status == 'Administrator':
            self.komentarz = nowykomentarz
            print('Zmiana komentarza przebiegła pomyślnie')
            self.pokaż()
        else:
            print('Nie masz uprawnień do zmiany komentarzy!')
            print()

class Uzytkownik:
    def __init__(self, imię, nazwisko, login):
        self.imię = imię
        self.nazwisko = nazwisko
        self.login = login
        
    pass

class ZwykłyUżytkownik(Uzytkownik):
    def __init__(self, imię, nazwisko, login):
        super().__init__(imię, nazwisko, login)
        self.status = 'Użytkownik'
        pass

class Administrator(Uzytkownik):
    def __init__(self, imię, nazwisko, login):
        super().__init__(imię, nazwisko, login)
        self.status = 'Administrator'
        pass

def pokażKomentarze(lista):
    print('============== Wyśwwietlam listę wszystkich komentarzy =================')
    print()
    for el in lista:
        el.pokaż()

users = [Administrator("Tomasz","Sobolewski","tsob"),\
         ZwykłyUżytkownik("Grzegorz","Lewandowski","glew"),
         ZwykłyUżytkownik("Mariusz","Niedźwiedzki","mnie"),
         ZwykłyUżytkownik("Janusz","Piłka","jpil")]


listakomentarzy = [\
    CKomentarz('Transakcja przebiegła pomyślnie. Polecam.',users[0]),\
    CKomentarz('Szybko sprawnie bez problemu ! Polecam tego sprzedawce !',users[1]),\
    CKomentarz('Polecam allegrowicza!',users[2]),\
    CKomentarz('Allegrowicz zasługuje na świąteczną gwiazdkę. Polecam i życzę wesołych!',users[3]),\
    CKomentarz('Bardzo rzetelny sprzedawca.Wszystko w jak najlepszym porzadku.',users[2]),\
    CKomentarz('OSZUST! Kupiłem nowego iPhona 6 a w paczce dostałem ZIEMNIAKA !!!!',users[3])\
    ]


pokażKomentarze(listakomentarzy)

listakomentarzy[2].zmień('Komentarz usunięty', users[2])
listakomentarzy[5].zmień('Komentarz usunięty', users[0])

pokażKomentarze(listakomentarzy)

