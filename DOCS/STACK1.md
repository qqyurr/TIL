# STACK 

2020-08-26 첫 작성

2020-08-27 수정

### 스택의 특성

- 물건을 쌓아올리듯 자료를 쌓아 올린 형태의 자료구조
- 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(LIFO, Last-In-First-Out)

### 스택의 push 알고리즘

```python
def push(item):
    s.append(item)
```

### 스택의 pop 알고리즘

```python
def pop():
    if len(s)==0:
        return False
    else:
        return s.pop(-1)
```

### 괄호검사

```python
# 왼쪽만나면 push 오른쪽만나면 pop해서 비교. 자기 짝인지
def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(': #push
            stack.append(arr[i])
        elif arr[i] == ')': #pop하고 비교해야 # 비교할필요없음 두개밖에없어서
            if len(stack) == 0: #stack이 비어있으면 False
                return False
            else:
                stack.pop()
    if stack: # 끝났는데 stack이 비어있지 않으면
        return False
    else:
        return True

stack = []
arr = "()()((())))"
print(check(arr))
```

### 재귀

#### 피보나치 기본 재귀

```python
def fibo(n):
	if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

> 엄청난 중복 호출 존재

#### Memoization

> 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 한다. 동적 계획법의 핵심

```python
# fibo(n)의 값을 계산하자마자 저장(memoize)하면 실행시간을 O(n)으로 줄일 수 있다.
# memo를 위한 배열 할당, 모두 0으로 초기화
# memo[0]을 0으로 memo[1]는 1로 초기화 한다

def fibo1(n):
    global memo
    # 배열 memo의 리스트 크기가 n과 같아질때까지
    if n >= 2 and len(memo) <= n:
        # n-1과 n-2의 값을 합친 것이 memo의 새로운 숫자로 들어간다.
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0,1]
    
```

#### DP(Dynamic Programming)

> 동적계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘
>
> 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.

1. 문제를 부분문제로 분할
2. 부분 문제로 나누는 일을 끝냈응면 가장 작은 부분 문제부터 해를 구한다.
3. 그 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.

```python
def fibo2(n):
    f = [0,1]
    
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        
    return f[n]
```

#### DFS(깊이우선탐색)

> 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요
>
> 깊이우선탐색(DFS) 너비우선탐색(BFS)
>
> 1. 시작 정점 v를 결정하여 방문한다.
>
> 2. 정점v가 인접한 정점 중에서
>
>    1) 방문하지 않은 정점 w가 있응면, 정점 v를 스택에 push하고 정점w를 방문한다. 그리고 w를 v로하여 다시 2.를 반복한다.
>
>    2) 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.를 반복
>
> 3. 스택이 공백이 될 때까지 2. 반복

```python
# 연습문제3
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    #방문체크
    visited[v] = 1
    print(v, end=" ")
    # v의 인접한 정점중에서 방문 안 한 정점을 재귀 호출
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 정점, 간선
N, E = map(int, input().split())
# 간선들 .....
temp = list(map(int, input().split()))
# 인접행렬
G = [[0]*(N+1) for _ in range(N+1)]
# 방문체크
visited = [0]*(N+1)
# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    # 양방향 간선 표시
    # 단방향으로 표시하려면 둘 중 하나만 하면 된다.
    G[s][e] = 1
    G[e][s] = 1
    
print(dfs(1)) #시작 정점이 1인 깊이우선탐색경로
```

