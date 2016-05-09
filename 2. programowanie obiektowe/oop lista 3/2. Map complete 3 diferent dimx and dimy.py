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
    
    def __init__(self, dimx, dimy):

        self.from_file = ''  # from file import
        self.map_array = [] # from file import
        
        self.dimx = dimx  # columns
        self.dimy = dimy  # rows      
        self.map = []
        self.players = []

        self.map = self.create_new_map(self.dimx, self.dimy)
        

    def create_new_map(self, dimx, dimy):
        
        _map = [[ 0 for el in range(dimx)] for el in range(dimy)]

        def _ustawpolaprzejściowe(): # '.'
            for col in range(self.dimx):
                for row in range(self.dimy):
                    _map[row][col] = Room(col, row, is_walk_through=True) 
                
        def _ustawpolanieprzejściowe():  # '#'
            for i in range(2*self.dimx): # 2 x więcej pól zakrytych niż wymiar mapy
                col = random.randint(0,dimx-1)
                row = random.randint(0,dimy-1)
                _map[row][col] = Room(col, row, is_walk_through=False)

        def _ustawprzedmioty():
            for col in range(dimx):
                for row in range(dimy):
                    if _map[row][col].jaki() == True: # jeżeli pokój przejściowy
                        r = random.randint(0,1)
                        if r == 1:
                            _map[row][col].przedmiot = Wartościowy()
                        else:
                            _map[row][col].przedmiot = Śmieć()
                            
        _ustawpolaprzejściowe()
        _ustawpolanieprzejściowe()
        _ustawprzedmioty()
        return _map

    def get_position(self, obj):
        return[obj.pos_x, obj.pos_y]
            
    def move_player(self, player, direction): # direction = 'up','down','left','right'
        p = get_position(player)
        pass
    
    def get_map():
        pass

    def add_player(self, player):
        self.players.append(player)

    def show(self):
        for el in self.map:
            for pok in el:
                if pok != 0:
                    print(pok.show(),end = ' ')            
            print()
            
    def import_map_from_file(self, file, allowable_chars='#.+opx'):
        # read file
        plik = open(file)
        try:
            self.from_file = plik.read()
        finally:
            plik.close()
            
        # convert text to array
        len_first_line = None
        for line in self.from_file.split('\n'):
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
    def __init__(self, pos_x, pos_y, is_walk_through, item = None):
        
        self.is_walk_through = is_walk_through       # blocked = False, walk through = True
        self.items = []        
        self.pos_x = pos_x
        self.pos_y = pos_y
        if item != None:
            self.items.append(item)
        
##        self.jestgracz = None   # ?

    def set_position(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def add_item(self, item):
        self.items.append(item)

    def jaki(self):
        return self.is_walk_through

    def show(self):
##        if self.jestgracz == True:
##            return 'G'
        
        if self.is_walk_through == True:
            if self.przedmiot.jaki == 'wartościowy':
                return '+'
            elif self.przedmiot.jaki == 'śmieć':
                return '.'
            else:
                return '?'
        else:
            return '#'
    


    
        
# ====================== main ===========================

m = Map(4,6)

m.show()
