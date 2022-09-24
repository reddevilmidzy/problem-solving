import sys
input = sys.stdin.readline

n=int(input())
guast=sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0

for i in range(n):
    if guast[i]-i>0:
        ans += guast[i]-i

print(ans)