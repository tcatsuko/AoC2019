from collections import deque
override_logic = True

f = open('aoc17.txt','r')
program_input_raw = []
for line in f:
    program_input_raw += [line]
f.close()
program_input = []
program_input_base = program_input_raw[0][:-1].split(',')
for item in program_input_base:
    program_input += [int(item)]

program_counter = 0
mode1 = 0
mode2 = 0
mode3 = 0
rel_base = 0
program_running = True

if override_logic == True:
    program_input[0] = 2


hull_map = [[]]
last_output = 0
    
    


# Build_Input based on manual examination of part 1 map:
sequence = 'A,B,B,C,C,A,A,B,B,C'
func_a = 'L,12,R,4,R,4'
func_b = 'R,12,R,4,L,12'
func_c = 'R,12,R,4,L,6,L,8,L,8'
commands = deque()

for item in sequence:
    commands.append(ord(item))
commands.append(10)
for item in func_a:
    commands.append(ord(item))
commands.append(10)
for item in func_b:
    commands.append(ord(item))
commands.append(10)
for item in func_c:
    commands.append(ord(item))
commands.append(10)
commands.append(ord('n'))
commands.append(10)

def expand_memory(program_input, spot_needed):
    current_length = len(program_input)
    needed_length = int(spot_needed) - current_length + 1
    new_array = []
    for x in range(needed_length):
        new_array += [0]
    return program_input + new_array

def input_routine():
    global commands
    command = commands[0]
    commands.rotate(-1)
    return command
    


def output_routine(output):
    global hull_map
    global last_output
    last_output = output
    current_row = hull_map[len(hull_map)-1]
    if output == 10:
        if len(current_row) > 0:
            hull_map += [[]]
    else:
        if override_logic == False:
            current_row += str(unichr(output))

program_output = []

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


    
print('Map created')
intersections = []

if len(hull_map[-1]) == 0:      # Seems to output an extra newline at the end of map creation
    del hull_map[-1]

if override_logic == False:     # Part 1
    width = len(hull_map[0])
    height = len(hull_map)
    # Find robot:
    robot_location = (0,0)
    for y in range(height):
        for x in range(width):
            if hull_map[y][x] == '^' or hull_map[y][x] == 'v' or hull_map[y][x] == '<' or hull_map[y][x] == '>':
                robot_location = (x,y)
                break
    # Top row
    for x in range(1,width-1):
        if hull_map[0][x] == '#' or (x,0) == robot_location:
            if hull_map[0][x-1] == '#' or (x-1,0) == robot_location:
                if hull_map[0][x+1] == '#' or (x+1,0) == robot_location:
                    if hull_map[1][x] == '#' or (x,1) == robot_location:
                        intersections += [(x,0)]
    # Bottom row
    for x in range(1,width-1):
        if hull_map[height-1][x] == '#' or (x,height-1) == robot_location:
            if hull_map[height-1][x-1] == '#' or (x-1, height-1) == robot_location:
                if hull_map[height-1][x+1] == '#' or (x+1, height-1) == robot_location:
                    if hull_map[height-2][x] == '#' or (x,height-2) == robot_location:
                        intersections += [(x,height-1)]
    # left side:
    for y in range(1,height-1):
        if hull_map[y][0] == '#' or (0,y) == robot_location:
            if hull_map[y-1][0] == '#' or (0,y-1) == robot_location:
                if hull_map[y+1][0] == '#' or (0,y+1) == robot_location:
                    if hull_map[y][1] == '#' or (1,y) == robot_location:
                        intersections += [(0,y)]
    # right side:
    for y in range(1,height-1):
        if hull_map[y][width-1] == '#' or (width-1,y) == robot_location:
            if hull_map[y-1][width-1] == '#' or (width-1, y-1) == robot_location:
                if hull_map[y+1][width-1] == '#' or (width-1, y+1) == robot_location:
                    if hull_map[y][width-2] == '#' or (width-2, y) == robot_location:
                        intersections += [(width-1, y)]
    # Now get the interior of the map
    for y in range(1,height-1):
        for x in range(1,width-1):
            if hull_map[y][x] == '#' or (x,y) == robot_location:
                if hull_map[y][x-1] == '#' or (x-1,y) == robot_location:
                    if hull_map[y][x+1] == '#' or (x+1,y) == robot_location:
                        if hull_map[y-1][x] == '#' or (x,y-1) == robot_location:
                            if hull_map[y+1][x] == '#' or (x,y+1) == robot_location:
                                intersections += [(x,y)]
    print(str(len(intersections)) + ' intersections found.')
    sum_of_alignment = 0
    for item in intersections:
        sum_of_alignment += (item[0] * item[1])
    for line in hull_map:
        print(''.join(line))    
    print('Part 1: The sum of the alignment parameters is ' + str(sum_of_alignment))
# Doing part 2 by hand-ish
else:
    print('Part 2: dust collected = ' + str(last_output))

        
# 3616 too low


