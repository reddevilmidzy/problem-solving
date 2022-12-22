import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i,j])
        elif graph[i][j] == 2:
            chicken.append([i,j])

candi = []

def bt(s):
    if len(s) == m:
        tmp = []
        for i in s:
            tmp.append(chicken[i])
        candi.append(tmp)
        return
    for i in range(len(chicken)):
        if not s:
            s.append(i)
            bt(s)
            s.pop()
        else:
            if i > s[-1]:
                s.append(i)
                bt(s)
                s.pop()
bt([])
ans = INF
for tmp in candi:
    distance = [INF] * (len(house))
    for k in tmp:
        r,c = k[0], k[1]
        for idx,i in enumerate(house):
            x,y = i[0],i[1]
            distance[idx] = min(distance[idx], abs(x-r) + abs(y-c))
    ans = min(ans, sum(distance))
            
print(ans)