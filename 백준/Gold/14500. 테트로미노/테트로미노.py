import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

res = []

for i in range(n):
    for j in range(m):
        
        #  세개 쭉 그은 다음, 찾기
        if i+2<n:
            now = 0
            for k in range(3):
                now += graph[i+k][j]

            if i+3<n:
                res.append(now+graph[i+3][j])
            if j+1<m:
                res.append(now+graph[i][j+1])
                res.append(now+graph[i+1][j+1])
                res.append(now+graph[i+2][j+1])
            if j>0:
                res.append(now+graph[i][j-1])
                res.append(now+graph[i+1][j-1])
                res.append(now+graph[i+2][j-1])

        if j+2<m:
            now = 0
            for k in range(3):
                now += graph[i][j+k]
            
            if j+3<m:
                res.append(now+graph[i][j+3])
            if i+1<n:
                res.append(now+graph[i+1][j])
                res.append(now+graph[i+1][j+1])
                res.append(now+graph[i+1][j+2])
            if i>0:
                res.append(now+graph[i-1][j])
                res.append(now+graph[i-1][j+1])
                res.append(now+graph[i-1][j+2])

        # 네모
        if i+1<n and j+1<m:
            now = graph[i][j]+graph[i+1][j]+graph[i][j+1]+graph[i+1][j+1]
            res.append(now)
        
        if i+1<n and 0<j<m-1:
            now = graph[i][j]+graph[i+1][j]
            res.append(now+graph[i][j+1]+graph[i+1][j-1])
            res.append(now+graph[i][j-1]+graph[i+1][j+1])
        if 0<i<n-1 and j+1<m:
            now = graph[i][j]+graph[i][j+1]
            res.append(now+graph[i+1][j]+graph[i-1][j+1])
            res.append(now+graph[i-1][j]+graph[i+1][j+1])
                
print(max(res))