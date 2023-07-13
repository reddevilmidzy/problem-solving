from collections import Counter
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

def ccw(a1, b1, a2, b2, a3, b3):
    tmp = (a2-a1)*(b3-b1)-(b2-b1)*(a3-a1)
    if tmp > 0: return 1
    elif tmp < 0: return -1
    return 0

def is_crossed(x1,y1,x2,y2,x3,y3,x4,y4):
    first = ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4)
    second = ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2)

    if first == 0 and second == 0: return max(x1,x2) >= min(x3,x4) and max(x3,x4) >= min(x1,x2) and max(y1,y2) >= min(y3,y4) and max(y3,y4) >= min(y1,y2)
    return first <= 0 and second <= 0

n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]

cross = []
parent = [i for i in range(n)]

for i in range(n):
    for j in range(i+1, n):
        x1,y1,x2,y2 = nums[i]
        x3,y3,x4,y4 = nums[j]

        if is_crossed(*nums[i], *nums[j]):
            cross.append((i,j))

for a,b in cross:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

for x in range(n):
    parent[x] = find(parent, x)

print(len(set(parent)))
print(Counter(parent).most_common(1)[0][1])