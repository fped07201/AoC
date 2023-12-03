import fs from 'fs'

let count = 0;

const data_lines = (fs.readFileSync("input.txt", 'utf-8')).split('\n')
    .map(str => Number(str));

for (let i = 1; i < data_lines.length; i++) {
    if (data_lines[i] > data_lines[i-1]) {
        count++;
    }
}
console.log(count);
