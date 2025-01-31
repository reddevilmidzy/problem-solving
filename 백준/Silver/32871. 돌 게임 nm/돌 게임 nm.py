import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    n,m = map(int,input().split())
    if n == 1 or m == 1:
        res.append("YES")
    elif n%2 == m%2:
        res.append("NO")
    else:
        res.append("YES")

print(*res,sep='\n')