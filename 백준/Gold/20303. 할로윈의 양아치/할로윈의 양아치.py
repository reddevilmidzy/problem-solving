import sys
input = sys.stdin.readline

def find(parent:list[int], x:int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent:list[int], a:int, b:int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m,k = map(int,input().split())
nums = [0]+list(map(int,input().split()))
graph = [list(map(int,input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]

for a,b in graph:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

for i in range(1, n+1):
    parent[i] = find(parent, i)

cnt = dict()

for i in range(1, n+1):
    if parent[i] not in cnt:
        cnt[parent[i]] = []
    cnt[parent[i]].append(i)

cost = []

for key in cnt.keys():
    tmp = 0
    for val in cnt[key]:
        tmp += nums[val]
    cost.append((len(cnt[key]), tmp))

dp = [[0]*(k) for _ in range(len(cost))]

for i in range(len(cost)):
    for j in range(k):
        if j - cost[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i][0]]+cost[i][1])
        else:
            dp[i][j] = dp[i-1][j]

# print(cost)
# print(dp)

# k 번째는 울기 때문에
print(dp[len(cost)-1][k-1])
