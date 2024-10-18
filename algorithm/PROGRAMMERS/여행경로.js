function solution(tickets) {
  let answer = [];
  const result = [];
  const visited = [];
  // 정렬
  tickets.sort();
  
  const len = tickets.length;
  const dfs = (str, count) => {
    result.push(str);

    // dfs 종료
    if(count === len) {
      answer = result;
      return true;
    }
    
    for(let i = 0; i < len; i++) {
      if(!visited[i] && tickets[i][0] === str) {
        visited[i] = true;
        
        if(dfs(tickets[i][1], count+1)) return true;
        
        visited[i] = false;
      }
    }
    
    result.pop();
    
    return false;
  }
  
  dfs("ICN", 0);
  
  return answer;
}
