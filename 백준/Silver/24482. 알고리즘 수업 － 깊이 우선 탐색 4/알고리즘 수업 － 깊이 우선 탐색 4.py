import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
def dfs(tree, v, visited):
    global cnt
    #visited[v] = True # 방문 처리
    ans[v] = cnt # 깊이 저장
    
    for i in sorted(tree[v], reverse=True): # 내림차순으로
        if not visited[i]: # 방문하지 않았다면 해당 정점 방문
            visited[i] = True
            cnt += 1 
            dfs(tree,i,visited)
            cnt -= 1 
n, m, r = map(int, input().rstrip().split())
visited = [False for i in range(n+1)] # 방문체크리스트
ans = [-1 for i in range(n+1)] # 정점 i의 깊이를 담을 리스트, 값을 -1로 한 이유: 방문하지 않은 정점처리를 위해.
tree= [[] for t in range(n+1)] # 그래프
cnt = 0
# 주어진 간선 정보 저장
for i in range(m):
    u,v = map(int, input().rstrip().split())
    tree[u].append(v)
    tree[v].append(u)
# 함수 호출
visited[r] = True
dfs(tree, r, visited)
print(*ans[1:], sep='\n')