from itertools import permutations
from collections import deque
f = open('aoc07.txt','r')
program_input_raw = []
for line in f:
    program_input_raw += [line]
f.close()
program_input_common = program_input_raw[0][:-1].split(',')
program_input = program_input_common[:]
part_2_raw = deque()
part_2_raw += [program_input[:]]
part_2_raw += [program_input[:]]
part_2_raw += [program_input[:]]
part_2_raw += [program_input[:]]
part_2_raw += [program_input[:]]

#print()
input_value = 5
largest_output = 0
sequences = list(permutations(range(0,5)))
for input_sequence in sequences:
    recent_output = 0
    for input_value in input_sequence:
        first_input = True
        program_counter = 0
        mode1 = 0
        mode2 = 0
        mode3 = 0
        
        program_running = True
    
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
                # Addition
                addend1 = 0
                addend2 = 0
                if mode1 == 0:
                    addend1 = int(program_input[int(program_input[program_counter + 1])])
                else:
                    addend1 = int(program_input[program_counter + 1])
                if mode2 == 0:
                    addend2 = int(program_input[int(program_input[program_counter + 2])])
                else:
                    addend2 = int(program_input[program_counter + 2])
                location = int(program_input[program_counter + 3])
                result = addend1 + addend2
                program_input[location] = str(result)
                program_counter += 4
            elif opcode == 2:
                param1 = 0
                param2 = 0
                if mode1 == 0:
                    param1 = int(program_input[int(program_input[program_counter + 1])])
                else:
                    param1 = int(program_input[program_counter + 1])
                if mode2 == 0:
                    param2 = int(program_input[int(program_input[program_counter + 2])])
                else:
                    param2 = int(program_input[program_counter + 2])
                result = param1 * param2
                location = int(program_input[program_counter + 3])
                program_input[location] = str(result)
                program_counter += 4
            elif opcode == 3:
                if first_input == True:
                    insert_value = input_value
                    first_input = False
                else:
                    insert_value = recent_output
                location = int(program_input[program_counter + 1])
                program_input[location] = str(insert_value)
                program_counter += 2
            elif opcode == 4:
                if mode1 == 0:
                    recent_output = program_input[int(program_input[program_counter + 1])]
                else:
                    recent_output = program_input[program_counter + 1]
                program_counter += 2
                #print(recent_output)
            elif opcode == 5:
                condition = 0
                if mode1 == 0:
                    condition = int(program_input[int(program_input[program_counter + 1])])
                else:
                    condition = int(program_input[program_counter + 1])
                if condition != 0:
                    if mode2 == 0:
                        program_counter = int(program_input[int(program_input[program_counter + 2])])
                    else:
                        program_counter = int(program_input[program_counter + 2])
                else:
                    program_counter += 3
            elif opcode == 6:
                condition = 0
                if mode1 == 0:
                    condition = int(program_input[int(program_input[program_counter + 1])])
                else:
                    condition = int(program_input[program_counter + 1])
                if condition == 0:
                    if mode2 == 0:
                        program_counter = int(program_input[int(program_input[program_counter + 2])])
                    else:
                        program_counter = int(program_input[program_counter + 2]) 
                else:
                    program_counter += 3
            elif opcode == 7:
                param1 = 0
                param2 = 0
                result = -1
                if mode1 == 0:
                    param1 = int(program_input[int(program_input[program_counter + 1])])
                else:
                    param1 = int(program_input[program_counter + 1])
                if mode2 == 0:
                    param2 = int(program_input[int(program_input[program_counter + 2])])
                else:
                    param2 = int(program_input[program_counter + 2])
                location = int(program_input[program_counter + 3])
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
                    param1 = int(program_input[int(program_input[program_counter + 1])])
                else:
                    param1 = int(program_input[program_counter + 1])
                if mode2 == 0:
                    param2 = int(program_input[int(program_input[program_counter + 2])])
                else:
                    param2 = int(program_input[program_counter + 2])
                location = int(program_input[program_counter + 3])
                if param1 == param2:
                    result = 1
                else:
                    result = 0
                program_input[location] = result    
                program_counter += 4
            elif opcode == 99:
                program_running = False

    if int(recent_output) > int(largest_output):
        largest_output = recent_output
    #print('outer sequence')
    
print('Part 1: largest output is ' + str(largest_output))

largest_result = 0

