const input = require('fs').readFileSync('./inputForJS.txt').toString().trim().split('\n');
const sol = (input) => {
    const n = +input.shift();
    const [r1, c1, r2, c2] = input[0].split(" ").map(Number);

    const direction = [
        [-2,-1],
        [-2,1],
        [0,-2],
        [0,2],
        [2,-1],
        [2,1],
    ]
    const visited = Array.from(Array(n), ()=> Array(n).fill(0))
    const queue = [[r1,c1,0]]
    visited[r1][c1] = 1;
    while (queue.length){
        const [x,y,cnt] = queue.shift()
        for(let [xi,yi] of direction){
            const nx = x+xi
            const ny = y + yi
            if(nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny]){
                visited[nx][ny] = 1
                if(nx === r2 && ny === c2){
                    return cnt + 1;
                }
                queue.push([nx,ny,cnt+1])
            }
        }
    }

    return -1

}
console.log(sol(input))

