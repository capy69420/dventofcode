import {readFileSync, promises as fsPromises} from 'fs'

function syncReadFile(filename) {
    const content = readFileSync(filename, 'utf8')
    const elfArr = content.split(/\r\n\r\n/)
    let caloriesArr = elfArr.map(x => x.split(/\r\n/))
    return caloriesArr.map(x => x.map(y=>Number(y)))    // array of elfs each contains an array of calories
}

const input = syncReadFile('./input.txt')
//const sortedCalories = input.map(caloriesArr => caloriesArr.sort((a,b)=>( b-a )))
const arr = input.map(caloriesArr => caloriesArr.reduce((acc,val) => acc + val))
console.log(Math.max.apply(arr,Math))
console.log(arr.indexOf(Math.max.apply(arr,Math)))