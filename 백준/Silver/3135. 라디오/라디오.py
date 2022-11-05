import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n = int(input())
stars = [int(input()) for _ in range(n)]
res = abs(a-b)
for star in stars:
    res = min(res, abs(star-b)+1)
print(res)