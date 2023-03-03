const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');


let len = input.shift();
let result = [];

for (let i = 0; i < len; i++) {
    let cnt = 0;
    for(item of input[i]){
        cnt += item ==="(" ? 1 : -1;

        if (cnt < 0) break;
    }

    result.push(cnt === 0 ? "YES" : "NO");

}

console.log(result.join("\n"));