# N으로 표현

###### 문제 설명

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

##### 제한사항

- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

##### 입출력 예

| N    | number | return |
| ---- | ------ | ------ |
| 5    | 12     | 4      |
| 2    | 11     | 3      |

##### 입출력 예 설명

예제 #1
문제에 나온 예와 같습니다.

예제 #2
`11 = 22 / 2`와 같이 2를 3번만 사용하여 표현할 수 있습니다.



 풀이

```python
def solution(N, number):
    possible_set = [0,[N]] 
    if N == number:
        return 1
    for i in range(2, 9):
        case_set = set() 
        basic_num = int(str(N)*i) 
        case_set.add(basic_num)
        for i_half in range(1, i//2+1): 
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]: 
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    if y !=0:
                        case_set.add(x/y)
                    if x !=0:
                        case_set.add(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set) 
    return -1 
```

> DP 문제입니다. 다섯가지 경우의 연산이 있는데, N이 5라면
>
> ```python
> 55
> 5 + 5
> 5 * 5
> 5 - 5
> 5 / 5
> ```
>
> 이렇게 다섯가지 방법으로 연산을 할 수 있습니다.
>
> 연산 결과를 리스트에 저장하고, 저장된 숫자를 가지고 또 연산을 하면 됩니다. 