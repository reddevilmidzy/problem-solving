import sys
input = sys.stdin.readline

def solve(n,m):
    res = 0
    for i in range(n, m+1):
        res += str(i).count('0')
    return res

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(solve(n,m))