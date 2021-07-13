
t = int(input())
for tc in range(1,t+1):
    a, b = map(int, input().split())
    # 가로 리스트 만들기
    garo_lst = []
    for i in range(a):
        garo_lst.append(input())
    # 세로 리스트 만들기
    sero_lst = []
    for i in range(a):
        temp = []
        for j in range(a):
            temp += garo_lst[j][i]
        sero_lst += ["".join(temp)]

    result = []
    # 가로에서 대칭 있으면 result에 저장
    for garo in garo_lst:
        for i in range(len(garo) - b + 1):
            # b의 범위만큼 garo의 값 비교, 범위는 1씩 옆으로 옮긴다.
            if garo[i:b + i] == garo[i:b + i][::-1]:
                result.append(garo[i:i + b])
    # 세로에서 대칭 있으면 result에 저장
    for sero in sero_lst:
        for i in range(len(sero) - b + 1):
            # b의 범위만큼 sero의 값 비교, 범위는 1씩 아래로 옮긴다.
            if sero[i:b + i] == sero[i:b + i][::-1]:
                result.append(sero[i:i + b])

    print(f'#{tc} {result[0]}')







