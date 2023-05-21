import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    v,e = map(int,input().split())
    print(2-v+e)