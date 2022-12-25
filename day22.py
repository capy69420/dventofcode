import re


def get_password(tiles, path):
  # Initialize the starting position and facing
  row = 0
  col = 0
  while tiles[0][col] != '.': # go to the starting point
    col += 1
  facing = 0 # right
  path = re.findall(r'\d+|\D', path)
  # Iterate through the path instructions
  for i in range(0,len(path)-1,2):
    # Extract the number of tiles to move and the direction to turn
    num_tiles = int(path[i])
    turn_dir = path[i+1]
    # Move forward in the current facing direction
    for j in range(num_tiles):
      if facing == 0: # right
        col += 1
        # warp to the other side
        if col >= len(tiles[row]) or tiles[row][col] == ' ':
            col = 0
            while tiles[row][col] != '.' and tiles[row][col] != '#': # not the other side yet or not a wall
                col += 1
        # hit a wall go back to the last '.'
        if tiles[row][col] == '#':
          while tiles[row][col] != '.': # go back
            if col == 0: # warp case
                col = len(tiles[row])
            col -= 1
      elif facing == 1: # down
        row += 1
        # is the last row, tiles[row][col] is out of range or is a space
        if row >= len(tiles) or len(tiles[row]) <= col or tiles[row][col] == ' ': # warp to the other side
            row = 0
            while tiles[row][col] != '.' and tiles[row][col] != '#': # not the other side yet or not a wall
                row += 1
        # hit the wall
        if tiles[row][col] == '#':
          while col >= len(tiles[row]) or tiles[row][col] != '.': # go back
            if row == 0:
                row = len(tiles)
            row -= 1
      elif facing == 2: # left
        col -= 1
        # warp to the other side
        if col < 0 or tiles[row][col] == ' ':
            col = len(tiles[row]) - 1
            while tiles[row][col] != '.' and tiles[row][col] != '#': # not the other side yet or not a wall
                col -= 1
        # hit a wall go back to the last '.'
        if tiles[row][col] == '#':
          while tiles[row][col] != '.': # go back
            if col == len(tiles[row]) - 1: # warp case
                col = -1
            col += 1
      elif facing == 3: # up
        row -= 1
        if row < 0 or len(tiles[row]) <= col or tiles[row][col] == ' ': # warp to the other side
            row = len(tiles) - 1
            while len(tiles[row]) <= col or (tiles[row][col] != '.' and tiles[row][col] != '#'): # not the other side yet or not a wall
                row -= 1
        # hit the wall
        if tiles[row][col] == '#':
          while col >= len(tiles[row]) or tiles[row][col] != '.': # go back
            if row == 0:
                row = len(tiles)
            row -= 1
    # Turn in the specified direction
    if turn_dir == "L":
      if facing == 0:
        facing = 3
      else:
        facing -= 1
    elif turn_dir == "R":
      facing = (facing + 1) % 4
  # Calculate and return the final password
  return 1000 * (row + 1) + 4 * (col + 1) + facing

with open("input22.txt") as f:
    tiles = []
    path = ""
    data = f.read().split("\n\n")
    path = data[1].strip()
    for line in data[0].split("\n"):
        tiles.append(line)

# Call the get_password function and print the result
password = get_password(tiles, path)
print(password)
