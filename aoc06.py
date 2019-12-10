f = open('aoc06.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
planets = {}
for item in raw_input:
    split_item = item.split(')')
    parent = split_item[0]
    child = split_item[1]
    if child not in planets:
        planets[child] = {}
        planets[child]['parent'] = parent
        planets[child]['children'] = []
    else:
        planets[child]['parent'] = parent
    if parent not in planets:
        planets[parent] = {}
        planets[parent]['children'] = []
        planets[parent]['children'] += [child]
    else:
        planets[parent]['children'] += [child]    
# Now traverse and count parents
orbits = 0

def find_orbits(planets, planet):
    if 'parent' not in planets[planet]:
        return 0
    else:
        return 1 + find_orbits(planets, planets[planet]['parent'])
    
for planet in planets.keys():
    orbits += find_orbits(planets, planet)
print('Part 1: there are ' + str(orbits) + ' direct and indrect orbits')