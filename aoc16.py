from collections import deque
import copy
part2 = True

f = open('aoc16.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
input_number = raw_input[0]
current_phase = 0
base_pattern = [0,1,0,-1]
number_of_phases = 100
pattern_queues = []
def split(word):
    return [char for char in word]
offset = 0


if part2 == True:
    print('Finished generating input number')
    

#for position in range(len(input_number)):
    ## First generate the correct input pattern
    #multiplier = position
    #base_pattern_queue = deque(base_pattern)
    #pattern_to_apply = deque()
    #for number in base_pattern:
        #pattern_to_apply.append(number)
        #for x in range(multiplier):
            #pattern_to_apply.append(number)
    #pattern_to_apply.rotate(-1)
    #pattern_queues += [pattern_to_apply]
output_signal = deque(split(input_number))
pattern_queues += [deque(base_pattern)]

print('Completed generating patterns')
print('Input number is ' + str(len(input_number)) + ' digits.')
output_signals = []
#output_signals += [''.join(list(output_signal))]

for phase in range(number_of_phases):
    new_output = deque()
    current_digit = 0
    for x in range(len(input_number)):
        current_digit_sum = 0
        #current_pattern = pattern_queues[x].copy()
        current_pattern = copy.copy(pattern_queues[0])
        current_pattern.rotate(-1)
        pattern_multiply = x
        current_multiply = 0
        if x > 0:
            current_multiply = 1
            current_pattern.rotate(1)
        for y in range(len(input_number)):
            current_digit_sum += int(output_signal[0]) * current_pattern[0]
            output_signal.rotate(-1)
            current_multiply += 1
            if current_multiply > pattern_multiply:
                current_multiply = 0
                current_pattern.rotate(-1)
            #current_pattern.rotate(-1)
        new_output.append(str(current_digit_sum)[-1])
    output_signal = copy.deepcopy(new_output)
    #output_signals += [''.join(list(output_signal))]
#output_signal_list = list(output_signal)
first_8 = ''
for x in range(offset, offset + 8):
    first_8 += output_signal[x]
print('Part 1: After ' + str(number_of_phases) + ' phases the output is ' + first_8)
# Part 2 clever solution
offset = int(raw_input[0][0:7])
# In second half of large number, its just the sum of digits
# Can march backwards and add things that way since offset is larger than half the length of the input arrau
input_number = raw_input[0]
part_2_input = input_number * 10000
part_2_input = list(part_2_input[offset:])
assert offset >= len(input_number) * 10000 / 2 


input_number_ints = [int(x) for x in split(input_number)]
input_number_ints = (input_number_ints * 10000)[offset:]
for step in range(100):
    for i in range(len(input_number_ints) - 2, -1, -1):
        input_number_ints[i] += input_number_ints[i + 1]
        input_number_ints[i] = int(str(input_number_ints[i])[-1])
answer = ''.join(str(x) for x in input_number_ints[0:8])
print('Part 2: answer is ' + answer)
        
        