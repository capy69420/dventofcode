# part 1
# recursively replace the values and evaluate the equation
def get_number(monkey, jobs):
    if monkey.isdigit():
        return int(monkey)
    else:
        parts = jobs[monkey].split(' ')
        if len(parts) == 1:
            return get_number(parts[0], jobs)
        else:
            a = get_number(parts[0], jobs)
            b = get_number(parts[2], jobs)
            if parts[1] == '+':
                return a + b
            elif parts[1] == '-':
                return a - b
            elif parts[1] == '*':
                return a * b
            elif parts[1] == '/':
                return a / b

# part 2
# return True if humn is in the monkey equation
def find_humn(monkey, jobs):
    if monkey == 'humn':
        return True
    elif monkey.isdigit():
        return False
    else:
        parts = jobs[monkey].split(' ')
        if len(parts) == 1:
            return find_humn(parts[0],jobs)
        else:
            res1 = find_humn(parts[0],jobs)
            res2 = find_humn(parts[2],jobs)
            if res1 or res2:
                return True
            else:
                return False

# solve the equation to find humn value equal result
def solve_equation(monkey, jobs, result):
    if monkey == 'humn':
        return result
    elif monkey.isdigit():
        return int(monkey)
    else:
        parts = jobs[monkey].split(' ')
        if len(parts) == 1:
            solve_equation(parts[0], jobs, result)
        else:
            # get the part that is possible to calculate
            calc_part = 0
            humn_part = 0
            if find_humn(parts[0], jobs):
                calc_part = 2
                humn_part = 0
            else:
                calc_part = 0
                humn_part = 2
            # get the sub result
            sub_res = get_number(parts[calc_part], jobs)
            new_result = 0
            if parts[1] == '+':
                new_result = result - sub_res
            elif parts[1] == '-':
                if calc_part == 2:
                    new_result = result + sub_res
                else:
                    new_result = sub_res - result
            elif parts[1] == '*':
                new_result = result / sub_res
            elif parts[1] == '/':
                if calc_part == 2:
                    new_result = result * sub_res
                else:
                    new_result = sub_res / result
            # solve the equation left
            return solve_equation( parts[humn_part], jobs, new_result)

# find the humn value so parts[0] == parts[2] of the monkey equation         
def find_humn_number(monkey, jobs):
    parts = jobs[monkey].split(' ')
    res = 0
    index = 0
    if find_humn(parts[0], jobs):
        res = get_number(parts[2], jobs)
    else:
        index = 2
        res = get_number(parts[0], jobs)
    # solve the equation res = get_number(parts[index], jobs) to find the value of humn
    return solve_equation(parts[index], jobs, res)

monkeys = {}
with open('input21.txt', 'r') as f:
    for line in f:
        name = line.split(':')[0].strip()
        job = line.split(':')[1].strip()
        monkeys[name] = job
    
    print(get_number('root', monkeys))
    print(find_humn_number('root', monkeys))