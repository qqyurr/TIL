function solution(scores) {
    const [wanhoA, wanhoB] = scores[0];
    
    const filter = scores.filter(([a,b]) => a+b > wanhoA + wanhoB);

    let noIncentive = false
    filter.forEach(([a,b]) => {
        if(a > wanhoA && b > wanhoB){
            noIncentive = true
        }
    })
    
    if(noIncentive) return -1;
    
    let count = 0
    filter.sort((a,b) => a[0]+a[1] - (b[0] + b[1]))
    
    for (let i=0;i<filter.length;i++){
        const [a,b] = filter[i]
        for(let j=i+1;j<filter.length;j++){
            const [x,y] = filter[j]
            if(a < x && b < y){
            count += 1
            break
            }
        }
    }

    return filter.length + 1 - count;
}
