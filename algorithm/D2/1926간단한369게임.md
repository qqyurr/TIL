# SWEA 간단한 369 게임

```python
k = int(input())
 
for i in range(1, k+1):
    total = 0
    for x in str(i):
        # string 형태로 바꾼 i 중에 3, 6, 9가 포함되어 있으면 1씩 total에 추가
        if x in ['3','6','9']:
            total += 1
    # total이 0이면 숫자 그대로 출력
    if total == 0:
        print(i, end = ' ')
    # total이 0이 아니라면 '-'가 total의 수만큼 출력
    else:
        print( '-'*total, end = ' ')
```

