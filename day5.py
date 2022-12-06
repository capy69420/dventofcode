# read the content of input5.txt
with open('input5.txt', 'r') as f:
    data = f.read()

# split the data by '\n\n'
data = data.split('\n\n')

def createStacks():
    # create the stacks
    stack1 = ['H', 'C', 'R']
    stack2 = ['B', 'J', 'H', 'L', 'S', 'F']
    stack3 = ['R', 'M', 'D', 'H', 'J', 'T', 'Q']
    stack4 = ['S', 'G', 'R', 'H', 'Z', 'B', 'J']
    stack5 = ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B']
    stack6 = ['T', 'H', 'C', 'G']
    stack7 = ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L']
    stack8 = ['R', 'J', 'Q', 'G', 'C']
    stack9 = ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']

    # create a list of stacks
    stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]
    return stacks

def createLists(data):
    # create lists for origin, target and amount
    origin_list = []
    target_list = []
    amount_list = []

    moves_data = data[1].split('\n')
    # iterate through the data and store the origin, target and amount
    for line in moves_data:
        moves = line.split()
        amount_list.append(int(moves[1]))
        origin_list.append(int(moves[3]))
        target_list.append(int(moves[5]))
    return origin_list, target_list, amount_list

# create a list of stacks
stacks = createStacks()
origin_list, target_list, amount_list = createLists(data) 

# iterate through the list of origin, target and amount
for i in range(len(origin_list)):
    # find the origin and target stack
    origin_stack = stacks[origin_list[i] - 1]
    target_stack = stacks[target_list[i] - 1]
    # move the crates from origin to target
    for j in range(amount_list[i]):
        target_stack.append(origin_stack.pop())
       
    
# print the top crates of each stack
print("Top crates of each stack are:")
for stack in stacks:
    print(stack[-1], end='')
print('\n')

# part 2
stacks = createStacks()

origin_list, target_list, amount_list = createLists(data)

# iterate through the list of origin, target and amount
for i in range(len(origin_list)):
    # find the origin and target stack
    origin_stack = stacks[origin_list[i] - 1]
    target_stack = stacks[target_list[i] - 1]
    amount = amount_list[i]
    # move the crates from origin to target
    end = len(origin_stack)
    stacks[target_list[i] - 1].extend(origin_stack[end - amount:end])
    stacks[origin_list[i] - 1] = origin_stack[0:end - amount]

  
# print the top crates of each stack
print("Top crates of each stack are:")
for stack in stacks:
    print(stack[len(stack)-1], end='')
print('\n')
# print using -1 don't do it, can generate unexpected results
for stack in stacks:
    print(stack[-1], end='')