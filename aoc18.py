import networkx as nx
import string
from copy import deepcopy

f = open('aoc18.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
clean_graph = nx.Graph()
edited_graph = nx.Graph()
# Build graph (x,y) tuples
start_position = (0,0)
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
            start_position = (x,y)
        # we know it's possible to move to this space
        if current_tile in list(string.ascii_uppercase):
            door_positions[current_tile] = (x,y)
        elif current_tile in list(string.ascii_lowercase):
            key_positions[current_tile] = (x,y)
        clean, dirty = travel_to_nodes(raw_input, (x,y))
        for item in clean:
            clean_graph.add_edge(item, (x,y))
        for item in dirty:
            edited_graph.add_edge(item, (x,y))

# Build a cached list of routes between each key
def find_doors_on_route(path, raw_input):
    doors = []
    for node in path:
        x = node[0]
        y = node[1]
        if raw_input[y][x] in string.ascii_uppercase:
            doors += raw_input[y][x]
    return doors
            
key_routes = {}
for key in key_positions:
    routes = {}
    for other_key in key_positions:
        short_route = {}
        if other_key == key:
            continue
        path = nx.shortest_path(clean_graph, key_positions[key], key_positions[other_key])
        doors = find_doors_on_route(path, raw_input)
        short_route['distance'] = len(path) - 1
        short_route['doors'] = doors
        routes[other_key] = short_route
    key_routes[key] = routes

# Now do BFS starting at start position.  Assume you can get at least one key without going through a door
def search(keys_found, position, distance):
    global key_positions
    global raw_data
    global clean_graph
    global distances
    global shortest_distance
    valid_paths = {}
    for key in key_positions:
        if key in keys_found:
            continue
        path = nx.shortest_path(clean_graph, position, key_positions[key])
        doors = find_doors_on_route(path, raw_input)
        doors_copy = doors[:]
        for door in doors:
            if string.lower(door) in keys_found:
                doors_copy.remove(door)
        if len(doors_copy) == 0:
            valid_paths[key] = path
    if len(valid_paths) == 0 and len(keys_found) == len(key_positions):
        if distance == 62:
            print()
        if distance < shortest_distance:
            shortest_distance = distance
        return
    for path in valid_paths:
        new_position = key_positions[path]
        new_keys_found = keys_found[:]
        new_keys_found += path
        new_distance = distance + len(valid_paths[path]) - 1
        search(new_keys_found, new_position, new_distance)
lookup_table = {}
for key in key_positions:
    new_dictionary = {}
    for second_key in key_positions:
        if second_key == key:
            continue
        new_dictionary[second_key] = {}
    lookup_table[key] = new_dictionary

all_keys = key_positions.keys()
all_keys.sort()
first_key = '@'
lookup_table['@'] = {}
for key in all_keys:
    lookup_table['@'][key] = {}
    path = nx.shortest_path(clean_graph,start_position, key_positions[key])
    doors = find_doors_on_route(path, raw_input)
    path_length = len(path) - 1
    lookup_table['@'][key]['distance'] = path_length
    doors_set = set()
    for item in doors:
        doors_set.add(item.lower())
    lookup_table['@'][key]['doors'] = doors_set
    
while all_keys:
    first_key = all_keys[0]
    for key in all_keys:
        if key == first_key:
            continue
        path = nx.shortest_path(clean_graph, key_positions[first_key], key_positions[key])
        doors = find_doors_on_route(path, raw_input)
        path_length = len(path) - 1
        lookup_table[first_key][key]['distance'] = path_length
        lookup_table[key][first_key]['distance'] = path_length
        doors_set = set()
        for item in doors:
            doors_set.add(item.lower())
        lookup_table[first_key][key]['doors'] = doors_set
        lookup_table[key][first_key]['doors'] = doors_set
    del all_keys[0]


distances = []
shortest_distance = 999999999999999999999999999999999999999999999999999999
def filter_paths(paths, keyset):
    data_to_return = {}
    
    
    for k,v in paths.items():
        if v['doors'].issubset(keyset):
            data_to_return[k] = v
    return data_to_return
            

def lookup_search(keys_found, position, distance):
    global key_positions
    global raw_data
    global clean_graph
    global distances
    global shortest_distance
    global lookup_table
    # First find where we can go based on current key
    # Also determine if we are at the start
    current_lookup_branch = lookup_table[position]
    current_keys_found = keys_found.copy()
    if position != '@':
        current_keys_found.add(position)
    possible_paths = 0
    next_position_keys = []
    for item in current_lookup_branch.keys():
        if item in current_keys_found:
            continue
        doors = current_lookup_branch[item]['doors']
        if current_lookup_branch[item]['doors'].issubset(current_keys_found):
            next_position_keys += item
        
    for item in keys_found:
        if item in next_position_keys:
            next_position_keys.remove(item)
    if len(next_position_keys) == 0:
        if distance < shortest_distance:
            shortest_distance = distance
        return
    for item in next_position_keys:
        lookup_search(current_keys_found, item, distance + current_lookup_branch[item]['distance'])
        
        
    

        
            
keys_found = []
position = start_position
distance = 0

lookup_search(set(), '@', distance)
#search(keys_found, start_position, distance)
#minimum_steps = min(distances)
print('Part 1: minimum of '+ str(shortest_distance))
            