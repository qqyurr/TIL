# Sherlock and the Valid String

Sherlock considers a string to be *valid* if all characters of the string appear the same number of times. It is also *valid* if he can remove just `1` character at `1` index in the string, and the remaining characters will occur the same number of times. Given a string `s` , determine if it is *valid*. If so, return `YES`, otherwise return `NO`.

-> 단어의 글자 비율이 같으면 YES, 틀리면 NO (abc->{a:1, b:1, c:1})

-> 단, 알파벳 중 하나를 제거할 수 있다. 그 이후에라도 비율이 같으면 YES

(abcc -> c제거 -> {a:1, b:1, c:1})

| 풀이

1. 문자와 문자별 갯수를 오브젝트로 만든다.

   -> {a:2, b:1, c:1}

2. 오브젝트의 value값을 set()으로 중복제거한다.

   -> 중복제거 이후 길이가 1 = `anagram`

   -> 길이가 2인 경우

   ​       - 1이 1개면 = `anagram`

   ​	     - 두 숫자의 차이가 1이고 큰 숫자가 1개면 `anagram`

   -> else  `anagram` 이 아닙니다.
