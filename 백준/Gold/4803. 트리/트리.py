import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(cur:int, pre:int):
    visited[cur] = True
    for nxt in tree[cur]:
        if nxt != pre:
            if not visited[nxt]:
                dfs(nxt, cur)
            else:
                global is_tree
                is_tree = False
                return

case_cnt = 0

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0: break
    case_cnt += 1

    tree = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    t = 0
    for _ in range(m):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)

    for cur in range(1, n+1):
        is_tree = True
        if not visited[cur]:
            t += 1
            dfs(cur, -1)
            if not is_tree:
                t -= 1
    print(f"Case {case_cnt}: ", end='')
    if t == 0:
        print("No trees.")
    elif t == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {t} trees.")