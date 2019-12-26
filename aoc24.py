from collections import defaultdict
from copy import deepcopy

f = open('aoc24.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

# Build grid


game_state = []
for line in raw_input:
    current_line = []
    for letter in line:
        current_line += [letter]
    game_state += [current_line]
biodiversity = set()

def calc_biodiversity(game_state):
    biodiversity = 0
    for y in range(len(game_state)):
        current_line = game_state[y]
        width = len(current_line)
        for x in range(width):
            if game_state[y][x] == '#':
                biodiversity += (1 << (x + (width * y)))
    return biodiversity
def get_infected(neighbors):
    if neighbors <= 2 and neighbors > 0:
        return '#'
    else:
        return '.'
def die(neighbors):
    if neighbors != 1:
        return '.'
    else:
        return '#'
    
def evolve(game_state):
    height = len(game_state)
    width = len(game_state[0])
    new_state = []
    for line in game_state:
        new_state += [line[:]]
    
    for y in range(height):
        for x in range(width):
            neighbors = 0
            if x > 0:
                if game_state[y][x-1] == '#':
                    neighbors += 1
            if x <= width - 2:
                if game_state[y][x+1] == '#':
                    neighbors += 1
            if y > 0:
                if game_state[y-1][x] == '#':
                    neighbors += 1
            if y <= height - 2:
                if game_state[y+1][x] == '#':
                    neighbors += 1
            if game_state[y][x] == '#':
                temp = die(neighbors)
                new_state[y][x] = temp
            else:
                temp = get_infected(neighbors)
                new_state[y][x] = temp
    return new_state
   
    
        
    
    
biodiversity.add(calc_biodiversity(game_state))


while True:
    game_state = evolve(game_state)
    new_biodiversity = calc_biodiversity(game_state)
    if new_biodiversity in biodiversity:
        break
    else:
        biodiversity.add(new_biodiversity)
print('Part 1: ' + str(new_biodiversity))
# 33255350 too high
# 32776479

# Part 2
game_state = []
for line in raw_input:
    current_line = []
    for letter in line:
        current_line += [letter]
    game_state += [current_line]
def build_blank():
    blank_board = [['.','.','.','.','.'],
                   ['.','.','.','.','.'],
                   ['.','.','.','.','.'],
                   ['.','.','.','.','.'],
                   ['.','.','.','.','.']]
    return blank_board
game_board = defaultdict(build_blank)
game_board[0] = game_state

def part2_evolve(game_board, level):
    level_state = game_board[level]
    one_below = game_board[level + 1]
    one_above = game_board[level - 1]
    new_state = build_blank()
    for y in range(5):
        for x in range(5):
            my_neighbors = []
            # Top neighbor
            if x == 2 and y == 2:
                continue
            if y == 0:
                my_neighbors += one_above[1][2]
            elif y == 3 and x == 2:
                my_neighbors += one_below[4][0]
                my_neighbors += one_below[4][1]
                my_neighbors += one_below[4][2]
                my_neighbors += one_below[4][3]
                my_neighbors += one_below[4][4]
            else:
                my_neighbors += level_state[y-1][x]
            # Bottom neighbor
            if y == 4:
                my_neighbors += one_above[3][2]
            elif y == 1 and x == 2:
                my_neighbors += one_below[0][0]
                my_neighbors += one_below[0][1]
                my_neighbors += one_below[0][2]
                my_neighbors += one_below[0][3]
                my_neighbors += one_below[0][4]
            else:
                my_neighbors += level_state[y+1][x]
            # Left neighbor
            if x == 0:
                my_neighbors += one_above[2][1]
            elif x == 3 and y == 2:
                my_neighbors += one_below[0][4]
                my_neighbors += one_below[1][4]
                my_neighbors += one_below[2][4]
                my_neighbors += one_below[3][4]
                my_neighbors += one_below[4][4]
            else:
                my_neighbors += level_state[y][x-1]
            # Right neighbor
            if x == 4:
                my_neighbors += one_above[2][3]
            elif x == 1 and y == 2:
                my_neighbors += one_below[0][0]
                my_neighbors += one_below[1][0]
                my_neighbors += one_below[2][0]
                my_neighbors += one_below[3][0]
                my_neighbors += one_below[4][0]
            else:
                my_neighbors += level_state[y][x+1]
            neighbors = my_neighbors.count('#')
            if level_state[y][x] == '.':
                new_state[y][x] = get_infected(neighbors)
            else:
                new_state[y][x] = die(neighbors)

    return new_state
current_bugs = 0
for x in range(200):
    current_bugs = 0
    all_levels = game_board.keys()
    min_key = min(all_levels)
    max_key = max(all_levels)
    game_board[min_key - 1] = build_blank()
    game_board[max_key + 1] = build_blank()
    new_game_board = deepcopy(game_board)
    
    for item in game_board.keys():
        new_game_board[item] = part2_evolve(game_board, item)
        for row in new_game_board[item]:
            current_bugs += row.count('#')
    for item in game_board.keys():
        if item not in new_game_board:
            new_game_board[item] = deepcopy(game_board[item])
    game_board = new_game_board
print('Part 2: there are ' + str(current_bugs) + ' bugs.')
# 32039 too high
#3155 too high