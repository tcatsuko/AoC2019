starting_panel = 1
free_play = True
f = open('aoc13.txt','r')
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
current_direction = (0,-1)
painting = True
surface = {}
surface[(0,0)] = starting_panel
painted_regions = set()

def input_routine(playing_board):
    global paddle_x
    global ball_x


    if ball_x < paddle_x:
        return -1
    elif ball_x > paddle_x:
        return 1
    else:
        return 0

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
playing_board = []
def output_routine(output, playing_board):
    global score
    global paddle_x
    global ball_x
    global game_running
    global program_running
    global empty_field
    if output[0] != '-1' and output[1] != '0':
        tile = {}
        tile['x'] = output[0]
        tile['y'] = output[1]
        tile['type'] = output[2]
        #playing_board += [tile]
        check_tile = filter(lambda block:block['x'] == tile['x'] and block['y'] == tile['y'], playing_board)
        if len(check_tile) > 0:
            playing_board.remove(check_tile[0])
        playing_board += [tile] 
        if output[2] == '3':
            paddle_x = int(output[0])
        elif output[2] == '4':
            ball_x = int(output[0])
    else:
        if game_running == True and empty_field == True:
            program_running = False
        blocks = filter(lambda block:block['type'] == '2',playing_board)
        
        score = output[2]
        print('Score: ' + str(score) + '. Blocks remaining: ' + str(len(blocks)))
    output = []


print()
program_output = []
if free_play == True:
    program_input[0] = '2'
game_drawn = False
game_running = False
empty_field = False
score = 0
max_blocks = 0
paddle_x = 0
ball_x = 0

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
        program_input[location] = str(input_routine(playing_board))
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
        program_output += [recent_output]
        if len(program_output) == 3:
            output_routine(program_output, playing_board)
            program_output = []
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
        program_input[location] = str(result)
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
        program_input[location] = str(result)
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
    blocks = filter(lambda block:block['type'] == '2', playing_board)
    if len(blocks) < max_blocks:
        game_running = True
        game_drawn = True
    else:
        max_blocks = len(blocks)
    
    
    #if len(blocks) == 363:
        #game_drawn = True
        #game_running = True
    if len(blocks) == 0 and game_running == True:
        empty_field = True
        

# Find block tiles
blocks = filter(lambda block:block['type'] == '2', playing_board)

print('Part 1: there are ' + str(max_blocks) + ' blocks in the board')
print('Part 2: score is ' + str(score))

#display_grid(surface)

