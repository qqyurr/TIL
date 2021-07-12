function solution(record) {
  let answer = [];
  let actionList = [];
  // object 형태로 user list 만들기
  // 오브젝트를 활용해야 등록, 수정을 한 번에 해결할 수 있다.
  let nickObj = {};
  for (let i = 0; i < record.length; i++) {
    let input = record[i].split(" ");
    if (input[0] === "Enter") {
      // 닉네임 변경 : 원래 있던 id면 변경, 신규 id면 새로 등록
      nickObj[input[1]] = input[2];
      // 들어온 행동 추가 : 출력될 행동들 저장
      actionList.push({ Action: input[0], Id: input[1] });
    } else if (input[0] === "Leave") {
      // 나간 행동 추가 : 출력될 행동들 저장
      actionList.push({ Action: input[0], Id: input[1] });
    } else {
      // 닉네임 변경 : 원래 있던 id 변경
      nickObj[input[1]] = input[2];
    }
  }
  // 결과 출력
  for (let i = 0; i < actionList.length; i++) {
    if (actionList[i].Action === "Enter") {
      answer.push(`${nickObj[actionList[i].Id]}님이 들어왔습니다.`);
    } else {
      answer.push(`${nickObj[actionList[i].Id]}님이 나갔습니다.`);
    }
  }
  return answer;
}
