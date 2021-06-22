import sys
from itertools import combinations
sys.stdin = open('15686.txt')
# N은 가로세로길이, M은 골라야할 치킨집 수
N, M = map(int,input().split())
BRD = [list(map(int,input().split())) for _ in range(N)]
distance = 0
# 치킨집 리스트 저장하기
chicken_list = []
for i in range(N):
    for j in range(N):
        if BRD[i][j] == 2:
            chicken_list.append((i,j))
#집 리스트 저장하기
house_list = []
for i in range(N):
    for j in range(N):
        if BRD[i][j] == 1:
            house_list.append((i,j))
min_value = 10000000000
for chicken_comb in combinations(chicken_list, M):
    chicken_distance = 0
    for house in house_list:
        temp = []
        for chicken in chicken_comb:
            temp.append(abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        chicken_distance += min(temp)
    if chicken_distance < min_value:
        min_value = chicken_distance
print(min_value)
