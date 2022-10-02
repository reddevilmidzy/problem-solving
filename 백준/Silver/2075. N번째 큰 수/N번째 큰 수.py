import sys,heapq
input = sys.stdin.readline

h = []
n = int(input())
for _ in range(n):
    for i in map(int,input().split()):
        if len(h)<n:
            heapq.heappush(h, i)
        else:
            if h[0]<i:
                # 메모리 초과 방지를 위해
                heapq.heappop(h)
                heapq.heappush(h, i)
                
print(heapq.heappop(h))