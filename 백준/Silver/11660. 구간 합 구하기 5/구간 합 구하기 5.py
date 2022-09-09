import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
# coor = [list(map(int,input().split())) for _ in range(m)]

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        prefix[i][j] = graph[i-1][j-1]+prefix[i][j-1]+prefix[i-1][j]-prefix[i-1][j-1]
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    if x1==x2 and y1==y2:
        print(graph[x1-1][y1-1])
    else:
        ans = prefix[x2][y2]-prefix[x1-1][y2]-prefix[x2][y1-1]+prefix[x1-1][y1-1]
        print(ans)
