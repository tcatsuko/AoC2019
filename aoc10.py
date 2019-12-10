import math
from operator import itemgetter
f = open('aoc10.txt','r')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()
# create tuples of each asteroid
asteroids = []
current_row = 0
current_column = 0
for line in raw_input:
    current_column = 0
    for character in line:
        if character == '#':
            asteroids += [(current_column, current_row)]
        current_column += 1
    current_row += 1


seen = 0
target_location = (0,0)
seen_asteroids = []
# Now, detect the asteroids seen
def check_cross(endpoint1, endpoint2, midpoint):
    x_short = midpoint[0] - endpoint1[0]
    y_short = midpoint[1] - endpoint1[1]

    x_long = endpoint2[0] - endpoint1[0]
    y_long = endpoint2[1] - endpoint1[1]

    cross = x_short * y_long - y_short * x_long
    if cross == 0:
        return True
    return False

def angle(point1, point2):
    adjacent = float(abs(point1[1] - point2[1]))
    hypo = math.sqrt((point2[0]-point1[0])*(point2[0]-point1[0]) + (point2[1]-point1[1])*(point2[1]-point1[1]))
    return math.degrees(math.acos(adjacent/hypo))


def in_sight(asteroid, other_remaining_asteroids):
    current_seen_locations = []
    for other_asteroid in remaining_asteroids:
        can_be_seen = True
        test_asteroids = remaining_asteroids[:]
        test_asteroids.remove(other_asteroid)
        # Check which is farther left
        left_bound = 0
        right_bound = 0
        top_bound = 0
        bottom_bound = 0
        left_bound = asteroid[0] if asteroid[0] <= other_asteroid[0] else other_asteroid[0]
        right_bound = other_asteroid[0] if other_asteroid[0] >= asteroid[0] else asteroid[0]
        top_bound = asteroid[1] if asteroid[1] <= other_asteroid[1] else other_asteroid[1]
        bottom_bound = other_asteroid[1] if other_asteroid[1] >= asteroid[1] else asteroid[1]
        #asteroids_in_square = list(filter(lambda x: x[0] >= left_bound and x[0] <= right_bound and x[1] >= top_bound and x[1] <= bottom_bound in x, test_asteroids))
        asteroids_in_square = [item for item in test_asteroids if (item[0] >= left_bound and item[0] <= right_bound and item[1] >= top_bound and item[1] <= bottom_bound)]
        asteroids_in_between = []
        for item in asteroids_in_square:
            if check_cross(asteroid, other_asteroid, item) == True:
                asteroids_in_between += [item]
        if len(asteroids_in_between) == 0:
            current_seen_locations += [other_asteroid]
    return current_seen_locations

for asteroid in asteroids:
    if asteroid == (3,4):
        print()
    current_seen = 0
    current_seen_locations = []
    remaining_asteroids = asteroids[:]
    remaining_asteroids.remove(asteroid)
    current_seen_locations = in_sight(asteroid, remaining_asteroids)
    current_seen = len(current_seen_locations)
    if current_seen >= seen:
        seen = current_seen
        seen_asteroids = current_seen_locations
        target_location = asteroid
print('Target location: ' + str(target_location) + ' with ' + str(seen) + ' asteroids detected')


# Now for the fun of part 2
vaporized_asteroids = 0
keep_blasting = True
asteroid = target_location
remaining_asteroids = asteroids[:]
remaining_asteroids.remove(asteroid)
for item in seen_asteroids:
    remaining_asteroids.remove(item)
    
winning_asteroid = (0,0)

while keep_blasting == True:
    if len(remaining_asteroids) == 0:
        keep_blasting = False
        continue
    if len(seen_asteroids) == 0:
        seen_asteroids = in_sight(remaining_asteroids)
        for item in seen_asteroids:
            remaining_asteroids.remove(item)
    seen_angles = []
    for item in seen_asteroids:
        raw_angle = angle(asteroid, item)
        if item[0] < asteroid[0] and item[1] < asteroid[1]:
            corrected_angle = 360.0 - raw_angle
        elif item[0] > asteroid[0] and item[1] > asteroid[1]:
            corrected_angle = 180.0 - raw_angle
        elif item[0] < asteroid[0] and item[1] > asteroid[1]:
            corrected_angle = 180.0 + raw_angle
        elif item[0] == asteroid[0] and item[1] < asteroid[1]:
            corrected_angle = 0.0
        elif item[1] == asteroid[1] and item[0] > asteroid[0]:
            corrected_angle = 90.0
        elif item[0] == asteroid[0] and item[1] > asteroid[1]:
            corrected_angle = 180.0
        elif item[1] == asteroid[1] and item[0] < asteroid[0]:
            corrected_angle = 270.0
        else:
            corrected_angle = raw_angle
        seen_angles += [corrected_angle]
    while len(seen_angles) > 0:
        min_angle_index = min(enumerate(seen_angles), key = itemgetter(1))[0]
        current_target = seen_asteroids[min_angle_index]
        del seen_angles[min_angle_index]
        del seen_asteroids[min_angle_index]
        vaporized_asteroids += 1
        if vaporized_asteroids == 200:
            winning_asteroid = current_target
            keep_blasting = False
            break
        
print('Part 2: ' + str(winning_asteroid[0]*100+winning_asteroid[1]))
        