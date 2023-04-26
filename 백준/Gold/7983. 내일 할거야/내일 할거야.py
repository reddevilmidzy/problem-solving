import sys
input = sys.stdin.readline

n = int(input())
task = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:-x[1])

day = task[0][1]

for d,t in task:
    if day >= t:
        day = t - d
    else:
        day -= d
print(day)