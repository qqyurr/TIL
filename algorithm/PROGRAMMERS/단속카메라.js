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
