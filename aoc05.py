f = open('aoc05.txt','r')
program_input_raw = []
for line in f:
    program_input_raw += [line]
f.close()
program_input = program_input_raw[0][:-1].split(',')
print()
input_value = 5
program_counter = 0
mode1 = 0
mode2 = 0
mode3 = 0
program_running = True
recent_output = -1
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
        location = int(program_input[program_counter + 1])
        program_input[location] = str(input_value)
        program_counter += 2
    elif opcode == 4:
        if mode1 == 0:
            recent_output = program_input[int(program_input[program_counter + 1])]
        else:
            recent_output = program_input[program_counter + 1]
        program_counter += 2
        print(recent_output)
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

print('Part 1: most recent output is ' + str(recent_output))
