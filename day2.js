import {readFileSync, promises as fsPromises} from 'fs'

function syncReadFile(filename) {
    const content = readFileSync(filename, 'utf8')
    let moves = content.split(/\r\n/)
    moves = moves.map(x => x.split(' '))
    return moves
}
function matchScore(p2, p1) {
    if (p2=='A' && p1=='X')
        return 4 // 3 + 1 draw + rock
    if (p2=='A' && p1=='Y')
        return 8 // 6 + 2 win + paper
    if (p2=='A' && p1=='Z')
        return 3 // 0 + 3 lose + scissors
    if (p2=='B' && p1=='X')
        return 1 // 0 + 1 lose + rock
    if (p2=='B' && p1=='Y')
        return 5 // 3 + 2 draw + paper
    if (p2=='B' && p1=='Z')
        return 9 // 6 + 3 win + scissors
    if (p2=='C' && p1=='X')
        return 7 // 6 + 1 win + rock
    if (p2=='C' && p1=='Y')
        return 2 // 0 + 2 lose + paper
    if (p2=='C' && p1=='Z')
        return 6 // 3 + 3 draw + scissors     
    return 0
}

const input = syncReadFile('./input2.txt')
console.log(input)
let totalScore = 0
for ( let i = 0; i < input.length; i++ ) {
    totalScore += matchScore(input[i][0],input[i][1])
}
console.log('total score: '+totalScore)
let outcomeScore = 0
for ( let i = 0; i < input.length; i++ ) {
    outcomeScore += matchOutcomeScore(input[i][0],input[i][1])
}
console.log('outcome score: '+outcomeScore)
//part 2



/*
Points per selected move:
    1 rock      X   A
    2 paper     Y   B
    3 scissors  Z   C
Points per outcome:
    lose 0
    draw 3
    win  6
score = moveScore + outcomeScore
matchScore(p2,p1)
p2 oponent, p1 yourself
part2
    X lose  0       A   1
    Y draw  3       B   2
    Z win   6       C   3
*/
function matchOutcomeScore(p2, outcome) {
    if ( outcome == 'X') {//lose
        if (p2 == 'A')
            return 3 // 0 + 3 scissors
        if (p2 == 'B')
            return 1 // 0 + 1 rock
        if (p2 == 'C')
            return 2 // 0 + 2 paper
    }
    if ( outcome == 'Y') {//draw
        if (p2 == 'A')
            return 4 // 3 + 1 rock
        if (p2 == 'B')
            return 5 // 3 + 2 paper
        if (p2 == 'C')
            return 6 // 3 + 3 scissors
    }
    if ( outcome == 'Z') {//win
        if (p2 == 'A')
            return 8 // 6 + 2 paper
        if (p2 == 'B')
            return 9 // 6 + 3 scissors
        if (p2 == 'C')
            return 7 // 6 + 1 rock
    }
    return 0

}