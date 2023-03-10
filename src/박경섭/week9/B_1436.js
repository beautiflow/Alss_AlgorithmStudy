const input = require('fs').readFileSync('./inputForJS.txt').toString().trim()

const n = +input
let count = 0;

for(let i = 666 ; i < Number.MAX_SAFE_INTEGER ; i++ ){
    if (String(i).indexOf('666') !== -1){
        count++
    }

    if(count === n){
        console.log(i)
        break
    }
    
}