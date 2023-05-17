import sys
input = sys.stdin.readline

def find(parent: list[int], x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: list[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,input().split())
truth = list(map(int,input().split()))[1:]

parent = [i for i in range(n+1)]

for x in truth:
    parent[x] = 0

parties = [list(map(int,input().split())) for _ in range(m)]
for party in parties:
    for i in range(1,party[0]):
        if find(parent, party[i]) != find(parent, party[i+1]):
            union(parent, party[i], party[i+1])

ans = m

for party in parties:
    for x in party[1:]:
        if find(parent, x) == 0:
            ans -= 1
            break
print(ans)