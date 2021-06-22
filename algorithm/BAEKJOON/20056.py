from collections import deque
import sys
sys.stdin = open('20056.txt')

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
q = deque()
a = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    a[r-1][c-1].append([m, s, d])
    q.append([r-1, c-1])

for _ in range(k):
    temp = []
    qlen = len(q)
    for _ in range(qlen):
        x, y = q.popleft()
        for _ in range(len(a[x][y])):
            m, s, d = a[x][y].popleft()
            nx = (s * dx[d] + x) % n
            ny = (s * dy[d] + y) % n
            q.append([nx, ny])
            # 다음 좌표가 저장된 파이어볼
            temp.append([nx, ny, m, s, d])
    # 하나씩 불러와서 지도에 저장
    for x, y, m, s, d in temp:
        a[x][y].append([m, s, d])

    for i in range(n):
        for j in range(n):
            # 좌표의 파이어볼이 겹치는 경우
            if len(a[i][j]) > 1:
                nm, ns, odd, even, flag = 0, 0, 0, 0, 0
                for idx, [m, s, d] in enumerate(a[i][j]):
                    nm += m
                    ns += s
                    if idx == 0:
                        if d % 2 == 0:
                            even = 1
                        else:
                            odd = 1
                    else:
                        # even인데 홀수가 들어올경우
                        if even == 1 and d % 2 == 1:
                            flag = 1
                        # odd 인데 짝수가 들어오는 경우
                        elif odd == 1 and d % 2 == 0:
                            flag = 1

                nm //= 5
                ns //= len(a[i][j])
                # 원래 파이어볼이 있던 자리 0으로 만들기
                a[i][j] = deque()
                # 질량이 0이 아니면 flag대로 좌표에 새로운 파이어볼 append
                if nm != 0:
                    for idx in range(4):
                        nd = 2 * idx if flag == 0 else 2 * idx + 1
                        a[i][j].append([nm, ns, nd])

ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j]:
            for m, s, d in a[i][j]:
                ans += m
print(ans)