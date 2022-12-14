import ast

def is_in_order(left, right):
    # both intergers
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        return 0
    # left is an integer
    elif isinstance(left, int):
        return is_in_order([left], right)
    # right is an integer
    elif isinstance(right, int):
        return is_in_order(left, [right])
    # both lists
    elif isinstance(left, list) and isinstance(right, list):
        # both empty lists
        if len(left) == 0 and len(right) == 0:
            return 0
        # left is empty
        if len(left) == 0:
            return 1
        # right is empty
        if len(right) == 0:
            return -1
        # compare the first element of each list
        l = left[0]
        r = right[0]
        res = is_in_order(l,r)
        # compare the rest of the list
        if res == 0:       
            return is_in_order(left[1:], right[1:])
        # l < r or l > r either returns 1 or -1
        else:
            return res

def get_order_sum(file):
    order_sum = 0
    with open(file) as f:
        data = f.read()
        data = data.split('\n\n')
        for i in range(len(data)):
            pair = data[i].split('\n')
            left = ast.literal_eval(pair[0])
            right = ast.literal_eval(pair[1])
            res = is_in_order(left, right)
            if res == 1:
                 order_sum += i+1      
    return order_sum

print('order sum:',get_order_sum('./input13.txt'))
