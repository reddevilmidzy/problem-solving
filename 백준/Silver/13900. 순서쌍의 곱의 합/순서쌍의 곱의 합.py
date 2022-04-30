import sys

input = sys.stdin.readline

n = int(input().rstrip())
# n = 3
lis = list(map(int, input().rstrip().split()))
# lis = [2,3,4]
s = sum(lis)
ans = 0

# 아에 시작부터 합 구하고 빼기로
for i in lis:
    s = s - i
    ans += i * s
print(ans) 