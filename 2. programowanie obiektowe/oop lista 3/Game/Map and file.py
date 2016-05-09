# import game map from file

class Map:
    def __init__(self):
        self._map_txt = ''
        self.map_array = []
        
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

m = Map()
t = m.import_map_from_file('map1.txt')

print(m._map_txt)
print(m.map_array)
