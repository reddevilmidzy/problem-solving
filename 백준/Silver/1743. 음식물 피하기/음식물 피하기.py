import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
def dfs(a,b):
    global cnt
    if 1 > a or n < a or 1 > b or m < b:
        return False
    if graph[a][b] == 1:
        cnt += 1
        graph[a][b] = 0
        dfs(a,b+1)
        dfs(a,b-1)
        dfs(a+1,b)
        dfs(a-1,b)
        ans.append(cnt)
        return True
    return False
    

n,m,k = map(int,input().rstrip().split())
graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(k):
    r,c = map(int,input().rstrip().split())
    graph[r][c] = 1

ans = []
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt = 0
        if dfs(i,j):
            pass

print(max(ans))