# zad 2 lista 3

import random

# ========================== Player =========================
class Player:
    def __init__(self, pos_x, pos_y):
        self.items_list = []
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.map = None

    def up(self):
        self.pos_x = x - 1
        self.pos_y = y

    def down(self):
        self.pos_x = x + 1
        self.pos_y = y

    def left(self):
        self.pos_x = x
        self.pos_y = y - 1

    def right(self):
        self.pos_x = x
        self.pos_y = y + 1

    def set_player_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_player_position(self):
        return [self.pos_x, self.pos_y]

    def show_items(self):
        for el in self.items_list:
            print(el)
        print()


#=========================== Map ===========================
class Map():
    
    def __init__(self, wymiar):

        self._map_txt = ''  # from file import
        self.map_array = [] # from file import
        
        self.wymiar = wymiar
        self.plan = \
            [[ 0 for el in range(wymiar)] for el in range(wymiar)]

        self.players = []
        
        self.ustawpolaprzejściowe()
        self.ustawpolanieprzejściowe()
        self.ustawprzedmioty()

    def add_player(self, player):
        self.players.append(player)

    def show(self):
        for el in self.plan:
            for pok in el:
                if pok != 0:
                    print(pok.show(),end = ' ')
            
            print()
            
    def ustawpolaprzejściowe(self):
        for i in range(self.wymiar):
            for j in range(self.wymiar):
                self.plan[i][j] = Room(True, i, j) 

    def ustawpolanieprzejściowe(self):
        for i in range(2*self.wymiar): # 2 x więcej pól zakrytych niż wymiar mapy
            x = random.randint(0,self.wymiar-1)
            y = random.randint(0,self.wymiar-1)
            self.plan[x][y] = Room(False, x, y)

    def ustawprzedmioty(self):
        for i in range(self.wymiar):
            for j in range(self.wymiar):
                if self.plan[i][j].jaki() == True: # jeżeli pokój przejściowy
                    r = random.randint(0,1)
                    if r == 1:
                        self.plan[i][j].przedmiot = Wartościowy()
                    else:
                        self.plan[i][j].przedmiot = Śmieć()
                        
                       
        
##        jaki = random.randint(0,1)  # ?

    def import_map_from_file(self, file, allowable_chars='#.+opx'):
        # read file
        plik = open(file)
        try:
            self._map_txt = plik.read()
        finally:
            plik.close()
            
        # convert text to array
        len_first_line = None
        for line in self._map_txt.split('\n'):
            templine = line
            if (templine.strip(allowable_chars)) is not '':  # check allowable characters
                self.map_array = []
                return None
            if len(line) == 0:
                continue           
            if len_first_line is None:
                len_first_line = len(line)    # first not empty line is constant width of array          
            if len_first_line != len(line):   # if current len(line) is equal width of array           
                break
            else:
                self.map_array.append(list(line))
        return None


    def change_char_to_objects(self):
        pass
        
        

# ========================== Przedmiot =========================
class Przedmiot:
    def __init__(self,wartośćprzedmiotu, nazwa = ''):
        self.nazwa = nazwa
        self.wartośćprzedmiotu = wartośćprzedmiotu # 1/0 = wartościowy, smieć


class Wartościowy(Przedmiot):
    def __init__(self):
        self.jaki = 'wartościowy'
        self.map_char = '+'

    def show(self):
        return self.map_char


class Śmieć(Przedmiot):
    def __init__(self):
        self.jaki = 'śmieć'
        self.map_char = '.'

    def show(self):
        return self.map_char


# ============================= Room ===========================
class Room():
    def __init__(self, pos_x, pos_y, room_type, item = None):
        
        self.room_type = room_type       # blocked = False, full walk = True
        self.items = []
        self.items.append(item)
        self.pos_x = pos_x
        self.pos_y = pos_y
##        self.jestgracz = None   # ?

    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def add_item(self, item):
        self.items.append(item)

    def jaki(self):
        return self.room_type

    def show(self):
##        if self.jestgracz == True:
##            return 'G'
        
        if self.room_type == True:
            if self.przedmiot.jaki == 'wartościowy':
                return '+'
            elif self.przedmiot.jaki == 'śmieć':
                return '.'
            else:
                return '?'
        else:
            return '#'
    


    
        
# ====================== main ===========================

m = Map(20)

m.show()
