const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');


let len = Number(input[0]);

let top = input[1].split(" ");

let stack = [];

let result = new Array(len).fill(0);

for (let i = len - 1; i >= 0; i--){

    if(stack.length != 0 && parseInt(top[stack[stack.length-1]]) < parseInt(top[i])){

        while(parseInt(top[stack[stack.length - 1 ]]) < parseInt(top[i])){

            let x = stack.pop();
            result[x] = i + 1;
        }
    }

    stack.push(i);
}

console.log(result.join(" "));
