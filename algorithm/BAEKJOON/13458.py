import sys
sys.stdin = open('13458.txt')

# 총감독관이 감시하는데 부족하면 부감독관이 들어간다.

N = int(input())
people = list(map(int, input().split()))
B, C = map(int,input().split())
count = 0
for i in range(N):
    # 시험장의 응시자수가 총감독관이 감시할 수 있는 수보다 작을 때
    if people[i] <= B:
        count +=1
    # 부감독관이 필요할때
    elif people[i] - B > 0:
        count += 1
        new = people[i] - B
        res = new // C
        count += res
        if new % C > 0:
            count +=1
print(count)

