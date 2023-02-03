import sys, heapq
input = sys.stdin.readline

def solve():
    n = int(input())
    task = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:(x[0], x[1]))
    room = [0]
    for st, ed in task:
        
        if room[0] <= st:
            heapq.heapreplace(room, ed)
        else:
            heapq.heappush(room, ed)
    return len(room)
print(solve())