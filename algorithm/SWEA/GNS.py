import sys
sys.stdin = open("GNS_test_input.txt", "r")

t = int(input())

for tc in range(t):
    a, b = input().split()
    b = int(b)
    num_list = list(input().split())
    numnum = []
    newnum = []
    txt = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    for num in num_list:
        for i in range(len(txt)):
            if num == txt[i]:
                numnum.append(i)
    numnum.sort()
    for i in numnum:
        newnum.append(txt[i])
    new = " ".join(newnum)
    print(f'#{tc+1}')
    print(new)
