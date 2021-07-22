# 타겟넘버

###### 문제 설명

n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

```
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

```python
def cal(base, idx):
    nidx = idx+1
    if nidx >= len(num):
        res.append(base)
        return  
    cal(base+num[nidx], nidx)
    cal(base+(num[nidx]*-1), nidx)
    
def solution(numbers, target):
    global num, res
    answer = 0
    res = []
    idx = 0
    num = numbers
    base = numbers[0]
    cal(base*-1, idx)
    cal(base, idx)
    for r in res:
        if r == target:
            answer += 1
    return answer
```

> solution 함수가 main이 아니기 때문에 전역변수로 쓸 것들은 따로 global 표시를 해줘야 합니다. 
>
> 주어지는 숫자의 개수가 2이상 20개 이하 -> 이 같은 방식으로 풀면 최대  2^20의 메모리가 필요하다. 백만정도? 다행히 테케는 다 통과했습니다.   

#### Javascript

```javascript
function solution(numbers, target) {
    var answer = 0;
    var idx = 0
    var base = numbers[0]
    var num = numbers
    var res = []
    cal(base*-1, idx)
    cal(base, idx)
    
    function cal(base, idx) {
        var nidx = idx + 1
        if (nidx >= num.length) {
            res.push(base)
            return
        }
        cal(base+num[nidx], nidx)
        cal(base+(num[nidx]*-1), nidx)
    }
    for (var r of res) {
        if (r === target) {
            answer += 1
        }
    }
    return answer;
}
```

> python에서 하던 것 처럼 num과 res를 전역변수로 만들어서 다른 함수에서도 사용하려고 했지만 많은방법을 써봐도 전역변수로 만들어지지가 않았다. 서치 결과 function안에 function을써서 해결하신 분이 있어서 함수안에 넣어봤더니 제대로 실행이 됐다. 