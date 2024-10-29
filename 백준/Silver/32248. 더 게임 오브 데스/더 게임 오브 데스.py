from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

visited = [-1] * n
queue = deque([0])
visited[0] = 0
cnt = 0
pre = -1
st = -1
while queue:
    cur = queue.popleft()

    nxt = nums[cur] - 1
    if visited[nxt] == -1:
        visited[nxt] = visited[cur] + 1
        queue.append(nxt)
    else:
        st = nxt
        pre = visited[nxt]
        cnt = visited[cur] - visited[nxt] + 1
    
#pre = 사이클있기전꺼
#cnt = 사이클거리
#st = 사이클 시작
# print('visit', visited)
# print('k', k, 'st', st, 'pre',pre,'cnt',cnt)
if k < pre:
    # print('여기')
    print(visited.index(k) + 1)
else:
    tmp = (k - pre) % cnt
    queue = deque([st])
    res = st
    while tmp:
        cur = queue.popleft()
        queue.append(nums[cur] - 1)
        res = nums[cur] - 1
        tmp -= 1

    print(res + 1)