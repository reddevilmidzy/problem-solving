import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
s = set()
check = set()
for i in range(n):
    s.add(input().rstrip())
cnt = 0
for j in range(m):
    word = input().rstrip()
    if word in s:
        cnt += 1
print(cnt)