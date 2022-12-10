# Read instructions from input file
with open('input10.txt', 'r') as f:
    instructions = f.readlines()

# Initialize the X register to 1 and the cycle counter to 0
x = 1
cycle = 0
signal_tuple = []

for instruction in instructions:
    # Split the instruction into the operation and value (if any)
    words = instruction.split()
    op = words[0]
    val = int(words[1]) if len(words) > 1 else None
    
    # Update the cycle counter based on the operation
    if op == 'addx':
        cycle += 1
        signal_tuple.append((cycle,x,instruction))
        cycle += 1
        signal_tuple.append((cycle,x,instruction))
        x += val
    else:
        cycle += 1
        signal_tuple.append((cycle,x,instruction))

sum = 0
# Calculate the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
# signal_tuple[k] is the strength at cycle k + 1
for k in [19, 59, 99, 139, 179, 219]:
    signal_strength = signal_tuple[k][0] * signal_tuple[k][1]
    cycle = k + 1
    print('Signal strength at cycle {}: {} x:{} i:{}'.format(cycle, signal_strength, signal_tuple[k][1], signal_tuple[k][2]))
    sum += signal_strength
print(sum)