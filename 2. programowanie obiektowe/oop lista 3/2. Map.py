# zad 2 lista 3

import random

# ========================== Player =========================
class Player:
    def __init__(self, pos_x, pos_y, name='No_name'):
        self.name = name
        self.items_count = {}
        self.items_list = []
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.map_char = 'G'
        self.moves = {'up': [0, -1], 'down': [0, 1],\
                      'left': [-1, 0], 'right': [1, 0],\
                      'u': [0, -1], 'd': [0, 1],\
                      'l': [-1, 0], 'r': [1, 0]
                      }  # {direction: [x][y]}

    def show_items(self):
        for el in self.items_list:
            print(el)
        print()

    def add_item(self, item):
        self.items_list.append(item)
        self.items_counter()

    def items_counter(self):
        ic = {}
        for i in self.items_list:
            if isinstance(i, Item):
                k = i.name
                v = 1
                if k in ic:
                    v = ic[k]+1
                else:
                    v = 1
                ic[k] = v
        self.items_count = ic
        return ic

#=========================== Map ===========================


class Map:

    def __init__(self, dimx=None, dimy=None):

        self.rooms = []
        self.player = None
        self.dimx = dimx  # columns
        self.dimy = dimy  # rows
        self.items_count = {}     # item counters

    def validate_position(self, pos):
        row = pos[1]  # y
        col = pos[0]  # x
        if (row < 0) or (row >= self.dimy):
            return False
        if (col < 0) or (col >= self.dimx):
            return False
        if isinstance(self.rooms[row][col], RoomWalkBlocked):
            return False
        return True
            
    def move_player(self, player, direction): # direction = 'up','down','left','right'
        p_x = player.pos_x
        p_y = player.pos_y
        move = player.moves[direction]
        pos_new = [p_x + move[0], p_y + move[1]]
        if self.validate_position(pos_new):
            self.rooms[p_y][p_x].player = False
            player.pos_x = pos_new[0]
            player.pos_y = pos_new[1]
            self.rooms[player.pos_y][player.pos_x].player = player
            return True
        else:
            return None
        
    def move_item(self, player):
        px = player.pos_x
        py = player.pos_y
        if isinstance(self.rooms[py][px].item, Item):
            i = self.rooms[py][px].item
            self.player.add_item(i)
            self.rooms[py][px].item = None

    def items_counter(self):
        ic = {}
        for row in self.rooms:
            for room in row:
                if isinstance(room.item, Item):
                    k = room.item.name
                    v = 1
                    if k in ic:
                        v = ic[k]+1
                    else:
                        v = 1
                    ic[k] = v
        self.items_count = ic
        return ic
        
    def show(self):
        for row in self.rooms:
            for room in row:
                if isinstance(room, Room):
                    print(room.get_map_char(),end = ' ')            
            print()

