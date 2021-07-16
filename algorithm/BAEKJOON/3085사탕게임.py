import sys
sys.stdin = open('사탕.txt')

def change(N):
    max_ans = []
    # 가로 바꾸기
    for i in range(N):
        for j in range(1,N):
            BRD[i][j-1], BRD[i][j] = BRD[i][j], BRD[i][j-1]
            che = check(N)
            max_ans.append(che)
            # 원상태로 복구
            BRD[i][j], BRD[i][j-1] = BRD[i][j-1], BRD[i][j]

    # 세로 바꾸기
    for i in range(N):
        for j in range(1,N):
            BRD[j-1][i], BRD[j][i] = BRD[j][i], BRD[j-1][i]
            che2 = check(N)
            max_ans.append(che2)
            BRD[j][i], BRD[j-1][i] = BRD[j-1][i], BRD[j][i]

def check(N):
    global max_cnt
    cnt_list = []
    # garo
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if BRD[i][j] == BRD[i][j-1]:
                cnt +=1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt

    # sero
    for i in range(N):
        cnt2 = 1
        for j in range(1,N):
            if BRD[j][i] == BRD[j-1][i]:
                cnt2 += 1
            else:
                if max_cnt < cnt2:
                    max_cnt = cnt2
                cnt2 = 1
        if max_cnt < cnt2:
            max_cnt = cnt2


N = int(input())
BRD = [list(input()) for _ in range(N)]
max_cnt = 0
change(N)
print(max_cnt)