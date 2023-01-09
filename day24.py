from collections import deque

class Node:
    def __init__(self, val, parent=None):
        self.val = val
        self.children = []
        self.parent = parent
    
    def add_child(self, child_node):
        self.children.append(child_node)
    def print_tree(self): 
        print(self.val) 
    
        if self.children: 
            for child in self.children: 
                child.print_tree()

def find_player(valley):
    for i in range(len(valley)):
        for j in range(len(valley[0])):
            if valley[i][j] == 'E':
                return i, j

# updates the blizzards and returns a list of the new blizzards
def update_blizzards(valley, blizzards):
    new_blizzards = []
    for i,j,direction in blizzards:
        if direction == '^':
            next_position = (i-1,j,direction)
        elif direction == 'v':
            next_position = (i+1,j,direction)
        elif direction == '<':
            next_position = (i,j-1,direction)
        elif direction == '>':
            next_position = (i, (j+1),direction)
        # check for the start or end points
        #if next_position != start_position or next_position != end_position:
        if next_position[0] == 0: # top row wall
            next_position = (len(valley) - 2, next_position[1], next_position[2])
        if next_position[0] == len(valley) - 1: # bottom row wall
            next_position = (1, next_position[1], next_position[2])
        if next_position[1] == 0: # left wall
            next_position = (next_position[0], len(valley[0]) - 2, next_position[2])
        if next_position[1] == len(valley[0]) - 1: # right wall
            next_position = (next_position[0], 1, next_position[2])

        new_blizzards.append(next_position)
        
    r, s = find_player(valley)
    # clean the old blizzards    
    for i, j, direction in blizzards:
        valley[i] = valley[i][:j] + '.' + valley[i][j+1:]
    # add the new one
    for i, j, direction in new_blizzards:
        d = direction
        if valley[i][j] != '.' and valley[i][j] != '#': # there is another blizzard in
            d = '2'
        valley[i] = valley[i][:j] + d + valley[i][j+1:]
    print(new_blizzards)
    return new_blizzards

def update_player(valley, player, new_position):
    global root
    copy_valley = []
    for i in range(len(valley)):
        copy_valley.append(valley[i])
    p1, p2 = player
    i, j = new_position
    # change player position to '.'
    copy_valley[p1] = valley[p1][:p2] + '.' + valley[p1][p2+1:]
    # change new position to 'E'
    copy_valley[i] = valley[i][:j] + 'E' + valley[i][j+1:]
    print_valley(copy_valley)

    # Create a new node with the updated position and valley
    new_node = Node(new_position, copy_valley)
    # Update the root to be the current node
    root = new_node
    return copy_valley

def print_valley(valley):
  # Print the valley map
  for row in valley:
    print(row)

def blizzard_basin(valley, start, end, wait_count):
  # Initialize a queue with the start position and a visited set
  queue = deque([start])
  visited = set()

  # Initialize the number of minutes to 0
  minutes = 0

  # Initialize the blizzards' positions
  blizzards = []
  for i in range(len(valley)):
    for j in range(len(valley[0])):
      if valley[i][j] in ('^', 'v', '<', '>'):
        blizzards.append((i, j, valley[i][j]))

  # While the queue is not empty
  while queue:
    # Get the size of the queue
    size = len(queue)

    # Iterate through the queue
    for i in range(size):
      # Get the current position
      row, col = queue.popleft()
      print('E'+':',row, col)
      #print_valley(valley)
      # Check if the current position is the end position
      if (row, col) == end:
        return minutes

      # Mark the current position as visited
      visited.add((row, col))

      blizzards = update_blizzards(valley, blizzards)
      # Calculate the next set of possible positions, including the current position
      next_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row, col)]
      # Iterate through the next positions
      for r, c in next_positions:
        # Check if the position is valid (not a wall or already visited) and not occupied by a blizzard
        if r < 0 or r >= len(valley) or c < 0 or c >= len(valley[0]) or valley[r][c] == '#':
          continue
        occupied = False
        for i, j, direction in blizzards:
          if i == r and j == c:
            occupied = True
            break
        if occupied:
          continue

        # If the 'E' is waiting in the same position for more than the maximum allowed number of minutes, return -1
        if (r, c) == (row, col) and minutes >= wait_count:
          return -1
        valley = update_player(valley, (row,col), (r,c))
        # Add the position to the queue
        queue.append((r, c))

    # Increase the number of minutes
    minutes += 1
  # Return -1 if the end position is not reached
  return -1





valley = []
with open('input24.txt', 'r') as f:
    for line in f:
        valley.append(line.strip())
    

start = (0, 1)
end = (5, 7)
max_wait = 15
# Initialize the root node with the starting position and valley
root = Node(start, valley)
print('Minutes:', blizzard_basin(valley, start, end, max_wait))
print('root')
root.print_tree()