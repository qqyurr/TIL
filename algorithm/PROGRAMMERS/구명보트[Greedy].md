# 구명보트

###### 문제 설명

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 **2명**씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
- 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

##### 입출력 예

| people           | limit | return |
| ---------------- | ----- | ------ |
| [70, 50, 80, 50] | 100   | 3      |
| [70, 80, 50]     | 100   | 3      |

> 문제풀이

효율성있게 문제를 푸려면 pop()이나 이런 리스트 자체를 변경하는 함수를 최대한 지양해야합니다.

```python
def solution(people, limit):
    answer = 0
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            if people[i]+people[j]<=limit:
                people.pop(i)
                people.pop(j-1)
                answer += 1
    answer = answer + len(people)

    return answer
```

> 처음 풀었던 방식 코드는 5분만에 짰는데 당연히 시간초과가 났다. pop을 두번이나 하고 반복문도 전체를 돌아버리니 메모리를 많이 잡아먹은 것 같습니다. 

```python
def solution(people, limit):
    answer = 0
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            if people[i]+people[j]<=limit:
                people[i] = 241
                people[j] = 241
                answer += 1
    for peo in people:
        if peo < 241:
            answer += 1
 
    return answer
```

> 이건 pop은 안되겠다 싶어서 인덱스 숫자를 바꿔버리는 것으로 했는데 이것도 반복문을 전체를 다 돌아야하기 때문에 시간이 많이 걸리는 것 같습니다.

정답

```python
def solution(people, limit):
    answer = 0
    people.sort()
    small = 0
    big = len(people) - 1
    while small <= big:
        answer += 1
        if people[small] + people[big] <= limit:
            small += 1
        big -= 1
            

    return answer
```

> 일단 sort를 통해서 가장 작은 수 가장 큰 수를 더해서 100이 넘는지 안넘는지 확인하는 방식으로 하는게 반복문도 덜 도는 방식이고, pop() 이나 리스트를 변경하는 방식이 아니기 때문에 시간이 덜 드는 좋은 방식입니다.