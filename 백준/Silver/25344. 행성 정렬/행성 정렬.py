import math, sys
input = sys.stdin.readline

n = int(input())
planet = list(map(int,input().split()))
pre = planet[0]
for i in range(1, n-2):
    pre = math.lcm(pre, planet[i])
print(pre)