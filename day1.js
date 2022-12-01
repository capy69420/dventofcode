import {readFileSync, promises as fsPromises} from 'fs'

function syncReadFile(filename) {
    const content = readFileSync(filename, 'utf8')
    const elfArr = content.split(/\r\n\r\n/)
    const caloriesArr = elfArr.map(x => x.split(/\r\n/))
    return caloriesArr.map(x => x.map(y=>Number(y)))    // array of elfs each contains an array of calories (interger)
}

const input = syncReadFile('./input.txt')
const sortedCalories = input.map(x=>x.reduce((acc, curr)=>acc+curr)).sort((a,b)=>b-a)
console.log('Top calories Elf: ' + sortedCalories[0])
let top3 = 0
for (let i=0; i<3; i++) {
    top3 += sortedCalories[i]
}
console.log('Top 3 sum of calories: ' + top3)