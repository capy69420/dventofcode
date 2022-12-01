import functools

elfList = open('./input.txt').read().split('\n\n')
elfsCalories = []
elfs2dArray = []
for elf in elfList:
    arr = elf.split('\n')
    elfs2dArray.append(arr)
    elfsCalories.append(
    int(functools.reduce(lambda a, b: int(a) + int(b), arr))
    )
max = functools.reduce(lambda a, b: int(a) if int(a) > int(b) else int(b), elfsCalories)
print('Elf carrying the most Calories:',max)
max_index = elfsCalories.index(max)
print('Elf index:',max_index)
print('Elf calories:',elfs2dArray[max_index])
caloriresRank = sorted(elfsCalories,reverse=True)
top3 = 0
for i in range(0,3):
    top3 += int(caloriresRank[i])
print('Sum of top 3 (calories):',top3)