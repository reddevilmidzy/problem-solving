h,n = map(int, input().split())
a = abs(h-n)

graph = [[0 for i in range(a+1)] for j in range(a+1)]
graph[0] = [1 for i in range(a+1)]

for i in range(a+1):
    for j in range(i, a+1):
        graph[i][j] = graph[i-1][j] +graph[i][j-1]

print(graph[-1][-1]) if h != n else print(1)