import { readFileSync, promises as fsPromises } from "fs"

function syncReadFile(filename) {
    const content = readFileSync(filename, 'utf8')
    return content
}

const input = syncReadFile('./input6.txt')