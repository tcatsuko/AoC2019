import networkx as nx
import string
from copy import deepcopy
from collections import deque

f = open('aoc18_2.txt','r')
single_robot = False

raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
clean_graph = nx.Graph()
# Build graph (x,y) tuples
start_positions = [(0,0),(0,0),(0,0),(0,0)]
key_positions = {}
door_positions = {}

def travel_to_nodes(raw_input, start_pos):
    x = start_pos[0]
    y = start_pos[1]
    clean_move = []
    if raw_input[y][x-1] != '#':
        clean_move += [(x-1,y)]
    if raw_input[y][x+1] != '#':
        clean_move += [(x+1,y)]
    if raw_input[y-1][x] != '#':
        clean_move += [(x,y-1)]
    if raw_input[y+1][x] != '#':
        clean_move += [(x,y+1)]
        
    dirty_move = []
    if raw_input[y][x] not in list(string.ascii_uppercase):
        for item in clean_move:
            if raw_input[item[1]][item[0]] not in string.ascii_uppercase:
                dirty_move += [item]
    return[clean_move, dirty_move]



for y in range(1,len(raw_input)-1):
    for x in range(1, len(raw_input[0])-1):
        #Determine type of tile
        current_tile = raw_input[y][x]
        if raw_input[y][x] == '#':
            # It's a wall.
            continue
        elif raw_input[y][x] == '@':
            start_positions[0] = (x,y)
            single_robot = True
        elif raw_input[y][x] == '1':
            start_positions[0] = (x,y)
            single_robot = False
        elif raw_input[y][x] == '2':
            start_positions[1] = (x,y)
        elif raw_input[y][x] == '3':
            start_positions[2] = (x,y)
        elif raw_input[y][x] == '4':
            start_positions[3] = (x,y)
        # we know it's possible to move to this space
        if current_tile in list(string.ascii_uppercase):
            door_positions[current_tile] = (x,y)
        elif current_tile in list(string.ascii_lowercase):
            key_positions[current_tile] = (x,y)
        clean, dirty = travel_to_nodes(raw_input, (x,y))
        for item in clean:
            clean_graph.add_edge(item, (x,y))


# Build a cached list of routes between each key
def find_doors_on_route(path, raw_input):
    doors = []
    for node in path:
        x = node[0]
        y = node[1]
        if raw_input[y][x] in string.ascii_uppercase:
            doors += raw_input[y][x]
    return doors
def find_keys_on_route(path, raw_input):
    keys = []
    new_path = path[:]
    del new_path[0]
    del new_path[-1]
    for node in path:
        x = node[0]
        y = node[1]
        if raw_input[y][x] in string.ascii_lowercase:
            keys += raw_input[y][x]
    return keys

key_routes = {}
for key in key_positions:
    routes = {}
    for other_key in key_positions:
        short_route = {}
        if other_key == key:
            continue
        if not nx.has_path(clean_graph, key_positions[key], key_positions[other_key]):
            continue
        path = nx.shortest_path(clean_graph, key_positions[key], key_positions[other_key])
        doors = find_doors_on_route(path, raw_input)
        short_route['distance'] = len(path) - 1
        short_route['doors'] = doors
        routes[other_key] = short_route
    key_routes[key] = routes

# Now do BFS starting at start position.  Assume you can get at least one key without going through a door

lookup_table = {}
for key in key_positions:
    lookup_table[key] = {}

all_keys = key_positions.keys()
all_keys.sort()
first_key = '@'

if single_robot == True:
    loops = 1
    node_names = ['@']
else:
    loops = 4
    node_names = ['1','2','3','4']
for name in node_names:
    lookup_table[name] = {}
for i in range(loops): 
    start_node = node_names[i]
    start_position = start_positions[i]
    for key in all_keys:
        
        if not nx.has_path(clean_graph, start_position, key_positions[key]):
            continue
        lookup_table[start_node][key] = {}
        path = nx.shortest_path(clean_graph,start_position, key_positions[key])
        doors = find_doors_on_route(path, raw_input)
        keys = find_keys_on_route(path, raw_input)
        keystring = ''.join(keys)
        keystring = keystring.replace(key, '')
        keys_set = set()
        for item in keys:
            keys_set.add(item)
        path_length = len(path) - 1
        lookup_table[start_node][key] = (path_length, ''.join(doors) + keystring)


    
for first_key in all_keys:
    for key in all_keys:
        if key == first_key:
            continue
        if not nx.has_path(clean_graph, key_positions[first_key], key_positions[key]):
            continue
        path = nx.shortest_path(clean_graph, key_positions[first_key], key_positions[key])
        doors = find_doors_on_route(path, raw_input)
        keys = find_keys_on_route(path, raw_input)
        path_length = len(path) - 1
        
        doors_set = set()
        for item in doors:
            doors_set.add(item)
        keys_set = set()
        for item in keys:
            keys_set.add(item)
        keystring = ''.join(keys)
        keystring = keystring.replace(key, '')
        lookup_table[first_key][key] = (path_length, ''.join(doors) + keystring)


if single_robot == True:
    info = {(('@'), frozenset()):0}
else:
    info = {(('1','2','3','4'),frozenset()):0}
keys = ''.join(lookup_table.keys())
keys = keys.replace('@','')

for _ in range(len(lookup_table) - loops):
    new_info = {}
    for item in info:
        location = item[0]
        found_keys = item[1]
        current_distance = info[item]
        for next_key in keys:
            if next_key not in found_keys:
                for robot in range(loops):
                    test1 = location[robot]
                    if next_key in lookup_table[location[robot]]:
                        lookup_value = lookup_table[location[robot]][next_key]
                        distance = lookup_value[0]
                        on_route = lookup_value[1]
                        #distance, on_route = lookup_table[location[robot]][next_key]
                        is_reachable = all((c in found_keys or c.lower() in found_keys) for c in on_route)
                        
                        if is_reachable:
                            new_distance = current_distance + distance
                            new_keys = frozenset(found_keys | set((next_key,)))
                            
                            next_keys = list(location)
                            next_keys[robot] = next_key
                            next_keys = tuple(next_keys)
                            if (next_keys, new_keys) not in  new_info or new_distance < new_info[(next_keys, new_keys)]:
                                new_info[(next_keys, new_keys)] = new_distance
    info = new_info
print('shortest route is ' + str(min(info.values())))
    

            
    

        
        
        
    

            