from numpy import intersect1d
f = open('aoc03.txt','r')
input_file = []
for line in f:
    input_file += [line]
f.close()

wire_1_raw = input_file[0][:-1]
wire_2_raw = input_file[1][:-1]

# Parse wire 1
wire_1 = wire_1_raw.split(',')
wire_2 = wire_2_raw.split(',')
wire_1_locations = []
wire_2_locations = []
wire_1_locations += [(0,0)]
wire_2_locations += [(0,0)]
shortest_distance = 999999999999999999999999999999999
for move in wire_1:
    current_pos = wire_1_locations[-1]
    direction = move[0]
    distance = int(move[1:])
    if direction == 'U':
        for count in range(distance):
            new_pos = (current_pos[0], current_pos[1] + 1)
            wire_1_locations += [new_pos]
            current_pos = new_pos
    elif direction == 'L':
        for count in range(distance):
            new_pos = (current_pos[0] - 1, current_pos[1])
            wire_1_locations  += [new_pos]
            current_pos = new_pos
    elif direction == 'D':
        for count in range(distance):
            new_pos = (current_pos[0], current_pos[1] - 1)
            wire_1_locations += [new_pos]
            current_pos = new_pos
    elif direction == 'R':
        for count in range(distance):
            new_pos = (current_pos[0] + 1, current_pos[1])
            wire_1_locations += [new_pos]
            current_pos = new_pos
            
current_pos = (0,0)
intersections = []
for move in wire_2:
    current_pos = wire_2_locations[-1]
    direction = move[0]
    distance = int(move[1:])
    if direction == 'U':
        for count in range(distance):
            new_pos = (current_pos[0], current_pos[1] + 1)
            wire_2_locations += [new_pos]
            current_pos = new_pos
    elif direction == 'L':
        for count in range(distance):
            new_pos = (current_pos[0] - 1, current_pos[1])
            wire_2_locations  += [new_pos]
            current_pos = new_pos
    elif direction == 'D':
        for count in range(distance):
            new_pos = (current_pos[0], current_pos[1] - 1)
            wire_2_locations += [new_pos]
            current_pos = new_pos
    elif direction == 'R':
        for count in range(distance):
            new_pos = (current_pos[0] + 1, current_pos[1])
            wire_2_locations += [new_pos]
            current_pos = new_pos


        

intersections = list(set(wire_1_locations).intersection(wire_2_locations))
for item in intersections:
    int_distance = abs(item[0]) + abs(item[1])
    if int_distance < shortest_distance and int_distance > 0:
        shortest_distance = int_distance

print('Part 1: shortest distance to intersection is ' + str(shortest_distance))
# part 2
shortest_hop = 99999999999999999999999999999999999999999999999999999999999999
for item in intersections:
    hop_size = wire_1_locations.index(item) + wire_2_locations.index(item)
    if hop_size < shortest_hop and hop_size > 0:
        shortest_hop = hop_size
print('Part 2: shortest distance is ' + str(shortest_hop))