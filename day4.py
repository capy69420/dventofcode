input = open('./input4.txt').read()
input = input.split('\n')
input_list = []
for i in input:
    input_list.append(i.split(','))

# Solution:

def find_overlaps(input_list):
  overlaps = 0
  for pair in input_list:
    sections1 = pair[0].split('-')
    sections2 = pair[1].split('-')
    if int(sections1[0]) <= int(sections2[0]) and int(sections1[1]) >= int(sections2[1]):
      overlaps += 1
    elif int(sections2[0]) <= int(sections1[0]) and int(sections2[1]) >= int(sections1[1]):
      overlaps += 1
  return overlaps

print(find_overlaps(input_list))

# Output: 2

# create list from input4.txt
assignment_pairs = []
with open('./input4.txt') as f:
    for line in f:
        assignment_pairs.append(line.strip())

# calculate the overlapping pairs
overlapping_pairs = 0
for pair in assignment_pairs:
    # convert to integer range
    pair_int_range = []
    for num in pair.split(','):
        pair_int_range.append(list(range(int(num.split('-')[0]), int(num.split('-')[1])+1)))

    # check if any of the ranges overlap
    for i in pair_int_range[0]:
        if i in pair_int_range[1]:
            overlapping_pairs += 1
            break

print(overlapping_pairs)