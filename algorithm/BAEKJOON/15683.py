import sys
sys.stdin = open('15683.txt')


delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
direction = {1: [[0], [1], [2], [3]], 2: [[0, 1], [2, 3]], 3: [[0, 2], [1, 3], [0, 3], [1, 2]],
             4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 5: [[0, 1, 2, 3]]}

def dfs(n, arr):
    global space
    if n == len(cam):
        # 방문표시
        visited = [[False for _ in range(M)] for _ in range(N)]
        for idx, c in enumerate(cam):
            x = c[0]
            y = c[1]
            for element in arr[idx]:
                c = 1
                while True:
                    nx = x + delta[element][0]*c
                    ny = y + delta[element][1]*c
                    if 0<=nx<N and 0<=ny<M and BRD[nx][ny] !=6:
                        if BRD[nx][ny]==0 and visited[nx][ny] == False:
                            visited[nx][ny] = True
                        c += 1
                    else:
                        break
        cnt = 0
        for ii in range(N):
            for jj in range(M):
                if BRD[ii][jj] == 0 and visited[ii][jj] == False:
                    cnt +=1
        if space > cnt:
            space = cnt
        return

    for dire in direction[BRD[cam[n][0]][cam[n][1]]]:
        arr.append(dire)
        dfs(n+1,arr)
        arr.pop()



N, M = map(int,input().split())
BRD = [list(map(int,input().split())) for _ in range(N)]
space = 0
#cctv가 있는 위치 cam에 저장
cam = []
for i in range(N):
    for j in range(M):
        if 1<= BRD[i][j] <=5:
            cam.append((i,j))
        if BRD[i][j] == 0:
            space += 1
print(cam)
dfs(0,[])
print(space)
