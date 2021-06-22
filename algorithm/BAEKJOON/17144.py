import sys
from copy import deepcopy
sys.stdin = open('17144.txt')

def spread():
    temp = [[0] * C for _ in range(R)]
    temp[cleaner[0][0]][cleaner[0][1]] = -1
    temp[cleaner[1][0]][cleaner[1][1]] = -1
    for i in range(R):
        for j in range(C):
            # 미세먼지가 있는 칸
            if s[i][j] > 0:
                cnt = 0
                # 4 방향 확인
                for dir in range(4):
                    x = i + dx[dir]
                    y = j + dy[dir]
                    # 벽이 아니고, 인접한 방향에 공기청정기가 없다면
                    if 0 <= x < R and 0 <= y < C and s[x][y] != -1:
                        temp[x][y] += s[i][j] // 5
                        cnt += 1
                temp[i][j] += s[i][j] - (s[i][j] // 5) * cnt
    return temp


def clean(x,y,dir):
    cleaning = deepcopy(s)
    # 클리너 위치 저장
    cx, cy = x, y-1
    s[x][y] = 0
    for d in range(4):
        while True:
            nx = x + dx[dir[d]]
            ny = y + dy[dir[d]]
            # 클리너 좌표로 돌아오면 return
            if nx == cx and ny == cy:
                return
            if 0 <= nx < R and 0 <= ny < C:
                s[nx][ny] = cleaning[x][y]
            else:
                break
            x,y = nx, ny


# T초후에 방에 남아있는 미세먼지 양 출력
R, C, T = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(R)]

# 공기청정기 위치 확인
cleaner = []
for i in range(R):
    for j in range(C):
        if s[i][j] == -1:
            cleaner.append((i,j))
c1 = cleaner[0]
c2 = cleaner[1]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(T):
    # 미세먼지 확산
    # 1. 미세먼지가 있는 칸 확인
    # 2. 벽이 없는 방향으로 미세먼지 확산
    s = spread()
    # 공기청정기 작동
    clean(c1[0], c1[1]+1, [3,1,2,0])
    clean(c2[0], c2[1]+1, [3,0,2,1])
    # 벽을 만나면 방향 바꾸기 필요
    # 위쪽 동 -> 북 -> 서 -> 남, 아래쪽 동 -> 남 -> 서 -> 북
    # 위 [3,1,2,0] 아래 [3,0,2,1]
s[c1[0]][c1[1]] = 0
s[c2[0]][c2[1]] = 0

dust = 0
for i in range(R):
    dust += sum(s[i])
print(dust)