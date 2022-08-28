import sys
input = sys.stdin.readline
n,w,h = map(int,input().split())
m=(w**2+h**2)**0.5
for _ in range(n): print('DA' if int(input()) <= m else 'NE')