def run_program(pc, first_flags, iterations, loop_output, program_input):
    mode1 = 0
    mode2 = 0
    mode3 = 0
    global largest_result
    program_running = True

    while program_running == True:
        instruction = program_input[0][pc[0]]
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
            # Addition
            addend1 = 0
            addend2 = 0
            if mode1 == 0:
                addend1 = int(program_input[0][int(program_input[0][pc[0] + 1])])
            else:
                addend1 = int(program_input[0][pc[0] + 1])
            if mode2 == 0:
                addend2 = int(program_input[0][int(program_input[0][pc[0] + 2])])
            else:
                addend2 = int(program_input[0][pc[0] + 2])
            location = int(program_input[0][pc[0] + 3])
            result = addend1 + addend2
            program_input[0][location] = str(result)
            pc[0] += 4
        elif opcode == 2:
            param1 = 0
            param2 = 0
            if mode1 == 0:
                param1 = int(program_input[0][int(program_input[0][pc[0] + 1])])
            else:
                param1 = int(program_input[0][pc[0] + 1])
            if mode2 == 0:
                param2 = int(program_input[0][int(program_input[0][pc[0] + 2])])
            else:
                param2 = int(program_input[0][pc[0] + 2])
            result = param1 * param2
            location = int(program_input[0][pc[0] + 3])
            program_input[0][location] = str(result)
            pc[0] += 4
        elif opcode == 3:
            if first_flags[0] == True:
                insert_value = iterations[0]
                first_flags[0] = False
            else:
                insert_value = loop_output
            location = int(program_input[0][pc[0] + 1])
            program_input[0][location] = str(insert_value)
            pc[0] += 2
        elif opcode == 4:
            if mode1 == 0:
                recent_output = program_input[0][int(program_input[0][pc[0] + 1])]
            else:
                recent_output = program_input[0][pc[0] + 1]
            pc[0] += 2
            pc.rotate(-1)
            first_flags.rotate(-1)
            iterations.rotate(-1)
            program_input.rotate(-1)
            recent_output = run_program(pc, first_flags, iterations,recent_output, program_input)
            if int(recent_output) > int(largest_result):
                largest_result = recent_output
            loop_output = recent_output
            #print(recent_output)
        elif opcode == 5:
            condition = 0
            if mode1 == 0:
                condition = int(program_input[0][int(program_input[0][pc[0] + 1])])
            else:
                condition = int(program_input[0][pc[0] + 1])
            if condition != 0:
                if mode2 == 0:
                    pc[0] = int(program_input[0][int(program_input[0][pc[0] + 2])])
                else:
                    pc[0] = int(program_input[0][pc[0] + 2])
            else:
                pc[0] += 3
        elif opcode == 6:
            condition = 0
            if mode1 == 0:
                condition = int(program_input[0][int(program_input[0][pc[0] + 1])])
            else:
                condition = int(program_input[0][pc[0] + 1])
            if condition == 0:
                if mode2 == 0:
                    pc[0] = int(program_input[0][int(program_input[0][pc[0] + 2])])
                else:
                    pc[0] = int(program_input[0][pc[0] + 2]) 
            else:
                pc[0] += 3
        elif opcode == 7:
            param1 = 0
            param2 = 0
            result = -1
            if mode1 == 0:
                param1 = int(program_input[0][int(program_input[0][pc[0] + 1])])
            else:
                param1 = int(program_input[0][pc[0] + 1])
            if mode2 == 0:
                param2 = int(program_input[0][int(program_input[0][pc[0] + 2])])
            else:
                param2 = int(program_input[0][pc[0] + 2])
            location = int(program_input[0][pc[0] + 3])
            if param1 < param2:
                result = 1
            else:
                result = 0
            program_input[0][location] = result
            pc[0] += 4
        elif opcode == 8:
            param1 = 0
            param2 = 0
            result = -1
            if mode1 == 0:
                param1 = int(program_input[0][int(program_input[0][pc[0] + 1])])
            else:
                param1 = int(program_input[0][pc[0] + 1])
            if mode2 == 0:
                param2 = int(program_input[0][int(program_input[0][pc[0] + 2])])
            else:
                param2 = int(program_input[0][pc[0]+ 2])
            location = int(program_input[0][pc[0] + 3])
            if param1 == param2:
                result = 1
            else:
                result = 0
            program_input[0][location] = result    
            pc[0] += 4
        elif opcode == 99:
            program_running = False
            return loop_output
#print('Part 1: largest recent output is ' + str(largest_output))

# Part 2:
loop_result = 0
sequences = list(permutations(range(5,10)))
for input_sequence in sequences:
    
    part_2_input = deque()
    part_2_input += [part_2_raw[0]]
    part_2_input += [part_2_raw[1]]
    part_2_input += [part_2_raw[2]]
    part_2_input += [part_2_raw[3]]
    part_2_input += [part_2_raw[4]]
    first_flags = deque()
    first_flags += [True]
    first_flags += [True]
    first_flags += [True]
    first_flags += [True]
    first_flags += [True]
    pc = deque()
    pc += [0]
    pc += [0]
    pc += [0]
    pc += [0]
    pc += [0]
    
    #input_sequence = [9,8,7,6,5]
    iterations = deque()
    iterations += [input_sequence[0]]
    iterations += [input_sequence[1]]
    iterations += [input_sequence[2]]
    iterations += [input_sequence[3]]
    iterations += [input_sequence[4]]
    
    
    #run_program(pc, first_flags, iterations, loop_output, program_input):
    program_result = run_program(pc, first_flags, iterations, 0, part_2_input)
    #print(program_result)
    
    if int(program_result) > int(loop_result):
        loop_result = program_result
    
print('Part 2: ' + str(loop_result))       
# 484272331 too high
#18812 too low
