from itertools import combinations
import sys
sys.stdin = open('14889.txt')

N = int(input())
BRD = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
team = []
# n명을 2팀으로 나눈다 -> 조합 필요
for i in list(combinations(members, N//2)):
    team.append(i)
# print(team)
min_num = 10000000
for i in range(len(team)//2):
    start = team[i]
    # print(start)
    add_start = 0
    for j in range(N//2):
        one = start[j]
        for m in start:
            add_start += BRD[one][m]
    # print(add_start)
    link = team[-1-i]
    add_link = 0
    for j in range(N//2):
        one = link[j]
        for m in link:
            add_link += BRD[one][m]
    # print(add_link)
    if min_num > (abs(add_start - add_link)):
        min_num = abs(add_start-add_link)
print(min_num)

