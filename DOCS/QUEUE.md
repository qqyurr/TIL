# QUEUE

리스트를 이용한 우선순위 큐의 구현

1. 리스트를 이용하여 자료 저장
2. 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
3. 가장 앞에 최고 우선순위의 원소가 위치하게 됨

: 삽입이나 삭제 연산일어날때 원소의 재배치 발생

: PriorityQueue

버퍼 

DFS -> Stack

#### BFS 너비 우선 탐색 -> 큐

: 시작점의 인접한 정점들을 모두 차례로 방문한 후 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

: 인접한 정점들을 탐색한 후, 차례로 너비 우선 탐색을 진행해야 하므로, 선입선출 형태의 자료구조인 큐 활용

```python
def BFS(G,v): # 그래프 G, 탐색시작점 v
	visited = [0]*n #n:정점의개수
	queue = [] # 큐 생성
	queue.append(v) # 시작점 v를 큐에 삽입
	while queue: # 큐가 비어있지 않은 경우
		t = queue.pop(0) # 큐의 첫번째 원소 반환
		if not visited[t]: # 방문되지 않은 곳이라면
			visited[t] = True # 방문한 것으로 표시
			visit(t)
		for i in G[t]: # t와 연결된 모든 선에 대해
			if not visited[i]: # 방문되지 않은 곳이라면
				queue.append(i) # 큐에 넣기
```

```python
def BFS(G,s): # 그래프 G 탐색 시작점 s
    visited = [0]*n # n: 정점의 개수
    D = [0]*n
    P = [0]*n
    Q = [] # 큐 생성
    visited[s] = True # 시작점 방문
    Q.append(s) # 시작점 s를 큐에 삽입
    while Q : # 큐가 비어있지 않은 경우
        v = Q.pop(0) # 큐의 첫 번째 원소 반환
        for w in G[v]: # v와 연결된 모든 선에 대해
            if not visited[w]: # 방문되지 않은 곳이라면
                visited[w] = True
                D[w] = D[v] +1
                P[w] = v
                Q.append(w) # 큐에 넣기
```



