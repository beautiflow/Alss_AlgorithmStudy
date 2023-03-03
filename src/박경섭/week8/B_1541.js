let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('-');

input = input.map((item) => {
    let newItem = item.split('+');
    // console.log(newItem)
    // console.log(newItem.reduce((a,b) => Number(a) + Number(b),0))
    return newItem.reduce((a,b) => Number(a) + Number(b),0)
    
});

console.log(input.reduce((a,b) => a - b))