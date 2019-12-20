import networkx as nx
import string

f = open('aoc20.txt','r')

part2 = True

raw_data = []
for line in f:
    raw_data += [line[:-1]]
f.close()
portals = {}
x = 0
y = 0
G = nx.Graph()
if part2 == False:
    levels = 1
else:
    levels = 50
def search_edges(position):
    global portals
    global G
    global raw_data
    second_left_position = (position[0]-2, position[1])
    left_position = (position[0]-1, position[1])
    right_position = (position[0]+1, position[1])
    second_right_position = (position[0]+2, position[1])
    top_position = (position[0], position[1]-1)
    second_top_position = (position[0], position[1]-2)
    bottom_position = (position[0], position[1]+1)
    second_bottom_position = (position[0], position[1]+2)
    # Left side first
    left_character = raw_data[left_position[1]][left_position[0]]
    if left_character == '.':
        for level in range(levels):
            point1 = (position, level)
            G.add_edge((position,level), (left_position, level))
    elif left_character in string.ascii_uppercase:
        second_left_character = raw_data[second_left_position[1]][second_left_position[0]]
        portal_name = second_left_character + left_character
        if portal_name not in portals.keys():
            portals[portal_name] = []
        if position[0] > 2:
            outer_portal = False
        else:
            outer_portal = True
        portals[portal_name] += [{'maze': position, 'portal':left_position, 'outer': outer_portal}]
    # right_character
    right_character = raw_data[right_position[1]][right_position[0]]
    if right_character == '.':
        for level in range(levels):
            G.add_edge((position,level), (right_position,level))
    elif right_character in string.ascii_uppercase:
        second_right_character = raw_data[second_right_position[1]][second_right_position[0]]
        portal_name = right_character + second_right_character
        if position[0] < len(raw_data[0]) - 4:
            outer_portal = False
        else:
            outer_portal = True
        if portal_name not in portals.keys():
            portals[portal_name] = []
        portals[portal_name] += [{'maze': position, 'portal':right_position, 'outer': outer_portal}]
    # Top character
    top_character = raw_data[top_position[1]][top_position[0]]
    if top_character == '.':
        for level in range(levels):
            G.add_edge((position, level), (top_position,level))
    elif top_character in string.ascii_uppercase:
        second_top_character = raw_data[second_top_position[1]][second_top_position[0]]
        portal_name = second_top_character + top_character
        if position[1] > 2:
            outer_portal = False
        else:
            outer_portal = True
        if portal_name not in portals.keys():
            portals[portal_name] = []
        portals[portal_name] += [{'maze': position, 'portal':top_position, 'outer': outer_portal}]
    # bottom character
    bottom_character = raw_data[bottom_position[1]][bottom_position[0]]
    if bottom_character == '.':
        for level in range(levels):
            G.add_edge((position, level), (bottom_position, level))
    elif bottom_character in string.ascii_uppercase:
        second_bottom_character = raw_data[second_bottom_position[1]][second_bottom_position[0]]
        portal_name = bottom_character + second_bottom_character
        if position[1] < len(raw_data) - 4:
            outer_portal = False
        else:
            outer_portal = True
        if portal_name not in portals.keys():
            portals[portal_name] = []
        portals[portal_name] += [{'maze': position, 'portal':bottom_position, 'outer': outer_portal}]
            
    
# Build standard edges
for y in range(len(raw_data)):
    current_line = raw_data[y]
    for x in range(len(current_line)):
        current_tile = current_line[x]
        if current_tile == '.':
            search_edges((x,y))
# build portals
for portal in portals:
    if portal == 'AA' or portal == 'ZZ':
        continue
    current_portal_pair = portals[portal]
    if part2 == False:
        first_node = (current_portal_pair[0]['maze'],0)
        second_node = (current_portal_pair[1]['maze'],0)
        G.add_edge(first_node, second_node)
    else:
        if portal == 'FD':
            print()
        for level in range(levels-1):
            first_point = current_portal_pair[0]['maze'] if current_portal_pair[0]['outer'] == False else current_portal_pair[1]['maze']
            second_point = current_portal_pair[1]['maze'] if current_portal_pair[1]['outer'] == True else current_portal_pair[0]['maze']
            G.add_edge((first_point,level),(second_point,level + 1))

start_node = portals['AA'][0]['maze']
end_node = portals['ZZ'][0]['maze']

shortest_path_length = len(nx.shortest_path(G,(start_node,0), (end_node,0))) - 1
print('Shortest path is ' + str(shortest_path_length))


    