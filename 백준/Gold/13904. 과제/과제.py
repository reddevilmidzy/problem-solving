import heapq

n = int(input())
work = sorted([list(map(int,input().split())) for _ in range(n)], key= lambda x:(x[1]), reverse=True)
visited = [False]*1001
ans = 0

for day, score in work:
    i = day
    # 과제를 미룰 만큼 미루기, 최대한 늦게
    while i > 0 and visited[i]:
        i -= 1    
    # 할타임 놓치거나 이미 다른 과제가 있다면 그 과제는 패스
    if i == 0:
        continue
    # i번째 날에 과제를 함
    visited[i] = True
    ans += score

print(ans)