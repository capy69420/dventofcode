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