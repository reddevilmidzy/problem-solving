import sys
input = sys.stdin.readline

def dfs(tree, v, visited):
    global leaf
    visited[v] = True
    if len(tree[v]) == 0:
        leaf -= 1
    for i in tree[v]:
        if not visited[i]:
            dfs(tree, i, visited)

n = int(input())
nums = list(map(int,input().rstrip().split()))
tree = [[] for i in range(n)]
visited = [False for i in range(n)]
delete = int(input())
leaf = 0
for i in range(n):
    if nums[i] != -1:
        tree[nums[i]].append(i)
    else:
        parente = i
        pass

for i in tree:
    if len(i) == 0:
        leaf += 1

if parente == delete:
    print(0)
else:
    dfs(tree, delete, visited)
    if len(tree[nums[delete]]) == 1:
        leaf += 1
    print(leaf)