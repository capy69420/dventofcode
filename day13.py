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

packets = []
def get_order_sum(file):
    order_sum = 0
    with open(file) as f:
        data = f.read()
        data = data.split('\n\n')
        for i in range(len(data)):
            pair = data[i].split('\n')
            left = ast.literal_eval(pair[0])
            right = ast.literal_eval(pair[1])
            packets.append(left)
            packets.append(right)
            res = is_in_order(left, right)
            if res == 1:
                 order_sum += i+1      
    return order_sum

div1, div2 = [[2]], [[6]]
def bubble_sort(packets):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(packets)):
            # not in order
            sorted = is_in_order(packets[i-1], packets[i])
            if sorted == -1:
                # swap them
                temp = packets[i]
                packets[i] = packets[i-1]
                packets[i-1] = temp
                swapped = True
    return packets
def decoder_key(packets, div):
    index = 1
    packets.insert(0, div)
    for i in range(1, len(packets)):
        # sorted
        if is_in_order(div,packets[i]) == 1:
            return index
        # not sorted swap it
        else:
            temp = packets[i-1]
            packets[i-1] = packets[i]
            packets[i] = temp
            index += 1
    return index

print('order sum:',get_order_sum('./input13.txt'))
bubble_sort(packets)
key1 = decoder_key(packets,div1)
key2 = decoder_key(packets,div2)
print('decoder key:',key1 * key2)