const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');


let len = input.shift();
let stack = [];

for(let i = 0; i < len; i++){
    let nowInput = input[i];
    if (nowInput == 0){
        stack.pop();
    }
    else{
        stack.push(parseInt(nowInput));
    }
    
    
}

if (stack.length === 0) {
    console.log(0);
}
else{
    let result = stack.reduce((sum,currv) => {
        return sum + currv;
    });

    console.log(result);

}