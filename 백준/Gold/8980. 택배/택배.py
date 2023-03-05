import sys
input = sys.stdin.readline

n,c = map(int,input().split())
m = int(input())
works = [[] for _ in range(n+1)]
for _ in range(m):
    st, ed, box = map(int,input().split())
    works[st].append([ed, box])

weight = 0
down = [0]*(n+1)
ans = 0
for i in range(1, n+1):
    works[i].sort()
    weight -= down[i]
    for ed, box in works[i]:
        if weight + box <= c:
            weight += box
            down[ed] += box # 나중에 여기 왔을 때 이 무게 뺄거임
            ans += box
        else:
            ans += c - weight
            weight += c - weight
            down[ed] += c - weight

print(ans)