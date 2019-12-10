import numpy as np

f = open('aoc08.txt','r')
input_file = []
for line in f:
    input_file += line[:-1]
f.close()

width = 25
height = 6
image = []

layer_size = width * height

current_width = 0
current_height = 0
current_capacity = 0
current_layer = []
current_row = []
for number in input_file:
    if current_capacity == layer_size:
        current_capacity = 0
        current_width = 0
        current_height = 0
        current_layer += [current_row]
        image += [current_layer]
        current_layer = []
        current_row = []
    elif current_width == width:
        current_layer += [current_row]
        current_row = []
        current_width = 0
        current_height += 1
    current_row += number
    current_width += 1
    current_capacity += 1
current_layer += [current_row]
image += [current_layer]

# Now determine number of '0'
num_zeroes = 999999999999999999999999999999999999999999999999999999
low_layer = 0
low_ones = 0
low_twos = 0
current_row = 0
current_layer = 0
for layer in image:
    layer_zeros = 0
    layer_ones = 0
    layer_twos = 0
    for row in layer:
        layer_zeros += row.count('0')
        layer_ones += row.count('1')
        layer_twos += row.count('2')
    if layer_zeros < num_zeroes:
        num_zeroes = layer_zeros
        low_ones = layer_ones
        low_twos = layer_twos
        low_layer = current_layer
    current_layer += 1

print('Part 1: ' + str(low_ones * low_twos))


def find_color(image, position, current_layer, num_layers):
    global width
    
    column = position % width
    row = position / width
    pixel = image[current_layer][row][column]
    if pixel == '0':
        return ' '
    elif pixel == '1':
        return '*'
    elif pixel == '2' and current_layer == num_layers - 1:
        return ' '
    else:
        return(find_color(image, position, current_layer + 1, num_layers))
    
new_image = []
new_row = []

for position in range(0,width*height):
    if position % width == 0:
        new_image += [new_row]
        new_row = []
    new_row += find_color(image, position, 0, len(image))
new_image += [new_row]

for row in new_image:
    print(''.join(row))

