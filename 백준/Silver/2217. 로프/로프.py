import sys
input = sys.stdin.readline

n = int(input())
roof = sorted([int(input()) for _ in range(n)])
ans = []
for i in roof:
    ans.append(i*n)
    n -=1

print(max(ans))