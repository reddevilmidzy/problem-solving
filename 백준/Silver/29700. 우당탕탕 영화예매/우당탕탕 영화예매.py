import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
s=[list(input().rstrip()) for _ in range(n)]

res = 0
for i in range(n):
    cur = 0
    for j in range(m):
        if s[i][j] == "0":
            cur += 1
        else:
            if cur >= k:
                res += cur-k+1
            cur= 0
    
    if cur >= k:
        res += cur-k+1

print(res)