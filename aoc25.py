import sys
from collections import deque

f = open('aoc25.txt','r')
program_input_raw = []
for line in f:
    program_input_raw += [line]
f.close()
program_input = []
program_input_base = program_input_raw[0][:-1].split(',')
program_commands = deque()

for item in program_input_base:
    program_input += [int(item)]


def output_routine(output):
    if output < 128:
        character = str(unichr(output))
        sys.stdout.write(character)
    else:
        print(str(output))

def expand_memory(program_input, spot_needed):
    current_length = len(program_input)
    needed_length = int(spot_needed) - current_length + 1
    new_array = []
    for x in range(needed_length):
        new_array += [0]
    return program_input + new_array

def input_routine():
    global program_commands
    if program_commands:
        return program_commands.popleft()
    else:
        new_command = raw_input('')
        for letter in new_command:
            program_commands.append(ord(letter))
        program_commands.append(10)  
        return program_commands.popleft()

def run_program(program_input):
    program_counter = 0
    mode1 = 0
    mode2 = 0
    mode3 = 0
    rel_base = 0    
    program_running = True
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
run_program(program_input)