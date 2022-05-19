import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split()) # n은 카드 개수, m은 만들어야 하는 합
arr = list(map(int, input().split())) #  카드번호가 들어있는 배열
combi = list(combinations(arr, 3)) # 조합시킴
combi_sum = [sum(i) for i in combi] # 답 후보들
a = m
for i in combi_sum:
    if m == i:
        a = m
        # print(m)
        break
    elif i > m:
        continue
    elif a > m - i:
        a = m - i
print(a) if a == m else print(m-a)