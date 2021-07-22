# 입국심사

###### 문제 설명

n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.

처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
- 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
- 심사관은 1명 이상 100,000명 이하입니다.

##### 입출력 예

| n    | times   | return |
| ---- | ------- | ------ |
| 6    | [7, 10] | 28     |

##### 입출력 예 설명

가장 첫 두 사람은 바로 심사를 받으러 갑니다.

7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.

10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.

14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.

20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.



##### 처음 시도한 코드

```python
def solution(n, times):
    short = min(times)
    copy = times[:]
    BRD = [0 for _ in range(len(times))]
    while n > 0:
        for idx in range(len(times)):
            min_time = min(copy)
            min_idx = copy.index(min_time)
            if copy[min_idx] + times[min_idx] < copy[idx] + times[idx]:
                copy[idx] += times[min_idx]
                n -= 1
                BRD[min_idx] += times[min_idx]
            else:
                copy[idx] += times[idx]
                n -= 1
                BRD[idx] += times[idx]
            print('idx', idx, 'BRD', BRD)
            if n == 0:
                break
    print(max(BRD))
    answer = max(BRD)
    return answer
```

> 이 코드는 주어진 테스트케이스(1개)는 통과했지만 다른 테스트케이스들은 통과하지 못하였다. 이런 식으로 푸는 게 아니고 완전탐색, 혹은 이분탐색으로 풀어야하는 문제였다. 완전탐색은 메모리가 너무 커서 통과하지 못하기 때문에 이분탐색으로 풀어야한다. 

##### python

```python
def solution(n, times):
    min_num = 1
    max_num = max(times)*n
    answer = max_num
    # 이분탐색
    while min_num <= max_num:
        mid = (min_num + max_num)//2
        cnt = 0
        for t in times:
            cnt += mid//t
        if n > cnt:
            min_num = mid + 1
        else:
            if mid <= answer:
                answer = mid
            max_num = mid - 1
    return answer
```

##### javascript

```javascript
function solution(n, times) {
    var min_num = 1;
    var max_num = Math.max.apply(null,times) * n
    var answer = max_num;
    while (min_num <= max_num) {//min_num이 max_num보다 커졌을때 stop
        // mid : 소요시간의 중간값 
        var mid = parseInt((min_num + max_num)/2)
        var cnt = 0
        // cnt : 중간값일 때 심사할 수 있는 사람 수
        for (var i = 0; i<times.length; i++){
            cnt += parseInt(mid/times[i])
        }
        if (n > cnt) { // mid 늘리기
            min_num = mid + 1
        } else { // mid 줄이기
            if (mid <= answer){// 둘 중 최솟값을 answer에 저장
                answer = mid
            }
            max_num = mid - 1
        }
    }
    return answer;
}
```

> 이진탐색의 시간 복잡도는 O(logN)  이 문제의 복잡도는 log10억 
> `심사관 당 맡는 입국자 수 = 시간(answer) / 심사관 당 심사시간`
