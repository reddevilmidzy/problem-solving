import sys, math
input = sys.stdin.readline

a, b, v = map(int, input().rstrip().split())
high = v - a
up = a - b

print(math.ceil(high/up)+1)