from itertools import combinations

def dfs(depth: int) -> None:
    global cnt
    
    if depth == 15:
        cnt = 1
        for sub in res:
            if sub.count(0) != 3:
                cnt = 0
                break
        return
    
    g1, g2 = games[depth]
    for x, y in ((0,2), (1,1), (2,0)):
        if res[g1][x] > 0 and res[g2][y] > 0:
            res[g1][x] -= 1
            res[g2][y] -= 1
            dfs(depth+1)
            res[g1][x] += 1
            res[g2][y] += 1

ans = []
games = list(combinations(range(6), 2))

for _ in range(4):
    tmp = list(map(int, input().split()))
    res = [tmp[i:i+3] for i in range(0, 16, 3)]
    cnt = 0
    dfs(0)
    ans.append(cnt)
print(*ans)