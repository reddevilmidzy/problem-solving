import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ans = []
min_box = 256
max_box = 0

for i in range(n):
    for j in range(m):
        min_box = min(min_box, graph[i][j])
        max_box = max(max_box, graph[i][j])

for k in range(min_box, max_box+1):
    time = 0
    box = b
    to_fill = 0
    for i in range(n):
        for j in range(m):
            tmp = graph[i][j]
            if tmp > k:
                box += tmp-k
            elif tmp < k:
                to_fill += k-tmp

    if to_fill > box:
        continue
    ans.append(((box-b)*2 + to_fill, k))

ans.sort(key=lambda x: (x[0], -x[1]))
print(*ans[0])