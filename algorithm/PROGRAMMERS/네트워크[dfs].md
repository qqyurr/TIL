# 네트워크

###### 문제 설명

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

##### 제한사항

- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
- 각 컴퓨터는 0부터 `n-1`인 정수로 표현합니다.
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
- computer[i][i]는 항상 1입니다.

##### 입출력 예

| n    | computers                         | return |
| ---- | --------------------------------- | ------ |
| 3    | [[1, 1, 0], [1, 1, 0], [0, 0, 1]] | 2      |
| 3    | [[1, 1, 0], [1, 1, 1], [0, 1, 1]] | 1      |

> 풀이

1. 첫 번째 컴퓨터와 연결된 컴퓨터 번호를 dfs()에 대입, answer += 1
2. visited 표시, 연결된 노드 찾기
   - 컴퓨터 번호와 같은 인덱스의 값이 1인 경우 and visited하지 않은 경우
   - 연결된 노드의 연결된 노드를 찾기 위해 dfs() 다시 실행
3. 한 dfs가 끝날 때(더 이상 시작점으로부터 연결된 노드가 없을 때) answer += 1

```python
def dfs(idx, computers, n):
    visited[idx] = True
#   연결된 노드 찾기
    for i in range(n):
        if computers[idx][i] == 1 and visited[i] == False:
#           연결된 노드 찾기
            dfs(i, computers, n)
    
def solution(n, computers):
    global visited
    answer = 0
    visited = [False]*n
    for idx in range(n):
        if visited[idx] == False:
            dfs(idx, computers, n)
            answer += 1
    return answer
```

```javascript
function solution(n, computers) {
    var answer = 0;
    const visited = Array.from({length: n}, () => false)
    
    function dfs(idx, computers, n){
        visited[idx] = true
        for (let i = 0; i<n ; i ++){
            if (computers[idx][i]===1 && visited[i]===false){
                dfs(i, computers,n)
            }
        }
    }
    for (let idx = 0 ; idx < n ; idx++){
        if (visited[idx] === false) {
            dfs(idx, computers, n)
            answer += 1
        }
    }

    return answer;
}
```

>for문에서 i와 idx의 값을 const로 선언했는데 돌아가지 않았다. let으로 했더니 잘 돌아갔다. let은 변수에 재할당이 가능하지만, const는 재선언, 재할당이 모두 불가능하기 때문이다.

##### for에서 var를 사용하면 안되는 이유

```javascript
var functions = [];

for (var i = 0; i < 3; i++) { // var 사용
  functions.push(function () {
    console.log(i);
  });
}

functions[0](); // 출력: 3
functions[1](); // 출력: 3
functions[2](); // 출력: 3
```

> 함수는 함수가 정의될 때의 변수 자체만을 기억하고, 실제 변수의 값을 꺼내오지는 않는다. i가 var로 선언되었고 function 스코프에 하나만 존재한다. 모든 익명 함수는 function 스코프에 존재하는 하나의 i만을 가리킨다. 

```javascript
var functions = [];

for (let i = 0; i < 3; i++) { // let 사용
  functions.push(function () {
    console.log(i);
  });
}

functions[0](); // 출력: 0
functions[1](); // 출력: 1
functions[2](); // 출력: 2
```

> let의 경우 for문이 돌 때마다 새로운 i를 만들고 여기에 이전 i의 값을 대입합니다. 