# zad 2 i 3 i 4 lista 2
# SP Programiowaine komputerów ZUT
# programowanie obiektowe
# @ Tomasz Sobolewski
# zajęcia 20.02.2016 r.

# =================== TaxInfo, PitInfo, ZusInfo ==================

class TaxInfo:
    def __init__(self, konto, kwota):
        super().__init__()
        self.konto = konto
        self.kwota = kwota
        
    def kwotadozapłaty(self):
        return self.kwota
    
    def numerkonta(self):
        return str(self.konto)
    
class ZusInfo(TaxInfo):
    def rodzaj(self):
        return 'ZUS'

class PitInfo(TaxInfo):
    def rodzaj(self):
        return 'PIT'


#======================= Konto ============================

class Konto:
    def __init__(self, imię, nazwisko, stan):
        self.imię = imię
        self.nazwisko = nazwisko
        self.stan = stan
        pass

    def stankonta(self):
        print(self.nazwakonta, self.imię, self.nazwisko,\
              'Stan konta wynosi :',self.stan, 'zł.')
        pass
    
    def zapłać(self, ile):
        print('Płacę: ', ile, 'zł.')
        self.odejmij(ile)

    def dodaj(self, kwota):
        self.stan += kwota
        pass

    def odejmij(self, kwota):
        self.stan -= kwota
        pass

    def przelew(self, kontodocelowe, kwota):
        self.odejmij(kwota)
        kontodocelowe.dodaj(kwota)
        pass

    def zapiszdopliku(self):    # TODO
        pass

    def odczytzpliku(self):     # TODO
        pass

class KontoFirmowe(Konto): 
    def __init__(self,imię, nazwisko, stankonta, pit, zus):
        super().__init__(imię, nazwisko, stankonta)
        self.nazwakonta = 'Konto firmowe'
        self.pit = pit
        self.zus = zus
        

    def zapłaćpit(self):
        print('Płacę PIT',self.pit.kwota,'zł')
        self.stan -= self.pit.kwota
        pass

    def zapłaćzus(self):
        print('Płacę ZUS',self.zus.kwota,'zł')
        self.stan -= self.zus.kwota
        pass

class KontoPrywatne(Konto):
    def __init__(self,imię, nazwisko, stankonta):
        super().__init__(imię, nazwisko, stankonta)
        self.nazwakonta = 'Konto prywatne'
        pass

# ======== Konto obrotowe i oszczędnościowe ====================

class KontoObrotowe(Konto):
    pass

class KontoOszczędnościowe(Konto):
    pass

# =============== Klasa Osoba Pracownik Wypłata =================

class Wypłata:
    def __init__(self, kwota)
    pass

class Osoba:
    # wypłata
    pass

class Pracownik(Osoba):
    pass




# ========================== main ===============================
pitkonto = '50 1090 1362 0000 0000 3601 7904'
pitinfo = PitInfo(pitkonto, 200)
pitinfobig = PitInfo(pitkonto, 500)
zusinfo = ZusInfo('26 1050 1445 1000 0022 7647 0461', 1000)

##print(pitinfo.kwotadozapłaty())
##print(zusinfo.kwotadozapłaty())
##
##print(pitinfo.numerkonta())
##print(zusinfo.numerkonta())

x = []

x.append(KontoFirmowe('Jan','Kowalski',1000000, pitinfo, zusinfo))
x.append(KontoFirmowe('Andrzej','Nowak',1000000, pitinfobig, zusinfo))
x.append(KontoFirmowe('Maria','Konopnicka',1000000, pitinfo, zusinfo))

kontoA = x[0]
kontoB = x[1]
kontoC = x[2]

kontoA.stankonta()
kontoB.stankonta()

print('Robię przelew ...')
kontoA.przelew(kontoB, 5000)

kontoA.stankonta()
kontoB.stankonta()

'''
for el in x:
    print('=======================')
    el.stankonta()
    el.zapłaćpit()
    el.zapłaćzus()
    el.stankonta()


y = []

y.append(KontoPrywatne('Jan','Kowalski',1000000))
y.append(KontoPrywatne('Andrzej','Nowak',1000000))
y.append(KontoPrywatne('Maria','Konopnicka',1000000))

for el in y:
    print('=======================')
    el.stankonta()
    el.zapłać(555)
    el.stankonta()
'''
