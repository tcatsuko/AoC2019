import networkx as nx

starting_panel = 1
free_play = False
f = open('aoc15.txt','r')
program_input_raw = []
for line in f:
    program_input_raw += [line]
f.close()
program_input = []
program_input_base = program_input_raw[0][:-1].split(',')
for item in program_input_base:
    program_input += [int(item)]
#program_input = program_input_base[:]

#input_value = 2
program_counter = 0
mode1 = 0
mode2 = 0
mode3 = 0
rel_base = 0
program_running = True
G = nx.Graph()

sensor_location = (999999,999999)
current_position = (0,0)
previous_position = (0,0)
start_position = (0,0)
start_direction = 3

# 1: North
# 2: South
# 3: West
# 4: East
determine_position = {1: (0,-1), 2:(0,1), 3:(-1,0), 4:(1,0)}
current_direction = 3
start_direction_sent = 2
test_directions = {1:3, 2:4, 3:2, 4:1}
reverse_directions = {1:2, 2:1, 3:4, 4:3}
next_direction = {1:4, 4:2, 2:3, 3:1}
corner_directions = {1:3, 3:2, 2:4, 4:1}
turn_corner = False
need_to_test = True
reverse_direction = False
change_direction = False

handles = {}
handles['determine_position'] = determine_position
handles['current_direction'] = current_direction
handles['test_directions'] = test_directions
handles['reverse_directions'] = reverse_directions
handles['next_direction'] = next_direction
handles['corner_directions'] = corner_directions
handles['turn_corner'] = turn_corner
handles['need_to_test'] = need_to_test
handles['reverse_direction'] = reverse_direction
handles['change_direction'] = change_direction
handles['direction_sent'] = 1
handles['current_position'] = current_position
handles['previous_position'] = previous_position

def expand_memory(program_input, spot_needed):
    current_length = len(program_input)
    needed_length = int(spot_needed) - current_length + 1
    new_array = []
    for x in range(needed_length):
        new_array += [0]
    return program_input + new_array
    
# Simulate input / output


painting = True
surface = {}
surface[(0,0)] = starting_panel
painted_regions = set()

def input_routine():
    global handles
    global start_position

    if handles['need_to_test'] == True:
        test_direction = handles['test_directions'][handles['current_direction']]
        handles['direction_sent'] = test_direction
        return test_direction
    handles['direction_sent'] = handles['current_direction']
    return handles['current_direction']
    

def output_routine(output):
# 0: Wall
# 1: Empty
# 2: Oxygen
    global G
    global sensor_location
    global handles
    global corridor
    global start_position
    if output == 0:
        # determine if we need to change direction
        direction_sent = handles['direction_sent']
        current_direction = handles['current_direction']
        current_position = handles['current_position']
        if current_direction == direction_sent:
            handles['change_direction'] = True
        if handles['need_to_test'] == True:
            handles['need_to_test'] = False
        else:
            next_direction = handles['next_direction'][current_direction]
            handles['current_direction'] = next_direction
            handles['need_to_test'] = True
      
    elif output == 1:
        
        if handles['need_to_test'] == True:
            current_direction = handles['test_directions'][handles['current_direction']]
            handles['current_direction'] = current_direction
        else:
            current_direction = handles['current_direction']
            handles['need_to_test'] = True
        previous_position = handles['current_position']
        position_offset = handles['determine_position'][current_direction]
        current_position = (previous_position[0] + position_offset[0], previous_position[1] + position_offset[1])

        handles['current_position'] = current_position
        # REMOVE BEFORE FLIGHT
        G.add_edge(previous_position, current_position)
        
    else:
        if handles['need_to_test'] == True:
            current_direction = handles['test_directions'][handles['current_direction']]
            handles['current_direction'] = current_direction
        else:
            current_direction = handles['current_direction']        
        previous_position = handles['current_position']
        position_offset = handles['determine_position'][current_direction]
        current_position = (previous_position[0] + position_offset[0], previous_position[1] + position_offset[1])
        handles['current_position'] = current_position
        handles['generator_position'] = current_position
        # REMOVE BEFORE FLIGHT
        G.add_edge(previous_position, current_position)     
    
  
 


print()
program_output = []
if free_play == True:
    program_input[0] = 2
game_drawn = False
game_running = False
empty_field = False
score = 0
max_blocks = 0
paddle_x = 0
ball_x = 0



