# zad 8 lista 1 programowanie obiektowe

'''
Przygotować klasę udostępniająca metody konwersji jednostek.
a) cali na cm,
b) cm na cale,
kg na lbs(funty),
d) lbs na kg.
'''

class UnitConverter:

    # conv = {unit_in : {unit_out1 : factor1, unit_out2 : factor2, unit_out3: factor3}}
    factor = {'cal':  {'cm': 2.54},
              'cm':   {'cal': 1/2.54},
              'kg':   {'lbs': 1/0.45359237},
              'lbs':  {'kg': 0.45359237}
             }
    units = ['cal','cm','kg','lbs']

    def convert(self, unit_in, unit_out, value, precision = 2):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()
        
        try:
            calc = self.factor[unit_in][unit_out] * float(value)
        except:
            return None

        calc = round(calc, precision)
        return calc
        
    def show(self, unit_in, unit_out, value, precision = 2):

        calc = self.convert(unit_in, unit_out, value, precision)
        if calc != None:
            print(value, unit_in,' = ', calc, unit_out)
        else:
            self.show_acceptable_conversions()  # czy w tym miejscu wydruk komunikatu ?

    def show_acceptable_conversions(self):

        units = self.units
        factor = self.factor
        #print('Dopuszczalne przeliczenia: cal<->cm, kg<->lbs(funt)')
        print('Acceptable conversions:', end = '')
        sep = ''
        separator = ','
        for u in units:
            if u in factor:
                for u2 in units:
                    if u2 in factor[u]:

                        print(sep, u,'->',u2, end='')
                        if sep == '':
                            sep = separator + ' '
        print('.\n')
            
def test():

    sep = '---------------------------------------------------'
    print(sep)
    
    uc = UnitConverter()
    
    print('Teraz test metody .convert():')
    print(uc.convert('cal', 'cm', 1, 5))
    print(uc.convert('cm', 'cal', 1, 9))
    print(uc.convert('kg', 'lbs', 1, 8))
    print(uc.convert('lbs', 'kg', 1, 8))
    print(sep)
    
    print('Teraz test metody .show():')
    uc.show('lbs', 'kg', 1, 8)
    uc.show('kg', 'lbs', 1, 8)
    uc.show('cm', 'cal', 1, 9)
    uc.show('cal', 'cm', 1, 5)
    print(sep)
    
    print('Teraz test metody .show_acceptable_conversions():\n')
    uc.show_acceptable_conversions()
    print(sep)

    print('Teraz test z niepoprawnymi danymi:\n')
    print('a')
    x = uc.convert('lbs', 'tona', 1, 5)
    print(x)
    print('b')
    uc.show('cal', 'metr', 1, 5)
    print(sep)
    pass        

def main():
    
    print('Teraz jestem w funkcji main()!\n')

    
#
#   run (F5):
#

if __name__ == '__main__':
    test()
    main()
