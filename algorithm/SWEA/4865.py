
t = int(input())
for tc in range(1,t+1):

    a = input()
    b = input()
    max_num = 0
    for i in a:
        cnt = 0
        for j in b:
            if i == j:
                cnt += 1
        if cnt > max_num:
            max_num = cnt

    print(max_num)

