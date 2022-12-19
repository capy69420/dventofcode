# Constants for the chamber size and the jet patterns
CHAMBER_WIDTH = 7
JET_PATTERNS = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

# Data structure to represent the chamber and the rocks in it
chamber = [['.' for _ in range(CHAMBER_WIDTH)] for _ in range(CHAMBER_WIDTH)]

# Keep track of the number of rocks that have fallen
num_rocks_fallen = 0

# Keep track of the position of the currently falling rock
rock_x = 2  # x coordinate (horizontal position)
rock_y = 0  # y coordinate (vertical position)

# Iterate through the list of jet patterns
for i, jet_pattern in enumerate(JET_PATTERNS):
    # Move the rock one unit in the direction indicated by the jet pattern
    if jet_pattern == '>':
        rock_x += 1
    elif jet_pattern == '<':
        rock_x -= 1

    # Check if the rock has collided with another rock or the walls of the chamber
    if rock_x < 0 or rock_x >= CHAMBER_WIDTH or chamber[rock_y][rock_x] == '#':
        # Stop the rock from moving
        rock_x = max(0, min(rock_x, CHAMBER_WIDTH - 1))
    else:
        # Move the rock down one unit
        rock_y += 1

    # Check if the rock has landed
    if rock_y >= CHAMBER_WIDTH or chamber[rock_y][rock_x] == '#':
        # The rock has landed, so place it in the chamber and start a new rock falling
        chamber[rock_y - 1][rock_x] = '#'
        rock_x = 2
        rock_y = 0
        num_rocks_fallen += 1

    # Print the current state of the chamber for debugging purposes
    print(f'After {i + 1} iterations:')
    for row in chamber:
        print(''.join(row))
    print()

# Print the final state of the chamber
print('Final chamber:')
for row in chamber:
    print(''.join(row))
print(f'Number of rocks fallen: {num_rocks_fallen}')
