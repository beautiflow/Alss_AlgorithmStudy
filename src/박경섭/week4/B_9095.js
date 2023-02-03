const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let testCase = input.shift()

let dp = [0,1,2,4]

for(let i=4; i<11; i++){
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
}

for(let i=0; i<testCase; i++) {
    console.log(dp[input[i]])
}