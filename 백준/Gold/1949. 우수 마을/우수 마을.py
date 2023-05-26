import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
dp = [[0]*2 for _ in range(n+1)]

# dp 2차원으로 만들고
# dp[i][1] => i번째 마을 우수마을
# dp[i][0] => i번째 마을 우수마을 아님
def dfs(cur: int):
    visited[cur] = True
    dp[cur][0] = 0
    dp[cur][1] = nums[cur]

    for nxt in tree[cur]:
        if not visited[nxt]:
            dfs(nxt)
            dp[cur][0] += max(dp[nxt][0], dp[nxt][1])
            dp[cur][1] += dp[nxt][0]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False]*(n+1)

dfs(1)
print(max(dp[1]))
