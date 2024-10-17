function solution(number, k) {
    const stack = [];
    let removeCount = k;

    for (let i = 0; i < number.length; i++) {
        const current = number[i];

        // 스택의 top보다 현재 숫자가 클 경우 제거
        while (removeCount > 0 && stack.length > 0 && stack[stack.length - 1] < current) {
            stack.pop();
            removeCount--;
        }
        stack.push(current);
    }

    // 만약 제거할 횟수가 남아있다면 뒤에서부터 제거
    while (removeCount > 0) {
        stack.pop();
        removeCount--;
    }

    return stack.join('');
}
