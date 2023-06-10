import sys
input = sys.stdin.readline

rival = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

n = int(input())
dices = [list(map(int,input().split())) for _ in range(n)]
eyes = {i for i in range(1, 7)}
ans = 0
for i in range(1, 7): # 주사위 눈 갯수
    tmp = 0
    cur = i
    for j in range(n):
        nxt_idx = rival[dices[j].index(cur)]        
        tmp += max(eyes - {cur} - {dices[j][nxt_idx]})
        cur = dices[j][nxt_idx]
    if tmp > ans:
        ans = tmp
print(ans)