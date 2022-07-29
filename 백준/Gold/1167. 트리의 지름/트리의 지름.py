import sys
from collections import deque
input=sys.stdin.readline

v=int(input())
graph = [[] for _ in range(v+1)]
for i in range(v):
    nums=list(map(int,input().rstrip().split()))
    for j in range(1,len(nums)-2,2):
        graph[nums[0]].append([nums[j], nums[j+1]])
    
def bfs(start):
    visited = [-1]*(v+1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    max_val = [0,0]

    while queue:
        q = queue.popleft()
        for e,w in graph[q]:
            if visited[e] == -1:
                visited[e] = visited[q] + w
                queue.append(e)
                if max_val[0] < visited[e]:
                    max_val = visited[e], e
    return max_val

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)