import sys
input = sys.stdin.readline

to_int = lambda x: ord(x) - ord('A')

def solve(a:int, b:int, c:int, pre):
    if a+b+c == n:
        print(''.join(res))
        exit()

    if dp[a][b][c][pre[0]][pre[1]]:
        return False
    
    dp[a][b][c][pre[0]][pre[1]] = True

    if cnt[0] >= a+1:
        res[a+b+c] = 'A'
        if solve(a+1,b,c,[pre[1], 0]):
            return True

    if cnt[1] >= b+1:
        res[a+b+c] = 'B'
        if pre[1] != 1 and solve(a,b+1,c,[pre[1], 1]):
            return True
    
    if cnt[2] >= c+1:
        res[a+b+c] = 'C'
        if pre[0] != 2 and pre[1] != 2 and solve(a,b,c+1,[pre[1], 2]):
            return True

    return False
    
s = input().rstrip()
n = len(s)
cnt = [0]*3
res = [''] * n
dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(len(s))] for _ in range(len(s))] for _ in range(len(s))]

for i in s:
    cnt[to_int(i)] += 1

solve(0,0,0,[0,0])
print(-1)