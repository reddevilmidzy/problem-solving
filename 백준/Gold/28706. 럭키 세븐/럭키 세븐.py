import sys
input = sys.stdin.readline

def cal(pre, op, v):
    if op == "+":
        return (pre + v) % 7
    return (pre * v) % 7

def solve():
    dp = [[False]*7 for _ in range(n+1)] 
    dp[0][1] = True

    for i in range(n):
        op1,v1,op2,v2 = cmd[i]
        for j in range(7):
            if dp[i][j]:
                dp[i+1][cal(j, op1, int(v1))] = True
                dp[i+1][cal(j, op2, int(v2))] = True
    return dp[-1][0]
            

t = int(input())
for _ in range(t):
    n = int(input())
    cmd = [list(input().rstrip().split()) for _ in range(n)]
    print(["UNLUCKY", "LUCKY"][solve()])