from collections import defaultdict
from sys import stdin
input = stdin.readline

n = int(input())
balls = []
color = defaultdict(int)
size = defaultdict(int)

for i in range(n):
    c,s = map(int,input().split())
    balls.append([i, c, s, 0, 0])
balls.sort(key=lambda x:(x[2], x[1]))

for i in range(n):
    balls[i][3] = balls[i-1][3] + balls[i][2]
    color[balls[i][1]] += balls[i][2]
    size[balls[i][2]] += balls[i][2]

    balls[i][4] = balls[i][3] - color[balls[i][1]] - size[balls[i][2]] + balls[i][2]
    if balls[i][2] == balls[i-1][2] and balls[i][1] == balls[i-1][1]:
        balls[i][4] = balls[i-1][4]

balls.sort()
print(*[ball[4] for ball in balls], sep='\n')