back_at_start = False
corridor = set()
corridor.add(start_position)
def test_maze(next_direction, input_maze):
    global handles
    current_position_x = handles['current_position'][0]
    current_position_y = handles['current_position'][1]
    if next_direction == 1:
        return input_maze[current_position_y - 1][current_position_x]
    elif next_direction == 2:
        return input_maze[current_position_y + 1][current_position_x]
    elif next_direction == 3:
        return input_maze[current_position_y][current_position_x - 1]
    else:
        return input_maze[current_position_y][current_position_x + 1]






while program_running == True:
    instruction = str(program_input[program_counter])
    # Parse instruction
    opcode = 0

    instruction_length = len(instruction)
    if instruction_length <= 2:
        opcode = int(instruction)
        mode1 = 0
        mode2 = 0
        mode3 = 0
    elif instruction_length == 3:
        opcode = int(instruction[1:])
        mode1 = int(instruction[0])
        mode2 = 0
        mode3 = 0
    elif instruction_length == 4:
        opcode = int(instruction[2:])
        mode1 = int(instruction[1])
        mode2 = int(instruction[0])
        mode3 = 0
    elif instruction_length == 5:
        opcode = int(instruction[3:])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])
    if opcode == 1:
        addend1 = 0
        addend2 = 0
        if mode1 == 0:
            addend_location = int(program_input[program_counter + 1])
            if addend_location >= len(program_input):
                program_input = expand_memory(program_input, addend_location)
    
            addend1 = int(program_input[addend_location])
        elif mode1 == 1:
            addend1 = int(program_input[program_counter + 1])
        else:
            addend_location = rel_base + int(program_input[program_counter + 1])
            if addend_location >= len(program_input):
                program_input = expand_memory(program_input, addend_location)
    
            addend1 = int(program_input[addend_location])
        if mode2 == 0:
            addend_location = int(program_input[program_counter + 2])
            if addend_location >= len(program_input):
                program_input = expand_memory(program_input, addend_location)
    
            addend2 = int(program_input[addend_location])
        elif mode2 == 1:
            addend2 = int(program_input[program_counter + 2])
        else:
    
            addend_location = rel_base + int(program_input[program_counter + 2])
            if addend_location >= len(program_input):
                program_input = expand_memory(program_input, addend_location)
    
            addend2 = int(program_input[addend_location])
            
            
        if mode3 == 0:
            location = int(program_input[program_counter + 3])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
        elif mode3 == 2:
            location = rel_base + int(program_input[program_counter + 3])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
    
        result = addend1 + addend2
        program_input[location] = result            
        
        
        program_counter += 4
    elif opcode == 2:
        param1 = 0
        param2 = 0
        if mode1 == 0:
            param_location = int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            param1 = int(program_input[param_location])
        elif mode1 == 1:
            param1 = int(program_input[program_counter + 1])
        else:
            param_location = rel_base + int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            param1 = int(program_input[param_location])
        if mode2 == 0:
            param_location = int(program_input[program_counter + 2])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            param2 = int(program_input[param_location])
        elif mode2 == 1:
            param2 = int(program_input[program_counter + 2])
        else:
            param_location = rel_base + int(program_input[program_counter + 2])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            param2 = int(program_input[param_location])
        result = param1 * param2
        if mode3 == 0:
            location = int(program_input[program_counter + 3])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
        elif mode3 == 2:
            location = rel_base + int(program_input[program_counter + 3])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
        program_input[location] = result
        program_counter += 4
    elif opcode == 3:
        if mode1 == 0:
            location = int(program_input[program_counter + 1])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
        elif mode1 == 2:
            location = rel_base + int(program_input[program_counter + 1])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
        program_input[location] = input_routine()
        program_counter += 2
        
    elif opcode == 4:
        if mode1 == 0:
            location = int(program_input[program_counter + 1])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
            recent_output = program_input[location]
        elif mode1 == 1:
            recent_output = program_input[program_counter + 1]
        else:
            location = rel_base + int(program_input[program_counter + 1])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
            recent_output = program_input[location]
        program_counter += 2
        output_routine(recent_output)
    elif opcode == 5:
        condition = 0
        if mode1 == 0:
            param_location = int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            condition = int(program_input[param_location])
        elif mode1 == 1:
            condition = int(program_input[program_counter + 1])
        else:
            param_location = rel_base + int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)            
            condition = int(program_input[param_location])
        if condition != 0:
            if mode2 == 0:
                location = int(program_input[program_counter + 2])
                if location >= len(program_input):
                    program_input = expand_memory(program_input, location)
                program_counter = int(program_input[location])
            elif mode2 == 1:
                program_counter = int(program_input[program_counter + 2])
            else:
                location = rel_base + int(program_input[program_counter + 2])
                if location >= len(program_input):
                    program_input = expand_memory(program_input, location)                
                program_counter = int(program_input[location])
        else:
            program_counter += 3
    elif opcode == 6:
        condition = 0
        if mode1 == 0:
            param_location = int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)            
            condition = int(program_input[param_location])
        elif mode1 == 1:
            condition = int(program_input[program_counter + 1])
        else:
            param_location = rel_base + int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)            
            condition = int(program_input[param_location])
            
        if condition == 0:
            if mode2 == 0:
                location = int(program_input[program_counter + 2])
                if location >= len(program_input):
                    program_input = expand_memory(program_input, location)
                program_counter = int(program_input[location])
            elif mode2 == 1:
                program_counter = int(program_input[program_counter + 2])
            else:
                location = rel_base + int(program_input[program_counter + 2])
                if location >= len(program_input):
                    program_input = expand_memory(program_input, location)                
                program_counter = int(program_input[location])
        else:
            program_counter += 3
    elif opcode == 7:
        param1 = 0
        param2 = 0
        result = -1
        if mode1 == 0:
            param_location = int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            param1 = int(program_input[param_location])
        elif mode1 == 1:
            param1 = int(program_input[program_counter + 1])
        else:
            param_location = rel_base + int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)            
            param1 = int(program_input[param_location])
        if mode2 == 0:
            param_location = int(program_input[program_counter + 2])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)                  
            param2 = int(program_input[param_location])
        elif mode2 == 1:
            param2 = int(program_input[program_counter + 2])
        else:
            param_location = rel_base + int(program_input[program_counter + 2])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)                  
            param2 = int(program_input[param_location])
        if mode3 == 0:
            location = int(program_input[program_counter + 3])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
        elif mode3 == 2:
            location = rel_base + int(program_input[program_counter + 3])
            if location >= len(program_input):
                program_input = expand_memory(program_input, location)
        if param1 < param2:
            result = 1
        else:
            result = 0
        program_input[location] = result
        program_counter += 4
    elif opcode == 8:
        param1 = 0
        param2 = 0
        result = -1
        if mode1 == 0:
            param_location = int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            param1 = int(program_input[param_location])
        elif mode1 == 1:
            param1 = int(program_input[program_counter + 1])
        else:
            param_location = rel_base + int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)            
            param1 = int(program_input[param_location])
        if mode2 == 0:
            param_location = int(program_input[program_counter + 2])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)             
            param2 = int(program_input[param_location])
        elif mode2 == 1:
            param2 = int(program_input[program_counter + 2])
        else:
            param_location = rel_base + int(program_input[program_counter + 2])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)               
            param2 = int(program_input[param_location])
        
        if mode3 == 0:
            location = int(program_input[program_counter + 3])
        else:
            location = rel_base + int(program_input[program_counter + 3])
        if location >= len(program_input):
            program_input = expand_memory(program_input, location)
        if param1 == param2:
            result = 1
        else:
            result = 0
        program_input[location] = result
        program_counter += 4
    elif opcode == 9:
        if mode1 == 0:
            param_location = int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)
            param1 = int(program_input[param_location])
        elif mode1 == 1:
            param1 = int(program_input[program_counter + 1])
        else:
            param_location = rel_base + int(program_input[program_counter + 1])
            if param_location >= len(program_input):
                program_input = expand_memory(program_input, param_location)            
            param1 = int(program_input[param_location])
        rel_base += param1
        program_counter += 2
        
    elif opcode == 99:
        program_running = False

    if len(G.edges) > 0 and handles['current_position'] == start_position and handles['current_direction'] == start_direction:
        program_running = False
    
        

shortest_path = nx.shortest_path(G,start_position, handles['generator_position'])
print('Part 1: shortest path is ' + str(len(shortest_path)-1))

# Part 2
max_path = 0
num_of_nodes = len(G.nodes())
for node in G.nodes():
    short_path = nx.shortest_path(G, node, handles['generator_position'])
    short_path_length = len(short_path) - 1
    if short_path_length > max_path:
        max_path = short_path_length
print('Part 2: Longest path is ' + str(max_path))