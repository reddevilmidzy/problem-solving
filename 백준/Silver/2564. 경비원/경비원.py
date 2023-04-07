import sys
input = sys.stdin.readline
# 1,2,3,4 북,남,서,동

m, n = map(int,input().split()) # 가로, 세로
k = int(input())
store = [list(map(int,input().split())) for _ in range(k)] # 상점 위치들
dirc, dist = map(int,input().split())
tmp = [0, m, m, n, n]
nm = {7:m, 3:n}
ans = 0

for way, far in store:
    tot = way + dirc
    if dirc == way: # 같은 방향에 있음
        ans += abs(dist - far)
    elif tot == 3 or tot == 7: # 북남 혹은 동서
        ans += min(dist + far, abs(tmp[dirc] - dist) + abs(tmp[way] - far)) + nm[tot]
    elif tot == 4: # 북서
        ans += far + dist
    elif tot == 6: # 동남
        ans += abs(tmp[way] - far) + abs(tmp[dirc] - dist)
    else: # 북동 혹은 남서
        if dirc == 1 or dirc == 3:
            ans += abs(tmp[dirc] - dist) + far
        else:
            ans += abs(tmp[way] - far) + dist
print(ans)