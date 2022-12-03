def compare_strings(string1, string2):
  result = ""
  for char in string1:
    if char in string2:
      result = char
  return result

def priority(item_type):
    if item_type.islower():
        return ord(item_type) - 96
    else:
        return ord(item_type) - 64 + 26

input = open('./input3.txt').read()
input = input.split('\n')

list = []
prio_sum = 0
for characters in input:
    list.append(characters)
    first_half = characters[0:int(len(characters)/2)]
    second_half = characters[int(len(characters)/2):]
    char = compare_strings(first_half, second_half)
    prio = priority(char)
    prio_sum += prio
    
print(prio_sum)


# part 2

# This function takes in a list of badges and calculates the total priority of all the badges.
# It iterates through the list in increments of three, creating a list of badges for each triplet.
# It then checks to see if all the triplets contain a common badge, and if they do, adds its priority to the total.
# Finally, it returns the sum of all the priorities.
def find_badge_priority(list): 
    sum = 0
    for i in range(0, len(list), 3): 
        badges = []
        for j in range(i, i+3): 
            for char in list[j]: 
                if char not in badges: 
                    badges.append(char) 
        common_badge = list[i][0] 
        for badge in badges: 
            all_contain = True 
            for k in range(i, i+3): 
                if badge not in list[k]: 
                    all_contain = False 
                    break 
            if all_contain: 
                common_badge = badge 
        sum += priority(common_badge) 
    print(sum)

find_badge_priority(list)