#=========================== MapCreator ===========================                   
class MapCreator:
    def __init__(self, dimx=20, dimy=20, file=None, allowable_chars='#.+opx'):
        self.map = Map()
        self.map.dimx = dimx
        self.map.dimy = dimy
        self._from_file = []    # array imported from file      
        if file is not None:
            self.import_map_from_file(file, allowable_chars)
        else:
            if dimx > 4 and dimy > 4:
                self.create_random_map()
            else:
                print('map dimensions are too small')
           
    def create_random_map(self):
        dimx = self.map.dimx
        dimy = self.map.dimy
        _rooms = [[ 0 for el in range(dimx)] for el in range(dimy)]

        def _set_walk_through_rooms(): # '.'
            for col in range(dimx):
                for row in range(dimy):
                    _rooms[row][col] = RoomWalkThrough()
                
        def _set_blocked_rooms():  # '#'
            for i in range(2*dimx): # 2 x więcej pól zakrytych niż wymiar mapy
                col = random.randint(0,dimx-1)
                row = random.randint(0,dimy-1)
                _rooms[row][col] = RoomWalkBlocked()

        def _set_items():
            for col in range(dimx):
                for row in range(dimy):
                    if _rooms[row][col].is_walk_through == True: # jeżeli pokój przejściowy
                        prc = random.randint(1,100)
                        if prc > 50:                      # ca p=50% rooms has got items 
                            r = random.randint(0,1)
                            if r == 1:
                                _rooms[row][col].item = ItemValuable()
                            else:
                                _rooms[row][col].item = ItemJunk()

        def _set_player():
            i = 0
            while True:
                px = random.randint(0,dimx-1)
                py = random.randint(0,dimy-1)
                r = _rooms[py][px]
                if not (isinstance(r, RoomWalkBlocked) or\
                        isinstance(r.item, (ItemValuable, ItemJunk))):
                    break
                i += 1
                if i > 100:
                    print('_set_player(): too many attempts')
                    break
            self.map.player = Player(px, py)
            _rooms[py][px].player = self.map.player
            print("player position: ", px, py)
            
            
                            
        _set_walk_through_rooms()
        _set_blocked_rooms()
        _set_items()
        _set_player()
        
        self.map.rooms = _rooms
        self.map.items_counter()

    def import_map_from_file(self, file, allowable_chars='#.+opx'):

        file_content = ''

        # read file
        plik = open(file)
        try:
            file_content = plik.read()
            print(file_content)
        finally:
            plik.close()
            
        # convert file to array
        len_first_line = None
        for line in file_content.split('\n'):
            templine = line
            if (templine.strip(allowable_chars)) is not '':  # check allowable characters
                self._from_file = []
                print('prohibited characters in file', list(templine))
                return None
            if len(line) == 0:
                continue           
            if len_first_line is None:
                len_first_line = len(line)    # first not empty line is constant width of array          
            if len_first_line != len(line):   # stop conversion if current len(line) 
                break                         # is not equal width of array (len_first_line)          
            else:
                self._from_file.append(list(line))

        # convert char array to objects array
        m = self._from_file
        if len(m) > 4:
            for row in range(len_first_line):
                for col in range(len(self._from_file)):
                    c = self._from_file[row][col]
                    if c == '#':
                        m[row][col] = RoomWalkBlocked()
                    elif c == '.':
                        m[row][col] = RoomWalkThrough()
                    elif c == 'o':
                        m[row][col] = RoomWalkThrough(item = ItemValuable())
                    elif c == 'x':
                        m[row][col] = RoomWalkThrough(item = ItemJunk())
                    elif c == 'p':
                        self.map.player = Player(col, row)
                        m[row][col] = RoomWalkThrough(player = self.map.player)
                    else:
                        pass
                                              
            self.map.dimy = len(m)
            self.map.dimx = len(m[-1])
            self.map.rooms = m        
        else:
             self.map.rooms = []     # when failure in creating map from file
        self.map.items_counter()

# ========================== Items =========================
class Item:
    def __init__(self, name = 'no_name'):
        self.name = name
        self.map_char = ' '     # one space
        
    def get_map_char(self):
        return self.map_char

class ItemValuable(Item):
    def __init__(self):
        super().__init__(name='Valuable')
        self.map_char = '+'

class ItemJunk(Item):
    def __init__(self):
        super().__init__(name = 'Junk')
        self.map_char = 'x'

# ============================= Room ===========================
class Room():
    def __init__(self, player = False, item = None):        
        self.item = item
        self.player = player
                
    def spend_item(self):
        if self.item != None:
            _item = self.item
            self.item = None
            return _item

    def get_map_char(self):
        if isinstance(self.player, Player):
            return self.player.map_char
        if isinstance(self.item, Item):
            return self.item.map_char
        else:
            return self.map_char

class RoomWalkThrough(Room):
    def __init__(self, player = False, item = None):
        super().__init__(player, item)
        self.is_walk_through = True
        self.map_char = '.'

class RoomWalkBlocked(Room):
    def __init__(self, player = False, item = None):
        super().__init__(player, item)
        self.is_walk_through = False
        self.map_char = '#'

             
# ====================== main ===========================

##mc = MapCreator(40,20);
##mapa = mc.map
##mapa.show()

mc = MapCreator(file='Game/map1.txt')
gamemap = mc.map
player = gamemap.player

game_over = False
while game_over == False:
    gamemap.show()
    print('Player: ',player.items_counter())
    print('Map   : ',gamemap.items_counter())
    
    direction = input('Podaj kierunek ruchu gracza:')
    di = direction
    dir_list = []
    
    if di.strip('udlr') == '': # (u)p, (d)own, (l)eft, (r)ight
        dir_list = list(direction)
    else:
        dir_list = [direction]
        
    for dir_ in dir_list:
        if dir_ in player.moves:
            if gamemap.move_player(player, dir_):
                gamemap.move_item(player)
                gamemap.items_counter()
                if not ('Valuable' in gamemap.items_count):
                    gamemap.show()
                    game_over = True    # game over
                    print('Player: ',player.items_counter())
                    print('Map   : ',gamemap.items_counter())
                    print('GAME OVER')                   
                    break
                
    if direction == '0':
        print('GAME OVER')
        break
    


