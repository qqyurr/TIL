# 가장 먼 노드

###### 문제 설명

n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 노드의 개수 n은 2 이상 20,000 이하입니다.
- 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
- vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

##### 입출력 예

| n    | vertex                                                   | return |
| ---- | -------------------------------------------------------- | ------ |
| 6    | [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] | 3      |

> 풀이

```python
from collections import deque
def solution(n, edge):
    answer = 0
    BRD = [[] for i in range(n+1)]
    for i in range(len(edge)):
        BRD[edge[i][0]].append(edge[i][1])
        BRD[edge[i][1]].append(edge[i][0])
    visited = [0]*(n+1)
    queue = deque()
    queue.append(1)
    visited[1] = 1
    while queue:
        idx = queue.popleft()
        for i in BRD[idx]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[idx] + 1
    max_num = max(visited)
    for v in visited:
        if v == max_num:
            answer += 1
    return answer
```

오랜만에 푼 BFS 문제. 처음에 풀 때는 BRD를 2차원 배열로 행과 열에 맞춰서 연결된 간선을 표시해서 답을 구했더니 테스트케이스 2개에서 시간초과가 나왔다. BRD에 해당번호와 간선으로 연결된 숫자만 체크하여 넣어서 값을 구했더니 정답이었습니다. 

> javascript

```javascript
function solution(n, edge) {
    var answer = 0;
    const BRD = Array.from(Array(n+1), ()=> new Array())
    let num = edge.length
    for (var i=0; i<num; i++){
        BRD[edge[i][0]].push(edge[i][1])
        BRD[edge[i][1]].push(edge[i][0])
    }
    console.log(BRD)
    const visited = Array.from({length: n+1}, () => 0)
    const queue = []
    queue.push(1)
    console.log(queue)
    visited[1] = 1
    while (queue.length) {
        const idx = queue.shift()
        for (var id of BRD[idx]){
            if(visited[id]===0){
                queue.push(id)
                visited[id] = visited[idx] + 1
            }
        }
    }
    const max_num = Math.max(...visited)
    for (var v of visited) {
        if (v===max_num){
            answer += 1
        }
    }
    
    return answer;
}
```

> 파이썬으로 풀고 자바스크립트로도 한번 다시 푸는걸 해보고 있는데 너무 헷갈린다. 자바스크립트에서 pop() 은 배열의 맨 끝 값을 제거하는 것이고 shift()가 맨 앞의 값을 제거하는 것이다. 

### JS에서 빈 2차원 배열, 1차원 배열 특정 길이로 만드는 방법 Array.from()

#### 2차원 배열(길이가 n+1)

```javascript
const BRD = Array.from(Array(n+1), ()=> new Array())
```

#### 0으로 된 1차원 배열(길이가 n+1)

```javascript
const visited = Array.from({length: n+1}, () => 0)
```



