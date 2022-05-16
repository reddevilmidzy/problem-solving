import sys
input = sys.stdin.readline
n = int(input().rstrip())
room = []
for i in range(n):
    start, finish = map(int, input().rstrip().split())
    room.append([start, finish])

room.sort(key= lambda x : x[0])
room.sort(key= lambda x : x[1])

cnt = 1
end = room[0][1]
for j in range(1, n):
    if room[j][0] >= end:
        cnt += 1
        end = room[j][1]

print(cnt)