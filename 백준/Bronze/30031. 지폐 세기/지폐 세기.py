import sys
input = sys.stdin.readline
d = {136:1000, 142:5000, 148:10000, 154:50000}
n = int(input())
res = 0
for _ in range(n):
    x,y = map(int,input().split())
    res += d[x]
print(res)