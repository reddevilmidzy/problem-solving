import sys, heapq

input = sys.stdin.readline

leftheap = []
rightheap = []

for i in range(int(input())):
    n = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -n)
    else:
        heapq.heappush(rightheap, n)
    
    if rightheap and rightheap[0] < -leftheap[0]:
        leftval = heapq.heappop(leftheap)
        rightval = heapq.heappop(rightheap)

        heapq.heappush(leftheap, -rightval)
        heapq.heappush(rightheap, -leftval)
    
    print(-leftheap[0])