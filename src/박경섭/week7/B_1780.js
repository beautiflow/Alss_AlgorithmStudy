const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const n = +input[0];
const paper = input.slice(1).map(v => v.split(" ").map(vv => +vv));

const countP = n =>{
    const count = [0,0,0];
    const recursive = (n,x,y) => {
        const num = paper[y][x];
        let numCount = 0;
        for (let i = 0; i < n; i++){
            for(let j = 0; j < n; j++){
                if(paper[y+j][x+i] === num) numCount++;
                else break;
            }
        }
        if(numCount === n*n) count[num+1]++;
        else{
            n /= 3;
            for(let i = 0; i < 3; i++){
                for(let j = 0; j < 3; j++){
                    recursive(n, x+i*n, y+j*n);
                }
            }
        }
    }
    recursive(n,0,0);
    console.log(count.join("\n"));

};
countP(n);