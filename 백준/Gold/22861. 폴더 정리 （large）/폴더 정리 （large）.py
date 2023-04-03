from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(folder):
    queue = deque()
    queue.append(folder)
    res = []

    while queue:
        f = queue.popleft()

        if f not in tree: # 폴더가 아니라 파일이라면 
            res.append(f)
            continue
        for child in tree[f]:
            queue.append(child)

    return res

n,m = map(int,input().split()) # 폴더, 파일
tree = defaultdict(list)

for _ in range(n+m):
    p,f,c = map(str,input().rstrip().split())
    if c == "1":
        tree[p].append(f)
        if f not in tree:
            tree[f] = []
    else:
        tree[p].append(f)

k = int(input())
for _ in range(k):
    y_route, x_route = map(str,input().rstrip().split())
    x = list(map(str, x_route.split("/")))[-1]
    y_route = list(map(str, y_route.split("/")))
    y, y_par = y_route[-1], y_route[-2]
    tree[x].extend(tree[y])
    tree[x] = list(set(tree[x]))
    tree[y_par].remove(y)
    del tree[y]

q = int(input())
for _ in range(q):
    route = list(map(str, input().rstrip().split("/")))
    ans = bfs(route[-1])
    print(len(set(ans)), len(ans))