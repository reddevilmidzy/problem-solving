import sys, heapq
input = sys.stdin.readline

h = []

for i in range(int(input().rstrip())):
    x = int(input().rstrip())
    if x != 0:
        heapq.heappush(h, x)
    elif x == 0:
        print(heapq.heappop(h)) if len(h) != 0 else print(0)
        
