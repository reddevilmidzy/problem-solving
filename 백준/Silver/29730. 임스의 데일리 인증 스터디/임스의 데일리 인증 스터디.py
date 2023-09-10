import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []
pre = "boj.kr/"
for _ in range(n):
    s = input().rstrip()
    if pre == s[:7]:
        b.append(int(s[7:]))
    else:
        a.append(s)
a.sort(key=lambda x:(len(x), x))
b.sort()
if a:
    print(*a,sep='\n')
for i in b:
    print(f"{pre}{i}")