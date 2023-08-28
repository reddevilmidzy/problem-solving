from collections import defaultdict, deque
import sys
# sys.stdin = open("pythonfile/input.txt","r")
input = sys.stdin.readline

def dfs(cur):
    global idx,num

    idx += 1
    d[cur] = idx
    visited[cur] = True
    stk.append(cur)

    parent = d[cur]
    
    for nxt in graph[cur]:
        if d[nxt] == -1:
            parent = min(parent, dfs(nxt))
        elif visited[nxt]:
            parent = min(parent, d[nxt])
    
    if d[cur] == parent:
        scc = []
        while True:
            node = stk.pop()
            visited[node] = False
            scc.append(node)
            scc_dict[node] = num

            if cur == node: break
        num += 1
        scc_list.append(scc)
    
    return parent


def topology():
    queue = deque()
    res = {}
    for web in web_site:
        res[web] = 1
        if cnt[web] == 0:
            queue.append(web)

    # print(queue)
    # print("cnt",cnt)
    while queue:
        cur = queue.popleft()
        # print("cur", cur)
        for nxt in dag[cur]:

            cnt[nxt] -= 1
            res[nxt] += res[cur]
            if cnt[nxt] == 0:
                # print("nxt",nxt)
                queue.append(nxt)
    
    return res
    # print(res)

m = int(input())
graph = defaultdict(list)
web_site = set()

for _ in range(m):
    tmp = list(input().rstrip().split())
    nxt = tmp[0]
    web_site.add(nxt)
    for cur in tmp[2:]:
        graph[cur].append(nxt)
        web_site.add(cur)


s = input().rstrip()
n = len(web_site)
idx = 0
num = 0
d = {i:-1 for i in web_site}
stk = []
visited = {i:False for i in web_site}
scc_dict = dict()
scc_list = []


for cur in web_site:
    if d[cur] == -1:
        dfs(cur)

dag = {i:[] for i in web_site}
cnt = {i:0 for i in web_site}

for cur in web_site:
    for nxt in graph[cur]:
        if scc_dict[cur] != scc_dict[nxt]:
            dag[cur].append(nxt)
            # dag[scc_dict[cur]].append(scc_dict[nxt])
            cnt[nxt] += 1
        # print(scc_dict[cur], scc_dict[nxt])

# print(dag)
# print(graph)
# print(web_site)
# print(d)
# print(scc_dict)
# print(scc_list)
# print(cnt)

res = topology()
print(res[s])