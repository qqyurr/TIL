# STACK2 + QUEUE

### 재귀 호출을 이용한 부분집합 생성 알고리즘

```
A[]
def powerset(n,k):
if n == k:
	PRINT
else:
    A[k] = 1
    powerset(n, k+1)
    A[k] = 0
    powerset(n, k+1)
```

```
def powerset(n,k,cursum):
	global total
	if cursum > 10:
		return
	total += 1
    if n == k:
        PRINT(n, cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum + arr[k])
        A[k] = 0
        powerset(n, k+1, cursum)
```

#### 순열 생성함수 {1,2,3}

```
for i1 in range(1,4):
	for i2 in range(1,4):
		# 앞에 나왔던 게 또 나오면 안돼요!
        if i2 != i1:
            for i3 in range(1,4):
            if i3!=i1 and i3 != i2:
                print(i1, i2, i3)

-> 123 132 213 231 312 321 
```

#### 재귀호출을 통한 순열 생성 (APS 응용)

```
// arr[] : 데이터저장된배열
// swap(i,j) : arr[i] <--교환--> arr[j]
// n : 원소의 개수, k: 현재까지 교환된 원소의 개수
perm(n,k)
	if k ==n
		print arrary
	else:
		for i in k -> n-1
			swap(k,i)
			perm(n, k+1)
			swap(k,i)
```



