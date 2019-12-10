f = open('aoc02.txt','r')
problem_input = []
for line in f:
    problem_input += [line]
initial_program_text = problem_input[0][:-1].split(',')
initial_program = []
for item in initial_program_text:
    initial_program += [int(item)]
print()
# part 1
part1_program = initial_program[:]
position = 0
part1_program[1] = 12
part1_program[2] = 2
while part1_program[position] != 99:
    opcode = part1_program[position]
    operand1 = part1_program[part1_program[position + 1]]
    operand2 = part1_program[part1_program[position + 2]]
    storage_location = part1_program[position + 3]
    if opcode == 1:
        part1_program[storage_location] = operand1 + operand2
    elif opcode == 2:
        part1_program[storage_location] = operand1 * operand2
    position += 4
print('Part 1: ' + str(part1_program[0]))

# part 2
output = 0
noun = 0
verb = 0
running = True
while running == True:
    part2_program = initial_program[:]
    part2_program[1] = noun
    part2_program[2] = verb
    position = 0
    while part2_program[position] != 99:
        opcode = part2_program[position]
        operand1 = part2_program[part2_program[position + 1]]
        operand2 = part2_program[part2_program[position + 2]]
        storage_location = part2_program[position + 3]
        if opcode == 1:
            part2_program[storage_location] = operand1 + operand2
        elif opcode == 2:
            part2_program[storage_location] = operand1 * operand2
        position += 4    
    if part2_program[0] == 19690720:
        running = False
    else:
        verb += 1
        if verb > 99:
            verb = 0
            noun += 1
print('Part 2: ' + str(100 * noun + verb))