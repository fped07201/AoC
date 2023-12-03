import fs from 'fs'

let count = 0;
const data_lines = (fs.readFileSync("input.txt", 'utf-8')).split('\n')
    .map(str => Number(str));

const averageList = [];

for(let i = 2; i < data_lines.length; i++) {
    averageList.push((data_lines[i-2])+data_lines[i-1]+data_lines[i]);
}

for (let i = 1; i < (averageList.length); i++) {
    if (averageList[i] > averageList[i-1]) {
        count++;
    }
}
console.log(count);
