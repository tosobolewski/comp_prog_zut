# zad 8 lista 1 programowanie obiektowe

'''
 Przygotować klasę reprezentującą planetę, atrybuty wydedukować z poniż-
szej tabeli:
(tabela w treści zadania)
'''

class Planet:

    AU = 149597870700 # au = astronomical unit [m]

    def __init__(self, name, distance, unit, isPlanet, note = None):

        if unit != 'au':
            return None
        
        self.name = name
        self.distance = float(distance)
        self.unit = unit
        self.isPlanet = None
        self.note = note

        if (isPlanet == True) or (isPlanet == False):
            self.isPlanet = isPlanet
        elif  isPlanet.lower() == 'true':
            self.isPlanet = True
        elif isPlanet.lower() == 'false':
            self.isPlanet = False
        elif isPlanet.lower() == 'false/true':
            self.isPlanet = False
        else:
            self.isPlanet = None
            

    def show(self, sep = '\t', unit = 'au'):
        print(self.getstr(sep, unit))

    def getlist(self, unit = 'au'):
        if (unit == 'tys.km') or (unit == 'tys. km'):
            _calcdistance = (self.AU / 1000000) * self.distance
            _calcdistance = round(_calcdistance, 2)
            _currentunit = 'tys.km'
        elif unit == 'au':
            _calcdistance = 1 * self.distance
            _currentunit = self.unit
        else:
            _calcdistance = 1 * self.distance
            _currentunit = self.unit
            pass
        return \
            [self.name, _calcdistance, _currentunit, self.isPlanet, self.note]

    def getstr(self, sep = ';', unit = 'au'):
        lst = self.getlist(unit)
        for i in range(len(lst)):
            lst[i] = str(lst[i])
        return sep.join(lst)    
        

def createPlanetObjBasedOnStr(inputstring, sep = ';'):
    el = inputstring.split(sep)
    if len(el) == 4:
        p = Planet(el[0], el[1], el[2], el[3])
        return p
    elif len(el) == 5:
        p = Planet(el[0], el[1], el[2], el[3], el[4])
        return p
    else:
        #print("Incorect number of arguments in a line: ",el)
        return None
    
def importPlanetsFromFileToList(fileName, lst):    
    file = open(fileName)
    try:
        filedata = file.read()
    finally:
        file.close()

    for el in filedata.split('\n'):
        p = createPlanetObjBasedOnStr(el, sep = ';')
        if p != None:
            lst.append(p)
            #print(p.getstr(';', 'au'))

def exportPlanetsFromListToFile(fileName, lst):  
    file = open(fileName,'w')
    try:
        for el in lst:
            #print(el.getstr(';', 'au'))
            file.write(el.getstr(';', 'au')+'\n')
    finally:
        file.close()

            
def main():
    
    # create list of planets
    planetlist = []

    # data definition
    initialdata =  ['Wulkan;0.03;au;false',
                    'Merkury;0.38;au;true',
                    'Wenus;0.72;au;true',
                    'Ziemia;1.0;au;true',
                    'Mars;1.52;au;true',
                    'Faeton;2.7;au;false',
                    'Jowisz;5.2;au;true',
                    'Saturn;9.53;au;true',
                    'Uran;19.19;au;true',
                    'Neptun;30.06;au;true',
                    'Pluton;39.48;au;false/true;Pluton is not Planet since 24/08/2006']

    # read from list and add each planet object to list
    for el in initialdata:
        p = createPlanetObjBasedOnStr(el, sep = ';')
        planetlist.append(p)
    print('== el.getlist() ==')
    for el in planetlist:
        print(el.getlist())
##    print('== el.show() ==')
##    for el in planetlist:
##        el.show()
        
    truePlanetList = []
    falsePlanetList = []
    for el in planetlist:
        if el.isPlanet == True:
            truePlanetList.append(el)
    for el in planetlist:
        if el.isPlanet != True:
            falsePlanetList.append(el)


    # show planets in units 'tys.km'
    print('\n======== True Planet list: ========')
    for el in truePlanetList:
        el.show(sep = '\t\t',unit = 'tys.km')

    print('\n======== False Planet list: ========')
    for el in falsePlanetList:
        el.show(sep = '\t\t',unit = 'tys.km')

    
    # write data to a file
    print('\n======== export Planets to file =========')
    exportPlanetsFromListToFile('planets_true.txt', truePlanetList)
    exportPlanetsFromListToFile('planets_false.txt', falsePlanetList)

    # import Planets from txt file
    print('\n======== import Planets from file =========')
    importPlanetList = []
    importPlanetsFromFileToList('planets_true.txt', importPlanetList)
    importPlanetsFromFileToList('planets_false.txt', importPlanetList)

    # show imported planets    
    print('\n======== Show imported objects: ========')
    for el in importPlanetList:
        el.show()

##    print('== importPlanetList[el] ==')
##    for el in importPlanetList:
##        print(el)
 

def test():
    return None

    print('I am in the test function now()!')
    
    p = Planet('Wulkan',0.03,'au',False)
    print(p.name)
    print(p.distance)
    print(p.isPlanet)
    print(p.note)
    
    p = Planet('Pluton','39.48','au','false/true','24/08/2006')
    print(p.name)
    print(p.distance)
    print(p.isPlanet)
    print(p.note)  

#
#   run (F5):
#

if __name__ == '__main__':
    test()
    main()
 
