from collections import defaultdict

n,p,q = map(int,input().split())
dp = defaultdict(int)
dp[0] = 1

def recursion(n,p,q):
    if n == 0:
        return 1
    
    if dp[n//p]==0:
        dp[n//p] = recursion(n//p,p,q)
    if dp[n//q]==0:
        dp[n//q] = recursion(n//q,p,q)
    return dp[n//p]+dp[n//q]

print(recursion(n,p,q))