f = open('aoc14.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

# Parse reactions
reactions = []
leftover = {}
for line in raw_input:
    process = line.split(' => ')
    result = process[1]
    ingredients = process[0]
    reaction = {}
    result_split = result.split(' ')
    reaction['result'] = result_split[1]
    reaction['quantity'] = int(result_split[0])
    my_ingredients = []
    for item in ingredients.split(', '):
        split_item = item.split(' ')
        individual_ingredient = (int(split_item[0]), split_item[1])
        my_ingredients += [individual_ingredient]
    reaction['ingredients'] = my_ingredients
    reactions += [reaction]
    leftover[reaction['result']] = 0


def calculate_ore(needed, product, reactions):
    global leftover
    reaction = filter(lambda rxn:rxn['result'] == product, reactions)[0]
    existing = leftover[product]
    reaction_result_quantity = reaction['quantity']
    if existing < needed:
        multiplier = (needed - existing) / reaction_result_quantity if (needed - existing) % reaction_result_quantity == 0 else (needed - existing) / reaction_result_quantity + 1
    else:
        multiplier = 0
    extra = (reaction['quantity'] * multiplier) - (needed - existing)
    if product != 'ORE':
        leftover[product] = extra
    ore = 0
    for item in reaction['ingredients']:
        if item[1] == 'ORE':
            ore += multiplier * item[0]
        else:
            ore += calculate_ore(multiplier * item[0], item[1], reactions)
    return ore

ore_needed = calculate_ore(1, 'FUEL', reactions)

print('Part 1: ore needed is ' + str(ore_needed))
#597478 too high
#2259 too low

# Now for part 2
part_1_ore_needed = ore_needed
ore_available = 1000000000000

# Reset leftover

for item in leftover.keys():
    leftover[item] = 0
test_fuel_needed = int(ore_available/part_1_ore_needed * 1.86185) # Looked at output stream and manually set
test_ore_needed = calculate_ore(test_fuel_needed, 'FUEL', reactions)
print ore_available - test_ore_needed
part2 = test_fuel_needed

while True:
    for item in leftover.keys():
        leftover[item] = 0
    test_ore_needed = calculate_ore(test_fuel_needed, 'FUEL', reactions)
    if test_ore_needed < ore_available:
        part2 = test_ore_needed
        print(ore_available - test_ore_needed)
    else:
        break
    test_fuel_needed += 1
print('part 2: ' + str(test_fuel_needed-1) + ' fuel needed to use up ore.')
for item in leftover.keys():
    leftover[item] = 0
print (ore_available - calculate_ore(test_fuel_needed - 1, 'FUEL', reactions) )