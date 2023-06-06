from itertools import permutations
import sys
input = sys.stdin.readline

c = int(input())
n = 11

def bt(s:list[int], visited:list[bool], idx:int) -> None:
    if len(s) == n:
        tmp = 0
        global ans
        for i in range(n):
            tmp += exp[s[i]][i]
        ans.append(tmp)
        return

    for i in range(n):
        if not visited[i] and exp[i][idx]:
            visited[i] = True
            s.append(i)
            bt(s, visited, idx+1)
            s.pop()
            visited[i] = False

for _ in range(c):
    ans = []
    exp = [list(map(int,input().split())) for _ in range(n)]
    bt([], [False]*n, 0)
    print(max(ans))