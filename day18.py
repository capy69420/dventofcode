# Initialize counter for exposed sides
exposed_sides = 0

# Parse input to extract positions of cubes
positions = []
max_coord = 0
with open('input18.txt', 'r') as f:
    for line in f:
        x, y, z = line.split(',')
        x, y, z = int(x), int(y), int(z)
        max_coord = max(x, y, z, max_coord)
        positions.append((x,y,z))

# Initialize 3D grid with dimensions large enough to fit all cubes
grid = [[[0 for _ in range(max_coord+2)] for _ in range(max_coord+2)] for _ in range(max_coord+2)]

# Place cubes in grid based on their positions
for x, y, z in positions:
    grid[x][y][z] = 1

adjacent = {}
for x,y,z in positions:
    adjacent[(x,y,z)] = []
# Iterate over cubes in grid and count exposed sides
for x, y ,z in positions:
    # out of the grid limits
    # top
    if grid[x][y][z+1] == 1:
        # check if it was counted already to evade repeat counts
        if (x,y,z+1) not in adjacent[(x,y,z)]:
            exposed_sides += 1
            adjacent[(x,y,z)].append((x,y,z+1))
    # bottom
    if grid[x][y][z-1] == 1:
        if (x,y,z-1) not in adjacent[(x,y,z)]:
            exposed_sides += 1
            adjacent[(x,y,z)].append((x,y,z-1))
    # sides
    if grid[x+1][y][z] == 1:
        if (x+1,y,z) not in adjacent[(x,y,z)]:
            exposed_sides += 1
            adjacent[(x,y,z)].append((x+1,y,z))
    if grid[x-1][y][z] == 1:
        if (x-1,y,z) not in adjacent[(x,y,z)]:
            exposed_sides += 1
            adjacent[(x,y,z)].append((x-1,y,z))
    if grid[x][y+1][z] == 1:
        if (x,y+1,z) not in adjacent[(x,y,z)]:
            exposed_sides += 1
            adjacent[(x,y,z)].append((x,y+1,z))
    if grid[x][y-1][z] == 1:
        if (x,y-1,z) not in adjacent[(x,y,z)]:
            exposed_sides += 1
            adjacent[(x,y,z)].append((x,y-1,z))

#print(adjacent)
# Output exposed sides
print(len(positions) * 6 - exposed_sides)
