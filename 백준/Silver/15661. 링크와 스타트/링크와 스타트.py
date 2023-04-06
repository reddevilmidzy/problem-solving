# 일단 백트래킹으로 풀어보자
# 추후에 비트마스킹도 도전
from itertools import combinations
import sys, math
input = sys.stdin.readline

def make_candi(n):
    div = math.factorial(n) // (math.factorial(n//2)**2)//2
    res = []
    cnt = 0
    # n이 짝수일때만 중간거 제거
    for i in range(1, n//2+1):
        for j in combinations(range(n), i):
            res.append(set(j))
            if i == n//2:
                cnt += 1
                if cnt == div:
                    return res
    # 여기는 n이 홀수 일때 옴
    return res

def diff(start_team: set):
    res = 0
    link_team = list(player - start_team)
    start_team = list(start_team)
    u = len(start_team)
    v = n - u

    for i in range(u-1):
        for j in range(i+1, u):
            res += ability[start_team[i]][start_team[j]]
            res += ability[start_team[j]][start_team[i]]

    for i in range(v-1):
        for j in range(i+1, v):
            res -= ability[link_team[i]][link_team[j]]
            res -= ability[link_team[j]][link_team[i]]
    return abs(res)

# n = 7
n = int(input())
ability = [list(map(int,input().split())) for _ in range(n)]
player = set(i for i in range(n))
ans = int(1e9)
for candi in make_candi(n):
    ans = min(ans, diff(candi))
print(ans)