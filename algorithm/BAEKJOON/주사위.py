import sys
sys.stdin = open('주사위.txt')

# 주사위 굴리기
def rolling(direc, dice):
    # 동쪽
    if direc == 1:
        return [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    # 서쪽
    elif direc == 2:
        return [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    # 북쪽
    elif direc == 3:
        return [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    # 남쪽
    elif direc == 4:
        return [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]

N, M, y, x, K = map(int,input().split())
BRD = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
dice = [0,0,0,0,0,0,0]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
for dc in direction:
    # 벽 확인
    if 0<= y + dy[dc-1] < N or 0<= x + dx[dc-1] < M:
        dice = rolling(dc, dice)
        x = x + dx[dc - 1]
        y = y + dy[dc - 1]
        if BRD[y][x] == 0:
            BRD[y][x] = dice[6]
        else:
            dice[6] = BRD[y][x]
            BRD[y][x] = 0

        print(dice[1])
