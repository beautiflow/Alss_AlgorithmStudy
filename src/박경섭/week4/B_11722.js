const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let testCase = input.shift()
let inputs = input[0].split(' ').map(v=>Number(v)); 
let dp = []

for(let i=0; i<testCase;i++){
    let max = 0;
    for(let j=0;j<i;j++){
        if(inputs[i]<inputs[j]&&dp[j]>max){
            max=dp[j]
        }
    }
    dp[i] = max + 1
}
console.log(Math.max(...dp))