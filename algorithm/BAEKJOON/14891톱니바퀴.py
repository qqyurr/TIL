import sys
sys.stdin = open('14891.txt')

# 왼쪽 확인
def left(num, dd):
    if num == 1:
        return
    if BRD[num][6] == BRD[num-1][2]:
        return
    else:
        if dd == 1:
            return (num-1, -1)
        elif dd == -1:
            return (num-1, 1)
# 오른쪽 확인
def right(num, dd):
    if num == 4:
        return
    if BRD[num][2] == BRD[num+1][6]:
        return
    else:
        if dd == 1:
            return (num+1, -1)
        elif dd == -1:
            return (num+1, 1)

# 회전
def turn(num, dirc):
    # 시계방향
    if dirc == 1:
        BRD[num] = BRD[num][-1] + BRD[num][:7]
    # 반시계방향
    else:
        BRD[num] = BRD[num][1:] + BRD[num][0]

BRD = [' ']
for _ in range(4):
    BRD.append(input())

k = int(input())
for _ in range(k):
    num, dirc = map(int, input().split(' '))
    result = [(num, dirc)]
    d = dirc
    for i in range(num, 0, -1):
        tmp = left(i, d)
        if not tmp:
            break
        result.append(tmp)
        d = tmp[1]
    d = dirc
    for i in range(num, 4):
        tmp = right(i, d)
        if not tmp:
            break
        result.append(tmp)
        d = tmp[1]

    for num, dirc in result:
        turn(num, dirc)

score = int(BRD[1][0])*1 + int(BRD[2][0])*2 + int(BRD[3][0])*4 + int(BRD[4][0])*8
print(score)
# 돌리고 나서 양 옆 바퀴 확인 [2] 와 [6] -> 숫자가 같으면 가만히 있고 숫자가 다르면 반대방향으로 회전 -> 또 확인

