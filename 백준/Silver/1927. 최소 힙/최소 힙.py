import heapq, sys
input = sys.stdin.readline
h = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, n)