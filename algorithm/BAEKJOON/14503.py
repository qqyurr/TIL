import sys
sys.stdin = open('14503.txt')

def change(d):
    if (d==0):
        return 3
    elif(d==1):
        return 0
    elif(d==2):
        return 1
    elif(d==3):
        return 2

def clean(x,y,d):
    count = 1
    BRD[x][y] = 2
    while(True):
        dc = d
        for i in range(4):
            cleaned = 0
            dc = change(dc)
            newx = x + dx[dc]
            newy = y + dy[dc]
            if (BRD[newx][newy] == 0 and 0<=newx<N and 0<=newy<M):
                count += 1
                x = newx
                y = newy
                BRD[newx][newy] = 2
                d = dc
                cleaned = 1
                break
        if(cleaned==0):
            if(d==0):
                x += 1
            elif(d==1):
                y -= 1
            elif(d==2):
                x -= 1
            elif(d==3):
                y +=1
            if(BRD[x][y]==1):
                break
    return count


N, M = map(int,input().split())
# 0 북, 1 동, 2 남, 3 서
r, c, d = map(int,input().split())
BRD = [list(map(int,input().split())) for _ in range(N)]
# 북동남서
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
x = r
y = c
# start의 동서남북 확인
print(clean(x,y,d))