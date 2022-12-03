def matchScore(p2, p1):
    if   p2 == 'A' and p1 == 'X':
        return 4 # draw rock
    elif p2 == 'B' and p1 == 'X':
        return 1 # lost paper rock
    elif p2 == 'C' and p1 == 'X':
        return 7 # win scissors rock
    elif p2 == 'A' and p1 == 'Y':
        return 8 # win rock paper
    elif p2 == 'B' and p1 == 'Y':
        return 5 # draw paper
    elif p2 == 'C' and p1 == 'Y':
        return 2 # lost scissors paper
    elif p2 == 'A' and p1 == 'Z':
        return 3 # lost rock scissors
    elif p2 == 'B' and p1 == 'Z':
        return 9 # win paper scissors
    elif p2 == 'C' and p1 == 'Z':
        return 6 # draw scissors
def movePoints(m):
    if   m == 'A':
        return 1
    elif m == 'B':
        return 2
    elif m == 'C':
        return 3
    else:
        return 0
def oposite(m):
    
def matchOutcome(p2,outcome):
    if outcome == 'X': # lose
        return 0 + movePoints(oposite(p2))
    elif outcome == 'Y': # draw
        return 3 + movePoints(p2)
    elif outcome == 'Z': # win
        return 6 + movePoints(oposite(p2))
    else:
        return 0

input = open('./input2.txt').read()
input = input.split('\n')
score = 0
for i in range(len(input)):
    input[i] = input[i].split(' ')
    score += matchScore(input[i][0],input[i][1])
print('part 1 score:',score)

