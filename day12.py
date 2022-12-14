# Parse the input
with open('input12.txt') as f:
    grid = [line.strip() for line in f]

def find_pos(value):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == value:
                return x, y
# Find the starting position
start_x, start_y = find_pos('S')
end_x, end_y = find_pos('E')

# Define the four possible directions to move in
directions = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1)    # right
]

# Define a function to check if a given position is valid
# (i.e. it is within the bounds of the grid and is not a wall)
def is_valid(x, y):
    if x < 0 or y < 0:
        return False
    if x >= len(grid[0]) or y >= len(grid):
        return False
    return grid[y][x] != '#'

# Define a function to find the next best position to move to
# (i.e. the position with the lowest elevation that is not lower than
# the current position)
def find_next_position(x, y, visited):
    next_x = None
    next_y = None
    min_elevation = float('inf')
    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if not is_valid(new_x, new_y):
            continue
        if (new_x, new_y) in visited:
            continue
        new_elevation = ord(grid[new_y][new_x]) - ord('a')
        if new_elevation > ord(grid[y][x]) - ord('a'):
            continue
        if new_elevation < min_elevation:
            min_elevation = new_elevation
            next_x = new_x
            next_y = new_y
    return next_x, next_y

# Keep track of the visited positions
visited = set()

# Keep track of the current position and steps taken
x = start_x
y = start_y
steps = 0

# Keep looping until we reach
