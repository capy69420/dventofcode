import math

# move the element in index a step and update the value
def move_step(L, index, step, value):
    # finished
    if value == 0:
        return L
    # border cases
    # index to move is the first element and the move is to the left
    elif index == 0 and step == -1:
        # remove it from the list
        temp = L.pop(0)
        # put it in place of the last - 1 element
        i = len(L)-2
        L.insert(i, temp)
        return move_step(L, i, step, value - step)
    # index is the last element and the move is to the right
    elif index == len(L)-1 and step == 1:
        # remove it from the list
        temp = L.pop()
        # insert it as second element in the list
        L.insert(1, temp)
        return move_step(L, 1, step, value - step)
    # index is a value in beetween or there is no need to move to the end/begining of the list
    else:
        # swap the values
        tmp = L[index]
        L[index] = L[index + step]
        L[index + step] = tmp
        return move_step(L, index + step, step, value - step)

def move_step_iterative(L, index, step, value):
    while value != 0:
        # border cases
        # index to move is the first element and the move is to the left
        if index == 0 and step == -1:
            # remove it from the list
            temp = L.pop(0)
            # put it in place of the last - 1 element
            i = len(L)-2
            L.insert(i, temp)
            index = i
        # index is the last element and the move is to the right
        elif index == len(L)-1 and step == 1:
            # remove it from the list
            temp = L.pop()
            # insert it as second element in the list
            L.insert(1, temp)
            index = 1
        # index is a value in between or there is no need to move to the end/beginning of the list
        else:
            # swap the values
            tmp = L[index]
            L[index] = L[index + step]
            L[index + step] = tmp
            index += step
        value -= step
    return L     

def sum_grove_coordinates(L, index_0):
    print(L[(index_0 + 1000) % len(L)])
    print(L[(index_0 + 2000) % len(L)])
    print(L[(index_0 + 3000) % len(L)])
    # look at the 1000th, 2000th and 3000th after 0
    return L[(index_0 + 1000) % len(L)] + L[(index_0 + 2000) % len(L)] + L[(index_0 + 3000) % len(L)]

L = []
with open('input20.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        L.append(num)
        
    copy_L = L.copy()
    # decript the list L while keeping the copy
    for i in range(len(L)):
        # get the index of the value that was originaly in the position i
        index_value = L.index(copy_L[i])
        value = copy_L[i]
        # move L[index_value] value times to the right or left position(positive or negative)
        step = 1
        # in case value is negative change the swap direction
        if value < 0:
            step = -1
        # move it value times using step
        L = move_step_iterative(L, index_value, step, value)
    print(sum_grove_coordinates(L, L.index(0)))