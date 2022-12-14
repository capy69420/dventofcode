# Read instructions from input file
with open('input10.txt', 'r') as f:
    instructions = f.readlines()

# Initialize the X register to 1 and the cycle counter to 0
x = 1
cycle = 0
signal_tuple = []

for instruction in instructions:
    # Split the instruction into the operation and value (if any)
    words = instruction.split()
    op = words[0]
    val = int(words[1]) if len(words) > 1 else None
    
    # Update the cycle counter based on the operation
    if op == 'addx':
        cycle += 1
        signal_tuple.append((cycle,x,instruction))
        cycle += 1
        signal_tuple.append((cycle,x,instruction))
        x += val
    else:
        cycle += 1
        signal_tuple.append((cycle,x,instruction))

sum = 0
# Calculate the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
# signal_tuple[k] is the strength at cycle k + 1
for k in [19, 59, 99, 139, 179, 219]:
    signal_strength = signal_tuple[k][0] * signal_tuple[k][1]
    cycle = k + 1
    print('Signal strength at cycle {}: {} x:{} i:{}'.format(cycle, signal_strength, signal_tuple[k][1], signal_tuple[k][2]))
    sum += signal_strength
print(sum)

# part 2
# Define the dimensions of the screen
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6

# Initialize the screen with empty pixels
screen = []
for i in range(SCREEN_HEIGHT):
  screen.append(["."] * SCREEN_WIDTH)

# Define the width of the sprite
SPRITE_WIDTH = 3

# Define the X register, which controls the horizontal position of the sprite
x_register = 0

# Define a function that updates the screen with the sprite
def update_screen(screen, x_register):
  # Calculate the horizontal position of the sprite on the screen
  sprite_pos = x_register - SPRITE_WIDTH // 2
  
  # Check if the sprite is visible on the screen
  if sprite_pos >= 0 and sprite_pos + SPRITE_WIDTH <= SCREEN_WIDTH:
    # Update the screen with the sprite
    for i in range(SPRITE_WIDTH):
      screen[0][sprite_pos + i] = "#"


# Loop through the cycles of the CPU and the CRT
for cycle in range(1, SCREEN_WIDTH * SCREEN_HEIGHT + 1):
  # Update the X register
  # (assuming that the value of the X register changes every 10 cycles)
  if cycle % 10 == 0:
    # Parse the instructions and update the X register accordingly
    for instruction in instructions:
      # (assuming that the instructions are in the form "X = VALUE")
      parts = instruction.split("=")
      if parts[0].strip() == "X":
        x_register = int(parts[1].strip())

  # Update the screen with the sprite
  update_screen(screen, x_register)

  # Move to the next row on the screen after every 40 cycles
  if cycle % SCREEN_WIDTH == 0:
    screen.pop(0)
    screen.append(["."] * SCREEN_WIDTH)

# Print the final screen
for row in screen:
  print("".join(row))
