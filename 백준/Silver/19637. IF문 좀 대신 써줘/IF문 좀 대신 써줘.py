from bisect import bisect_left
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
name = []
level = []
for _ in range(n):
    a,b = map(str,input().split())
    name.append(a)
    level.append(int(b))

for _ in range(m):
    print(name[bisect_left(level, int(input()))])