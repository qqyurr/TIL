import sys
sys.stdin = open('solvingclub.txt','r')

for tc in range(10):
    t = int(input())
    # 가로 리스트 만들기
    garo_lst = []
    for i in range(100):
        garo_lst.append(input())
    # 세로 리스트 만들기
    sero_lst = []
    for i in range(100):
        temp = []
        for j in range(100):
            temp += garo_lst[j][i]
        sero_lst += ["".join(temp)]

    max_len = 0
    for garo in garo_lst:
        for i in range(100):
            for b in range(100-i+1):
                # b의 범위만큼 garo의 값 비교, 범위는 1씩 옆으로 옮긴다.
                if garo[i:b + i] == garo[i:b + i][::-1]:
                    if b > max_len:
                        max_len = b

    for sero in sero_lst:
        for i in range(100):
            for b in range(100-i+1):
                # b의 범위만큼 sero의 값 비교, 범위는 1씩 옆으로 옮긴다.
                if sero[i:b + i] == sero[i:b + i][::-1]:
                    if b > max_len:
                        max_len = b

    print(f'#{t} {max_len}')
