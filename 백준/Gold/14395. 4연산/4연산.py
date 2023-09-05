from collections import deque

def bfs(s:int, t:int):
    if s == t:
        return 0
    
    queue = deque()
    queue.append(((s, "")))
    visited = set()
    visited.add(s)
    res = []
    while queue:
        cur,cmd = queue.popleft()
        if cur == t:
            res.append(cmd)
            continue
        for nxt,v in [(cur*cur, "*"), (cur+cur, "+"), (cur-cur, "-"), (cur//cur, "/")]:
            if nxt not in visited and 0 < nxt < INF:
                queue.append((nxt, cmd+v))
                if nxt != t:
                    visited.add(nxt)
    res.sort(key=lambda x:(len(x), x))
    return res[0] if res else -1

s,t = map(int,input().split())
INF = max(s,t)+1
print(bfs(s,t))