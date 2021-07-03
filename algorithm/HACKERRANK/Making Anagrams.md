# Making Anagrams

| 문제

```
anagrams이 되게 하려면 두 단어가 똑같은 글자만을 포함하고 있어야한다.
예를 들어, adb, abd 는 anagrams이다.
하지만 adc, abc 는 anagrams가 아니다.
a = 'cde'
b = 'dcf'
a,b라는 단어가 있다면 두 단어에서 어떤 글자를 제거해야 a,b가 anagrams가 될 수 있을까? 
```

| 풀이

1. string을 list로 변환해서 글자들을 쪼개서 list안에 넣는다.
2. list 두개를 반복문을 돌며 같은 글자들을 찾는다. 찾고나서는 pop()을 통해 제거한다. 
3. cnt로 같은 글자가 나올 때마다 숫자를 센다. 

```python
def makeAnagram(a, b):
    # Write your code here
    a_list = list(a)
    a_len = len(a_list)
    b_list = list(b)
    b_len = len(b_list)
    cnt = 0
    for i in range(a_len):
        for j in range(len(b_list)):
            if a_list[i] == b_list[j]:
                b_list.pop(j)
                cnt += 1
                break 
    res = 0
    res += a_len - cnt
    res += b_len - cnt
    return res
```

```javascript
function makeAnagram(a, b) {
    // Write your code here
    let split_a = [...a]
    let split_b = [...b]
    let len_a = a.length
    let len_b = b.length
    let cnt = 0
    for (let i = 0; i < len_a; i++){
        console.log(i)
        for (let j = 0; j<split_b.length; j++) {
            console.log(j)
            if(split_a[i]===split_b[j]){
                split_b.splice(j,1)
                cnt += 1
                break;
            }
        }
    }
    let res = 0
    res += len_a - cnt
    res += len_b - cnt
    return res
}
```



| 느낀점

Javascript로도 알고리즘을 잘 풀 수 있게 연습해야겠다. 