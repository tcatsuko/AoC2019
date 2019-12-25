from collections import deque
part1 = False

f = open('aoc23.txt','r')
program_input_raw = []
for line in f:
    program_input_raw += [line]
f.close()
program_input_common = []
program_input_base = program_input_raw[0][:-1].split(',')
for item in program_input_base:
    program_input_common += [int(item)]

programs = []
bases = []
inputs = []
outputs = []
counters = []
part1_found = False

def expand_memory(program_input, spot_needed):
    current_length = len(program_input)
    needed_length = int(spot_needed) - current_length + 1
    new_array = []
    for x in range(needed_length):
        new_array += [0]
    return program_input + new_array

for i in range(50):
    programs += [program_input_common[:]]
    bases += [0]
    temp_input = deque()
    temp_input.append(i)
    inputs += [temp_input]
    counters += [0]


#program_counter = 0
part1_result = -1
#rel_base = 0    
#program_running = True
last_NAT_y = 9999999999999999999999999999
NAT = [-1,-1]
idle_count = 0
def check_idle(inputs):
    global idle_count
    for program in inputs:
        if program:
            return False
    print('Idle!')
    idle_count += 1
    return True
while part1_found == False:
    for i in range(50):
        mode1 = 0
        mode2 = 0
        mode3 = 0    
        program_running = True
        program_input = programs[i]
        rel_base = bases[i]
        my_input = inputs[i]
        program_counter = counters[i]
        outputs = deque()
        sent_x = False
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
                #program_input[location] = input_routine()
                if my_input:
                    program_input[location] = my_input.popleft()
                    if sent_x == False:
                        sent_x = True
                    else:
                        program_running = False
                    print('Program ' + str(i) + ': input is ' + str(program_input[location]))
                else:
                    #print('Program ' + str(i) + ': input is -1')
                    program_running = False
                    program_input[location] = -1
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
                #output_routine(recent_output)
                outputs.append(recent_output)
                print('Computer ' + str(i) + ' outputs ' + str(recent_output))
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
        programs[i] = program_input
        bases[i] = rel_base
        #my_input = inputs[i]
        while outputs:
            first_value = outputs.popleft()
            if first_value == 255:
                #temp1 = outputs.popleft()
                #part1_result = outputs.popleft()
                #part1_found = True
                NAT[0] = outputs.popleft()
                NAT[1] = outputs.popleft()
                if part1 == True:
                    part1_found = True
            else:
                output_index = first_value
                x_value = outputs.popleft()
                y_value = outputs.popleft()
                inputs[output_index].append(x_value)
                inputs[output_index].append(y_value)
        counters[i] = program_counter
    use_nat = check_idle(inputs)
    if use_nat == True and part1 == False and idle_count > 10:
        idle_count = 0
        inputs[0].append(NAT[0])
        inputs[0].append(NAT[1])
        if NAT[1] == last_NAT_y:
            break
        else:
            last_NAT_y = NAT[1]
    if part1 == True and part1_found == True:
        break
print('Answer is ' + str(NAT[1]))