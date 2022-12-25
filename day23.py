# print the map
def print_map(g):
    max_row, max_col = len(g), len(g[0])
    map = []
    for m in g:
        print(m)


def remove_empty_space(elves,grove):
    rows, cols = len(grove), len(grove[0])
    new_grove = []
    start_row, end_row = 0, rows
    start_col, end_col = 0, cols
    elf_found = False
    for i in range(rows): # first row
        if elf_found:
            break
        for j in range(cols):
            if (i,j) in elves:
                start_row = i
                elf_found = True
                break
    elf_found = False
    for i in range(rows - 1, -1, -1): # last row moving backwards
        if elf_found:
            break
        for j in range(cols):
            if (i,j) in elves:
                end_row = i + 1
                elf_found = True
                break
    elf_found = False
    for j in range(cols):
        for i in range(start_row, end_row+1):
            if (i,j) in elves:
                start_col = j
                elf_found = True
                break
        if elf_found:
            break
    elf_found = False
    for j in range(cols - 1,0, -1):
        for i in range(start_row, end_row):
            if (i,j) in elves:
                end_col = j + 1
                elf_found = True
                break
        if elf_found:
            break
    print(start_row,end_row)
    print(start_col,end_col)
    j = 0
    for i in range(start_row, end_row):
        new_grove.append(grove[i][start_col:end_col])
        print(new_grove[j])
        j += 1
    print('new grove len:', len(new_grove))
    return new_grove

def update_grove(grove, elves):
    max_row, max_col = len(grove), len(grove[0])
    map = []
    for i in range(max_row):
        for j in range(max_col):
            if (i,j) in elves:
                string = grove[i]
                grove[i] = string[:j] + '#' + string[j+1:]
            else:
                string = grove[i]
                grove[i] = string[:j] + '.' + string[j+1:]
    
def increase_grove_size(grove):
    rows, cols = len(grove), len(grove[0])
    new_grove = []
    for i in range(rows + 2):
        new_row = []
        for j in range(cols + 2):
            if i < 2 or i >= rows + 2 or j < 2 or j >= cols + 2:
                new_row.append('.')
            else:
                new_row.append(grove[i - 2][j - 2])
        new_grove.append(new_row)
    return new_grove

# return True if there is an elf in the direction
def has_elf_in_direction(pos, direction, grove):
    rows, cols = len(grove), len(grove[0])
    row, col = pos
    if direction == "N":
        positions = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
    elif direction == "S":
        positions = [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    elif direction == "W":
        positions = [(row - 1, col - 1), (row, col - 1), (row + 1, col - 1)]
    elif direction == "E":
        positions = [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
    else:
        raise ValueError("Invalid direction: {}".format(direction))

    for position in positions:
        row, col = position
        if (row >= 0 and row < rows and col >= 0 and col < cols and
                grove[row][col] == "#"):
            return True
    return False

# return false if there is another elf around
def no_elf_around(elf, grove):
    rows, cols = len(grove), len(grove[0])
    row, col = elf
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for direction in directions:
        row_offset, col_offset = direction
        if (row + row_offset >= 0 and
                row + row_offset < rows and
                col + col_offset >= 0 and
                col + col_offset < cols and
                grove[row + row_offset][col + col_offset] == "#"):
            return False

    return True

def extract_elves(grove, max_rounds):
    rows, cols = len(grove), len(grove[0])
    directions = ["N", "S", "W", "E"]
    elves = []
    proposed_destinations = {}

    # Find the positions of all Elves in the grove
    for i in range(rows):
        for j in range(cols):
            if grove[i][j] == "#":
                elves.append((i, j))
    print('initial state:')
    print_map(grove)
    # Simulate the extraction process
    for round in range(max_rounds):
        # Consider proposed moves for each Elf
        for elf in elves:
            row, col = elf
            proposed_destination = elf
            if  no_elf_around(elf, grove):
                break # do nothing
            for direction in directions:
                if direction == "N":
                # proposal destination is outside the map size range
                    if row - 1 < 0:
                        increase_grove_size(grove)
                    if not has_elf_in_direction(elf, direction, grove):
                        proposed_destination = (row - 1, col)
                elif direction == "S":
                    if row + 1 >= rows:
                        increase_grove_size(grove)
                    if not has_elf_in_direction(elf, direction, grove):
                        proposed_destination = (row + 1, col)
                elif direction == "W":
                    if col - 1 < 0:
                        increase_grove_size(grove)
                    if not has_elf_in_direction(elf, direction, grove):
                        proposed_destination = (row, col - 1)
                elif direction == "E":
                    if col + 1 >= cols:
                        increase_grove_size(grove)
                    if not has_elf_in_direction(elf, direction, grove):
                        proposed_destination = (row, col + 1)
                else:
                    raise ValueError("Invalid direction: {}".format(direction))


                # Check if the proposed destination is valid
                # not another elf in the proposed destination
                if (proposed_destination not in elves):
                    # Save the proposed destination for this Elf
                    proposed_destinations[elf] = proposed_destination
                    break

        # Move Elves to their proposed destinations
        for elf in elves:
            if elf in proposed_destinations:
                destination = proposed_destinations[elf]
                # This Elf can move to the proposed destination
                elves.remove(elf)
                elves.append(destination)
                
        update_grove(grove, elves)
        print('round:', round+1)
        print_map(grove)

    print('map:')
    map = remove_empty_space(elves, grove)
    for i in range(len(map)):
        print(map[i])
    #open a file in write mode
    f = open("./sample.txt", "w")

    #write a line to the file
    for t in map:
        f.write(t +'\n')

    #close the file
    f.close()
    # find the maximum i,j in elves
    max_row, max_col = 0,0
    min_row, most_left = len(grove),len(grove[0])
    for i, j in elves:
        if i < min_row:
            min_row = i
        if i > max_row:
            max_row = i
        if j > max_col:
            max_col = j
        if j < most_left:
            most_left = j

    # print map
  
    print(max_row, min_row)
    print(most_left, max_col)
    print('rows', len(map))
    print('cols', len(map[0]))
    print('elves',len(elves))
    return (len(map)+1) * (len(map[0])+1)

grove = []
with open('input23.txt', 'r') as f:
    for line in f:
        grove.append(line.strip())
# Example input

result = extract_elves(grove, 10)
print(result)
