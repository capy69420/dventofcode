# Sand starting pour
pour_x, pour_y = 500,0
# Stores the rocks
rocks = []
# Read rocks lines from input
with open('input14.txt', 'r') as f:
    lines = f.readlines()

# Find the max/min x and y, sand puring location set as min
max_x, min_x, max_y, min_y = -1000, pour_x, -1000, pour_y
for line in lines:
    # Store rhe rocks locations per input line
    rock_path = []
    coords = line.split('->')
    for i in range(len(coords)):
        # draw rock line from coord[i] to the next one
        x, y = coords[i].strip().split(',')
        x, y = int(x), int(y)
        # get the min and max to draw the borders
        if min_x > x:
            min_x = x
        if max_x < x:
            max_x = x
        # same for y
        if min_y > y:
            min_y = y
        if max_y < y:
            max_y = y
        # save the rocks position
        rock_path.append((x,y))
    rocks.append(rock_path)


# Create the map
output_map = []
# from 0 to max_y - min inclusive
for i in range(max_y - min_y+1):
    row = []
    for j in range(max_x - min_x+1):
        row.append('.')
    output_map.append(row)

# add the sand pouring
output_map[pour_y - min_y][pour_x - min_x] = '+'

# add the rocks
for paths in rocks:
    for i in range(len(paths)-1):
        x1, y1 = paths[i]
        x2, y2 = paths[i+1]
        # turn x1 y1 into the lower one
        if x1 > x2:
            x = x1
            x1 = x2
            x2 = x
        if x1 > x2:
            y = y1
            y1 = y2
            y2 = y
        # print the path
        for j in range(x2 - x1+1):
            output_map[y1 - min_y][x1 - min_x + j] = '#'
        for j in range(y2 - y1+1):
            output_map[y1 - min_y + j][x1 - min_x] = '#'


# Simulate the sand falling
# Stores the current sand locations
# Stores the units of sand come to rest

sand = []
units_of_sand = 0
current_sand = []

while sand:
    # Get the current sand locations
    current_sand = sand.copy()
    sand.clear()
    # Iterate each sand
    for x, y in current_sand:
        # Move down
        new_x, new_y = x, y + 1
        # Check if out of the range
        if new_y >= len(output_map):
            # Sand flow out
            units_of_sand += 1
            continue
        # Check if the tile below is air
        if output_map[new_y][new_x] == '.':
            # Move the sand down
            output_map[new_y][new_x] = 'o'
            output_map[y][x] = '.'
            sand.append((new_x, new_y))
            continue
        # Move diagonally one step down and to the left
        new_x, new_y = x - 1, y + 1
        if new_x >= 0 and new_y < len(output_map) and output_map[new_y][new_x] == '.':
            # Move the sand down
            output_map[new_y][new_x] = 'o'
            output_map[y][x] = '.'
            sand.append((new_x, new_y))
            continue
        # Move diagonally one step down and to the right
        new_x, new_y = x + 1, y + 1
        if new_x < len(output_map[0]) and new_y < len(output_map) and output_map[new_y][new_x] == '.':
            # Move the sand down
            output_map[new_y][new_x] = 'o'
            output_map[y][x] = '.'
            sand.append((new_x, new_y))
            continue
        # Sand comes to rest
        output_map[y][x] = 'o'
        units_of_sand += 1

# Print the output
for line in output_map:
    print(''.join(line))

# Print the result
print('\nUnits of sand come to rest before sand starts flowing into the abyss below: {}'.format(units_of_sand))