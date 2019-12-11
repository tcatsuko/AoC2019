starting_panel = 0

f = open('aoc11.txt','r')
program_input_raw = []
for line in f:
    program_input_raw += [line]
f.close()
program_input_base = program_input_raw[0][:-1].split(',')
program_input = program_input_base[:]

#input_value = 2
program_counter = 0
mode1 = 0
mode2 = 0
mode3 = 0
rel_base = 0
program_running = True


def expand_memory(program_input, spot_needed):
    current_length = len(program_input)
    needed_length = int(spot_needed) - current_length + 1
    new_array = []
    for x in range(needed_length):
        new_array += [0]
    return program_input + new_array
    
# Simulate input / output

current_position = (0,0)
current_direction = (0,1)
painting = True
surface = {}
surface[(0,0)] = starting_panel
painted_regions = set()

def input_routine(surface, current_position):
    if current_position in surface:
        return surface[current_position]
    else:
        surface[current_position] = 0
        return surface[current_position]

def change_direction(command, current_direction):
    my_command = str(command)
    if my_command == '0':
        if current_direction == (0,-1):
            return (-1,0)
        elif current_direction == (-1,0):
            return(0,1)
        elif current_direction == (0,1):
            return (1,0)
        else:
            return(0,-1)
    else:
        if current_direction == (0,-1):
            return(1,0)
        elif current_direction == (1,0):
            return(0,1)
        elif current_direction == (0,1):
            return (-1,0)
        else:
            return(0,-1)
    
def output_routine(surface, command):
    global painting
    global current_position
    global current_direction
    global painted_regions
    
    if painting == True:
        painting = False
        surface[current_position] = int(command)
        painted_regions.add(current_position)
    elif painting == False:
        painting = True
        current_direction = change_direction(command, current_direction)
        current_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])




print()
while program_running == True:
    instruction = program_input[program_counter]
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
        program_input[location] = str(result)            
        
        
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
        program_input[location] = str(result)
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
        program_input[location] = str(input_routine(surface, current_position))
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
        output_routine(surface, recent_output)
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

def display_grid(surface):
    # find min_x
    keys = surface.keys()
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for item in keys:
        if item[0] < min_x:
            min_x = item[0]
        if item[0] > max_x:
            max_x = item[0]
        if item[1] < min_y:
            min_y = item[1]
        if item[1] > max_y:
            max_y = item[1]
    x_size = max_x + (0 - min_x)
    y_size = max_y + (0 - min_y)
    image_output = []
    for y in range(y_size + 1):
        current_row = []
        for x in range(x_size + 1):
            current_row += [' ']
        
        image_output += [current_row]
    for item in keys:
        corrected_location = (item[0] - (min_x - 0), item[1] - (min_y - 0))
        value = surface[item]
        if value == 1:
            image_output[corrected_location[1]][corrected_location[0]] = '#'
            #print(image_output[corrected_location[1]][corrected_location[0]])
    image_output.reverse()
    for row in image_output:
        row.reverse()
        print(''.join(row))
        
print('The robot painted ' + str(len(painted_regions)) + ' at least once.')

display_grid(surface)

