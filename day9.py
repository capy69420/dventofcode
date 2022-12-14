# Define a function to simulate the movement of the head and tail of the rope
def simulate_rope_movement(motions):
  # Set the initial positions of the head and tail to be overlapping
  head_pos = (0, 0)
  tail_pos = (0, 0)

  # Keep track of the positions that the tail has visited
  visited_positions = set()
  
  # Iterate over the motions of the head
  for motion in motions:
    # Update the position of the head based on the motion
    direction = motion[0]
    distance = int(motion[1])

    # Loop over the range of the distance and apply the motion for each step
    for step in range(1, distance + 1):
        prev_head_pos = head_pos
        if direction == "U":
            head_pos = (head_pos[0], head_pos[1] + 1)
        elif direction == "D":
            head_pos = (head_pos[0], head_pos[1] - 1)
        elif direction == "L":
            head_pos = (head_pos[0] - 1, head_pos[1])
        elif direction == "R":
            head_pos = (head_pos[0] + 1, head_pos[1])

        # Update the position of the tail based on the new position of the head
        # x distance between the head and the tail is 2, y distance is the same
        if head_pos[1] == tail_pos[1] and abs(head_pos[0] - tail_pos[0]) == 2:
            tail_pos = (tail_pos[0] + (head_pos[0] - tail_pos[0]) // 2, tail_pos[1])
        # y distance between the head and the tail is 2, x distance is the same
        elif head_pos[0] == tail_pos[0] and abs(head_pos[1] - tail_pos[1]) == 2:
            tail_pos = (tail_pos[0], tail_pos[1] + (head_pos[1] - tail_pos[1]) // 2)
        # diagonals distance 1 do nothing
        elif (abs(head_pos[0] - tail_pos[0]) == 1 and abs(head_pos[1] - tail_pos[1]) == 1):
            tail_pos = tail_pos
        elif head_pos[0] == tail_pos[0] and head_pos[1] == tail_pos[1]:
            tail_pos = tail_pos
        # diagonal distance 2
        else:
            tail_pos = prev_head_pos
        
        # Add the position of the tail to the set of visited positions
        print(tail_pos, head_pos)
        visited_positions.add(tail_pos)

  # Return the number of unique positions visited by the tail
  print(visited_positions)
  return len(visited_positions)

# Read the input from the file "input9.txt"
with open("./input9.txt") as f:
  # Parse the input into a list of motions
  motions = [(line.split()[0], int(line.split()[1])) for line in f]

# Simulate the movement of the rope and print the result
result = simulate_rope_movement(motions)
print(result)