import re
bingo_pattern_re = r"\d{1,2}"

tiles = []
random_numbers = None

tile_number = 0

class Tile:
    def __init__(self, tile_array, size = 5):
        self.tile_array = tile_array
        self.marks = [False] * size * size
        self.size = size
        self.bingoed = False
    
    def try_mark(self, number):
        if number in self.tile_array:
            self.marks[self.tile_array.index(number)] = True
            return True
        return False

    def check_bingo_columns(self):
        for column_index in range(self.size):
            column_indices = range(column_index, self.size ** 2, 5)
            mark_status = True
            for index in column_indices:
                mark_status = mark_status and self.marks[index]
            if mark_status:
                return True
        return False

    def check_bingo_rows(self):
        for row_index in range(self.size):
            row_indices = range((row_index * self.size),(row_index * self.size) + self.size)
            mark_status = True

            for index in row_indices:
                mark_status =  mark_status and self.marks[index]
            
            if mark_status:
                return True
        return False

    def check_bingo(self):
        if self.check_bingo_columns() or self.check_bingo_rows():
            self.bingoed = True
            return True
        return False
    
    def calculate_result(self):
        sum = 0
        for index in range(self.size ** 2):
            if not self.marks[index]:
                sum += int(self.tile_array[index])
        
        return sum

with open("input.txt") as fp: 
    random_numbers = fp.readline().strip().split(',')

    lines = []

    while True: 
        line = fp.readline()
        if not line: 
            break

        actual_line = line.strip()
        if not actual_line:
            tile_array = []
            for line in range(5):
                tile_array += re.findall(bingo_pattern_re, fp.readline().strip())
            tiles.append(Tile(tile_array))

done = False
number_of_bingos = 0
for number in random_numbers:
    if not done:
        for index, tile in enumerate(tiles):
            tile.try_mark(number)
            if not tile.bingoed and tile.check_bingo():
                number_of_bingos += 1
                if number_of_bingos == len(tiles):
                    print(int(number), tile.calculate_result())
                    print(int(number) * tile.calculate_result())
                    done=True
                    break