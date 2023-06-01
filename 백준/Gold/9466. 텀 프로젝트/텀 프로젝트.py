import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur:int):
    visited[cur] = True
    nxt = nums[cur]
    if not visited[nxt]: dfs(nxt)
    elif not matched[nxt]:
        global cnt
        cnt -= 1
        while nxt != cur:
            cnt -= 1
            nxt = nums[nxt]
    matched[cur] = True

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [0] + list(map(int,input().split()))

    visited = [False]*(n+1)
    matched = [False]*(n+1)
    cnt = n

    for node in range(1, n+1):
        if not visited[node]:
            dfs(node)
    print(cnt)