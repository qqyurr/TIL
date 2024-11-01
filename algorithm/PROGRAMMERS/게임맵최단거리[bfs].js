function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const visited = Array.from({length:maps.length},()=> new Array(maps[0].length).fill(false));
    const dir = [[-1, 0], [1, 0], [0, -1], [0, 1]];
        
    const bfs = () => {
        let queue = [[0,0,1]] // 행,열,이동거리
        
        while (queue.length) {
            let [row, col, distance] = queue.shift();
            
            if (row === n-1 && col === m-1) {
                return distance;
            }
            
            for (let [x, y] of dir) {
                let newX = row + x;
                let newY = col + y;
                // isWall
                if (newX >= 0 && newX < n && newY >= 0 && newY < m && maps[newX][newY] === 1) {
                    if (!visited[newX][newY]) {
                        visited[newX][newY] = true;
                        queue.push([newX, newY, distance + 1]);
                    }
                    
                }
            }
        }
        
        return -1;
    }
   
    return bfs();
}
