from collections import deque

f = open('aoc22.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

num_of_cards = 10007
target_card = 2019

deck = []
for x in xrange(num_of_cards):
    deck.append(x)

print('start position: ' + str(deck.index(2019)))
def deal_new(deck,_):
    deck.reverse()
    return deck

def cut(deck, n):
    temp_deck = deck[n:] + deck[0:n]
    return temp_deck

def deal_increment(deck, n):
    queue = deque(deck)
    current_rotate = 0
    for item in deck:
        queue[0] = item
        queue.rotate(-n)
        current_rotate += n
    queue.rotate(current_rotate)
    return list(queue)

instructions =[]

for line in raw_input:
    split_line = line.split(' ')
    if split_line[0] == 'deal':
        if split_line[1] == 'into':
            instructions += [(deal_new,0)]
        elif split_line[1] == 'with':
            argument = int(split_line[3])
            instructions += [(deal_increment, argument)]
    elif split_line[0] == 'cut':
        argument = int(split_line[1])
        instructions += [(cut, argument)]


for instruction in instructions:
    current_instruction = instruction[0]
    argument = instruction[1]
    deck = current_instruction(deck, argument)

# Part 1:

position = str(deck.index(target_card))
print('Part 1: card ' + str(target_card) + ' is in position ' + str(position))

num_of_cards = 119315717514047
offset = 0
increment = 1

state = (offset, increment)

def new_deal(state, argument, size):
    offset = state[0]
    increment = state[1]
    increment *= -1
    offset += increment
    return (offset, increment)

def new_cut(state, argument, size):
    offset = state[0]
    increment = state[1]
    offset += increment * argument
    return (offset, increment)
def new_increment(state, argument, size):
    offset = state[0]
    increment = state[1]
    increment *= pow(argument, size-2, size)
    return (offset, increment)
def get_card_in_position(state, i, size):
    offset = state[0]
    increment = state[1]
    return (offset + i * increment) % size
def inv(n, cards):
    return pow(n, cards-2, cards)

new_instructions = []
for instruction in instructions:
    if instruction[0] == deal_new:
        new_instructions += [(new_deal, 0, num_of_cards)]
    elif instruction[0] == cut:
        new_instructions += [(new_cut, instruction[1], num_of_cards)]
    elif instruction[0] == deal_increment:
        new_instructions += [(new_increment, instruction[1], num_of_cards)]

for instruction in new_instructions:
    state = instruction[0](state, instruction[1], instruction[2])

offset_diff = state[0]
increment_mul = state[1]

multiplier =101741582076661

final_increment = pow(increment_mul, multiplier, num_of_cards)
final_offset = offset_diff * (1 - pow(increment_mul, multiplier, num_of_cards)) * inv(1 - increment_mul, num_of_cards)

position = get_card_in_position((final_offset, final_increment), 2020, num_of_cards)
print('Part 2: the card in position 2020 is ' + str(position))