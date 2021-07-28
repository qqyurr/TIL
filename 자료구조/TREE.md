# TREE :evergreen_tree:

트리의 개념

- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리모양의 구조

노드(node) - 트리의 원소

간선(edge) - 노드를 연결하는 선. 부모 노드와 자식 노드를 연결

루트 노드(root node) - 트리의 시작 노드

포화 이진 트리(Full Binary Tree) - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리

완전 이진 트리(Complete Binary Tree) - 노드 수가 n개일 때, 1번부터 n번까지 빈 자리가 없는 이진 트리

##### 3가지의 기본적인 순회방법

- 전위 순회

  - 부모 -> 좌 -> 우

  ```python
  def preorder_traverse(T):
      if T:
          visit(T) #print(T.item)
          preorder_traverse(T.left)
          preorder_traverse(T.right)
  ```

  

- 중위 순회

  - 좌 -> 부모 -> 우

  ```python
  def inorder_traverse(T):
      if T:
          inorder_traverse(T.left)
          visit(T) #print(T.item)
          inorder_traverse(T.right)
  ```

  

- 후위 순회

  - 좌-> 우 -> 부모

  ```python
  def postorder_traverse(T):
      if T:
          postorder_traverse(T.left)
          postorder_traverse(T.right)
          visit(T) #print(T.item)
  ```

  

##### 노드 번호의 성질

- 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : `2 * i`
- 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : `2 * i + 1`



##### 이진트리를 순회하여 정점 번호 출력

```python
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(T):
    if T:
        print(T, end=' ')
        preorder(tree[T][0])
        preorder(tree[T][1])

def inorder(T):
    if T:
        inorder(tree[T][0])
        print(T,end=' ')
        inorder(tree[T][1])

def postorder(T):
    if T:
        postorder(tree[T][0])
        postorder(tree[T][1])
        print(T, end=' ')

n = int(input())
temp = list(map(int, input().split()))
tree = [[0]*2 for _ in range(n+1)]
for i in range(0, len(temp), 2):
    parent, child = temp[i], temp[i+1]

    if not tree[parent][0]:
        tree[parent][0] = child
    # parent에 숫자 있으면 두번째 자리에 숫자 넣기
    else:
        tree[parent][1] = child
        
print(tree)
preorder(1)
print()
inorder(1)
print()
postorder(1)
```

##### 이진 탐색 트리

> 탐색 작업을 효율적으로 하기 위한 자료 구조
>
> 모든 원소는 서로 다른 유일한 키를 갖는다.
>
> key(왼쪽 서브트리) < key(루트 노드) <key(오른쪽 서브트리)
>
> `중위순회하면 오름차순으로 정렬된 값을 얻을 수 있다.`

##### 최소힙만들기

```python
# 최소힙
def heappush(value):
    global heapcount
    heapcount += 1
    heap[heapcount] = value
    cur = heapcount
    parent = cur//2

    # 루트가 아니고(parent=0이 아니고),  if 부모노드값 > 자식노드값 => swap
    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur//2

def heappop():
    global heapcount
    # 루트 저장 하고
    rootValue = heap[1]
    # 마지막 인덱스랑 바꾸기
    heap[1] = heap[heapcount]
    # 마지막 인덱스의 숫자 지우기
    heap[heapcount] = 0
    # heapcount 1 줄이기
    heapcount -= 1

    parent = 1
    child = parent * 2
    if child + 1  <= heapcount: # 오른쪽자식존재, heapcount 아래는 다 채워져 있기 때문에, 작은 지 확인하면 된다.
        # 둘중에 더 작은거 child에 저장
        if heap[child] > heap[child+1]:
            child = child + 1
    # 자식노드가 존재하고, 부모노드 > 자식노드 => swap
    while child <= heapcount and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:  # 오른쪽자식존재, heapcount 아래는 다 채워져 있기 때문에, 작은 지 확인하면 된다.
            # 둘중에 더 작은거 child에 저장
            if heap[child] > heap[child + 1]:
                child = child + 1

    return rootValue

heapcount = 0
temp = [7,2,5,3,4,6]
N = len(temp)
heap = [0]*(N+1)
for i in range(N):
    heappush(temp[i])
for i in range(N):
    print(heappop(), end=' ')
```

##### heapq 이용하여 최소힙만들기

```python
# 최소힙만 지원 (heapq)
import heapq
heap = [7,2,5,3,4,6]
print(heap)
heapq.heapify(heap)
print(heap)
heapq.heappush(heap,1)
print(heap)
# 하나씩 순서대로 pop
while heap:
    print(heapq.heappop(heap), end = ' ')
print()
##########################
temp = [7,2,5,3,4,6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, (-temp[i]))
heapq.heappush(heap2, (-1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)*-1, end = ' ')
```

