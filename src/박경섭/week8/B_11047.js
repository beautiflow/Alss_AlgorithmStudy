const fs = require('fs');
let [N, ...nums] = fs.readFileSync('./dev/stdin').toString().trim().split(/\s+/).map(Number);

let price = nums.shift();
nums.sort((a, b) => b - a);

let count = 0;

while(price != 0){
    if(nums[0] > price){
        nums.shift();
    }
    else{
        count += parseInt(price / nums[0]);
        price = price % nums[0];
    }


}

console.log(count)
