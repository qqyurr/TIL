function solution(answers) {
    const numberOneAnswer = [1, 2, 3, 4, 5];
    const numberTwoAnswer = [2, 1, 2, 3, 2, 4, 2, 5];
    const numberThreeAnswer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let resultDict = {1: 0, 2: 0, 3: 0};
    
    for (let i = 0; i < answers.length; i++) {
        if (numberOneAnswer[i % numberOneAnswer.length] === answers[i]) {
            resultDict['1'] = resultDict['1'] + 1;
        }
        if (numberTwoAnswer[i % numberTwoAnswer.length] === answers[i]) {
            resultDict['2'] = resultDict['2'] + 1;
        }
         if (numberThreeAnswer[i % numberThreeAnswer.length] === answers[i]) {
            resultDict['3'] = resultDict['3'] + 1;
        }
    }
    
    const maxCount = Math.max(...Object.values(resultDict));
    const answer = Object.entries(resultDict)
    .filter(([a,b]) => b === maxCount)
    .map(([x,y])=> Number(x));
    
    return answer;
}
