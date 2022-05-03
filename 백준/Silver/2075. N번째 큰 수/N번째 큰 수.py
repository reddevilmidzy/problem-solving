import heapq

h = []
n = int(input())
for i in range(n):
    for j in map(int, input().split()):
        if len(h) < n:
            heapq.heappush(h, j)
        else:
            if h[0] < j:
                heapq.heappop(h)
                heapq.heappush(h, j)

print(h[0])