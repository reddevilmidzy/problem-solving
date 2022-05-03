import sys, heapq
h = []
input = sys.stdin.readline
for i in range(int(input().rstrip())):
    a = list(map(int, input().rstrip().split()))
    if a == [0]:
        if len(h) == 0:
            print(-1)
        else:
            print(-heapq.heappop(h))
    else:
        for j in a[1:]:
            heapq.heappush(h, -j)