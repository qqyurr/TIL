// [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

function solution(routes) {
    let count = 0;
    let camera = -30001
    const sortedList = routes.sort((a, b) => a[1] - b[1]);
    
    sortedList.forEach((route) => {
        if (camera < route[0]) {
            count += 1;
            camera = route[1];
        }
    })
    
    return count;
}
