from collections import deque
n,k = map(int,input().split())
dis = 5*int(1e5)


def bfs(st, ed):
    queue = deque()
    queue.append([st, 0, ed])
    visited = [[-1]*(dis+1) for _ in range(2)]
    visited[0][st] = 0
    while queue:
        node, time, target = queue.popleft()
        # print("node", node, "time", time, "target", target)
        if target > dis:
            return -1
        if visited[time%2][target] != -1:
            return time

        for nxt in [node-1, node+1, node*2]:
            if nxt < 0 or nxt > dis:
                continue
            if visited[(time+1)%2][nxt] == -1:
                queue.append([nxt, time+1, target+time+1])
                visited[(time+1)%2][nxt] = time + 1
    return -1
print(bfs(n, k))