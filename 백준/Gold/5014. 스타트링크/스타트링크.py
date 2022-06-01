from collections import deque
f,s,g,u,d = map(int, input().split())

# f= 총 층의 계수
# s는  강호의 위치층
#  g= 스타트링크의 위치
# u= 위로 갈수 있는 층
# d= 아래로 갈 수 있는 층
# 가능하다면 누른 버튼 최소값
# 불가하다면 use the stairs
visited = [False for i in range(f+1)]
def bfs():
    queue = deque()
    queue.append((s, 0))
    while queue:
        now, cnt = queue.popleft()
        candi = [now+u, now-d]
        for i in candi:
            if 0 < i <= f:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, cnt+1))
                    if i == g:
                        return cnt+1
    return "use the stairs"
if s == g:
    print(0)
else:
    visited[s] = True
    print(bfs())