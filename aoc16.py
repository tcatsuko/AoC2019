from collections import deque
import copy
part2 = True

f = open('test_aoc16.txt','r')
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
    offset_string = ''
    for x in range(7):
        offset_string += input_number[x]
    offset = int(offset_string)
    input_raw = input_number
    input_number = ''
    for x in range(10000):
        input_number += input_raw

if part2 == True:
    print('Finished generating input number')
    

for position in range(len(input_number)):
    # First generate the correct input pattern
    multiplier = position
    base_pattern_queue = deque(base_pattern)
    pattern_to_apply = deque()
    for number in base_pattern:
        pattern_to_apply.append(number)
        for x in range(multiplier):
            pattern_to_apply.append(number)
    pattern_to_apply.rotate(-1)
    pattern_queues += [pattern_to_apply]
output_signal = deque(split(input_number))
print('Completed generating patterns')
print('Input number is ' + str(len(input_number)) + ' digits.')
for phase in range(number_of_phases):
    new_output = deque()
    current_digit = 0
    for x in range(len(input_number)):
        current_digit_sum = 0
        #current_pattern = pattern_queues[x].copy()
        current_pattern = copy.copy(pattern_queues[x])
        for y in range(len(input_number)):
            current_digit_sum += int(output_signal[0]) * current_pattern[0]
            output_signal.rotate(-1)
            current_pattern.rotate(-1)
        new_output.append(str(current_digit_sum)[-1])
    output_signal = copy.deepcopy(new_output)
#output_signal_list = list(output_signal)
first_8 = ''
for x in range(offset, offset + 8):
    first_8 += output_signal[x]
print('Part 1: After ' + str(number_of_phases) + ' phases the output is ' + first_8)
       
        