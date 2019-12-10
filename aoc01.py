f = open('aoc01.txt','r')
problem_input = []
for line in f:
    problem_input += [int(line)]
fuel_total = 0
for part_mass in problem_input:
    fuel_total += (part_mass / 3) - 2
print('Part 1: Total mass is ' + str(fuel_total))

def calc_fuel(mass):
    fuel_required = (mass / 3)-2
    if fuel_required > 0:
        return fuel_required + calc_fuel(fuel_required)
    else:
        return 0
# part 2
fuel_total = 0
for part_mass in problem_input:
    fuel_total += calc_fuel(part_mass)
print('Part 2: Total mass is ' + str(fuel_total))
