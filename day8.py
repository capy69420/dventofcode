matrix = []    
# open input8.txt file
with open("input8.txt", "r") as f:
    # iterate through each line
    for line in f:
        # store line in a list
        rows = line.split()
        for i in rows:
            # separate each digit
            row = [int(h) for h in i]
            matrix.append(row)


def left_score(matrix, i, j):
    count = 0
    k = j - 1
    while (k >= 0):
        count += 1
        if (matrix[i][k] >= matrix[i][j]):
            return count   
        k -= 1
    return count
def right_score(matrix, i, j):
    count = 0
    k = j + 1
    while (k < len(matrix[i])):
        count += 1
        if (matrix[i][k] >= matrix[i][j]):
            return count   
        k += 1
    return count
def up_score(matrix, i, j):
    count = 0
    k = i - 1
    while (k >= 0):
        count += 1
        if (matrix[k][j] >= matrix[i][j]):
            return count   
        k -= 1
    return count
def down_score(matrix, i, j):
    count = 0
    k = i + 1
    while (k < len(matrix)):
        count += 1
        if (matrix[k][j] >= matrix[i][j]):
            return count   
        k += 1
    return count

def visible_left(matrix, i, j):
    k = j - 1
    while (k >= 0):
        if (matrix[i][k] >= matrix[i][j]):
            return False
        k -= 1
    return True

def visible_right(matrix, i, j):
    k = j + 1
    while (k < len(matrix[i])):
        if (matrix[i][k] >= matrix[i][j]):
            return False
        k += 1
    return True

def visible_up(matrix, i, j):
    k = i - 1
    while (k >= 0):
        if (matrix[k][j] >= matrix[i][j]):
            return False
        k -= 1
    return True

def visible_down(matrix, i, j):
    k = i + 1
    while (k < len(matrix)):
        if (matrix[k][j] >= matrix[i][j]):
            return False
        k += 1
    return True
max_pos = []
max_score = 0
# set counter for visible trees
visible_trees = 0
# edge visible trees
col = len(matrix)
row = len(matrix[0])
visible_trees += col * 2 + row*2 - 4
# iterate through the matrix without borders
for i in range(1,len(matrix)-1):
    for j in range(1,len(matrix[i])-1):
        # for each i,j look for higher values up, right, down and left
        score = left_score(matrix,i,j) * right_score(matrix,i,j) * up_score(matrix,i,j) * down_score(matrix,i,j)
        if score > max_score:
            max_score = score
            max_pos = [i,j]
        left = visible_left(matrix,i,j)
        right = visible_right(matrix,i,j)
        up = visible_up(matrix,i,j)
        down = visible_down(matrix,i,j)
        if (left or right or up or down):
            visible_trees += 1

# print total number of visible trees
print("The total number of visible trees is", visible_trees)
print("The max score is", max_score,'and coordinates are:', max_pos)