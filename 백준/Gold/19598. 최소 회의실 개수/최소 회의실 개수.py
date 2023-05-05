import sys, heapq
input = sys.stdin.readline

n = int(input())
times = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))

room = [0]

for st, ed in times:
    if st >= room[0]:
        heapq.heapreplace(room, ed)
    else:
        heapq.heappush(room, ed)
print(len(room))