import copy
from fractions import gcd

def lcm(x, y):
    return (x*y) // gcd(x,y)


f = open('aoc12.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
moons = []
for line in raw_input:
    new_moon = {}
    new_moon['vx'] = 0
    new_moon['vy'] = 0
    new_moon['vz'] = 0
    split_values = line.split(', ')
    new_moon['x'] = int(split_values[0].split('=')[1])
    new_moon['y'] = int(split_values[1].split('=')[1])
    new_moon['z'] = int(split_values[2].split('=')[1][:-1])
    moons += [new_moon]
steps = 0
total_steps = 1000


for x in range(total_steps):
    # Apply gravity
    for moon in moons:
        other_moons = moons[:]
        other_moons.remove(moon)
        for other_moon in other_moons:
            if other_moon['x'] > moon['x']:
                moon['vx'] += 1
            elif other_moon['x'] < moon['x']:
                moon['vx'] -= 1
            if other_moon['y'] > moon['y']:
                moon['vy'] += 1
            elif other_moon['y'] < moon['y']:
                moon['vy'] -= 1 
            if other_moon['z'] > moon['z']:
                moon['vz'] += 1
            elif other_moon['z'] < moon['z']:
                moon['vz'] -= 1  
    # Move moons
    for moon in moons:
        moon['x'] += moon['vx']
        moon['y'] += moon['vy']
        moon['z'] += moon['vz']
    steps += 1

# calculate energy
total_energy = 0
for moon in moons:
    potential_energy = abs(moon['x']) + abs(moon['y']) + abs(moon['z'])
    kinetic_energy = abs(moon['vx']) + abs(moon['vy']) + abs(moon['vz'])
    total_energy += (potential_energy * kinetic_energy)

print('Part 1: The total energy after ' + str(steps) + ' steps is ' + str(total_energy))

#part 2
x_steps = 0
y_steps = 0
z_steps = 0

moons = []
for line in raw_input:
    new_moon = {}
    new_moon['vx'] = 0
    new_moon['vy'] = 0
    new_moon['vz'] = 0
    split_values = line.split(', ')
    new_moon['x'] = int(split_values[0].split('=')[1])
    new_moon['y'] = int(split_values[1].split('=')[1])
    new_moon['z'] = int(split_values[2].split('=')[1][:-1])
    moons += [new_moon]
states = []
moons_initial = []
for moon in moons:
    moon_copy = copy.deepcopy(moon)
    moons_initial.append(moon_copy)


while True:
    # Apply gravity
    for moon in moons:
        other_moons = moons[:]
        other_moons.remove(moon)
        for other_moon in other_moons:
            if other_moon['x'] > moon['x']:
                moon['vx'] += 1
            elif other_moon['x'] < moon['x']:
                moon['vx'] -= 1
            
    # Move moons
    for moon in moons:
        moon['x'] += moon['vx']
    x_steps += 1    
    if moons == moons_initial:
        break

        
print('Part 2: it took ' + str(x_steps) + ' steps to get to x axis initial conditions')

moons = []
for line in raw_input:
    new_moon = {}
    new_moon['vx'] = 0
    new_moon['vy'] = 0
    new_moon['vz'] = 0
    split_values = line.split(', ')
    new_moon['x'] = int(split_values[0].split('=')[1])
    new_moon['y'] = int(split_values[1].split('=')[1])
    new_moon['z'] = int(split_values[2].split('=')[1][:-1])
    moons += [new_moon]
states = []
moons_initial = []
for moon in moons:
    moon_copy = copy.deepcopy(moon)
    moons_initial.append(moon_copy)

while True:
    # Apply gravity
    for moon in moons:
        other_moons = moons[:]
        other_moons.remove(moon)
        for other_moon in other_moons:
            if other_moon['y'] > moon['y']:
                moon['vy'] += 1
            elif other_moon['y'] < moon['y']:
                moon['vy'] -= 1
            
    # Move moons
    for moon in moons:
        moon['y'] += moon['vy']
    y_steps += 1    
    if moons == moons_initial:
        break
        
print('Part 2: it took ' + str(y_steps) + ' steps to get to y axis initial conditions')

moons = []
for line in raw_input:
    new_moon = {}
    new_moon['vx'] = 0
    new_moon['vy'] = 0
    new_moon['vz'] = 0
    split_values = line.split(', ')
    new_moon['x'] = int(split_values[0].split('=')[1])
    new_moon['y'] = int(split_values[1].split('=')[1])
    new_moon['z'] = int(split_values[2].split('=')[1][:-1])
    moons += [new_moon]
states = []
moons_initial = []
for moon in moons:
    moon_copy = copy.deepcopy(moon)
    moons_initial.append(moon_copy)

while True:
    # Apply gravity
    for moon in moons:
        other_moons = moons[:]
        other_moons.remove(moon)
        for other_moon in other_moons:
            if other_moon['z'] > moon['z']:
                moon['vz'] += 1
            elif other_moon['z'] < moon['z']:
                moon['vz'] -= 1
            
    # Move moons
    for moon in moons:
        moon['z'] += moon['vz']
    z_steps += 1    
    if moons == moons_initial:
        break

        states += moons_copy  
print('Part 2: it took ' + str(z_steps) + ' steps to get to z axis initial conditions')
print('Part 2: it takes ' + str(lcm(x_steps, lcm(y_steps, z_steps))) + ' steps to reach a duplicate condition')

            