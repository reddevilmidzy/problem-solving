import sys
input = sys.stdin.readline

n,c = map(int,input().split())
m = int(input())
works = sorted([list(map(int,input().split())) for _ in range(m)], key=lambda x:(x[1], x[0]))
up = [0]*(n+1)
ans = 0

for st, ed, box in works:
    weight = min(box, c-max(up[st:ed]))
    if weight > 0:
        for i in range(st, ed):
            up[i] += weight
    ans += weight

print(ans)