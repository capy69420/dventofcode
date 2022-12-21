import math

# mixing  move each number
# > or < in the file
# n positions, n being the number to move
# using % operator
# move each number in order of appearance
def move(L, index, value):
    length = len(L)
    step = 1
    # in case value is negative change the swap direction
    if value < 0:
        step = -1
    for i in range(0, value, step):
        # if it is the last element in the list and move it to the right
        # remove it then put it at the beginning of the list
        if step == 1 and (index + i + 1) % length == 0:
            # remove it
            tmp = L.pop()
            # insert it on index 1
            L.insert(1, tmp)
        # if it is the first element in the list and move it to left
        elif step == -1 and (index + i) % length == 0:
            # remove it
            tmp = L.pop(0)
            # inser it on the last index - 1
            L.insert(length - 1, tmp)
        else:
            # swap a value with the next
            tmp = L[(index + i) % length]
            L[(index + i) % length] = L[(index + i + step) % length]
            L[(index + i + step) % length] = tmp
        

def sum_grove_coordinates(L, index_0):
    # look at the 1000th, 2000th and 3000th after 0
    return L[(index_0 + 1000) % len(L)] + L[(index_0 + 2000) % len(L)] + L[(index_0 + 3000) % len(L)]

L = []
with open('input20.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        L.append(num)
        
    copy_L = L.copy()
    print(L)
    # decript the list L while keeping the copy
    for i in range(len(L)):
        # get the index of the value that was originaly in the position i
        index_value = L.index(copy_L[i])
        value = copy_L[i]
        # move L[index_value] value times to the right or left position(positive or negative)
        move(L, index_value, value)
        print(L)
    print(sum_grove_coordinates(L, L.index(0)))