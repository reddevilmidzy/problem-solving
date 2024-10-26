from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
left = dict()
right = defaultdict(int)
ss = set()
for _ in range(n):
    l,r = map(int,input().split())
    if r not in left:
        left[r] = l
    else:
        left[r] = min(l, left[r])
    right[l] = max(r, right[l])
    ss.add((l,r))

q = int(input())
for _ in range(q):
    l, r = map(int,input().split())

    if (l,r) in ss:
        print(1)
    elif r in left and left[r] <= l and r <= right[l]:
        print(2)
    else:
        print(-1)