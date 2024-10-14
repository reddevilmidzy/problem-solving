import sys, math
input = sys.stdin.readline

n,k = map(int,input().split())
p = list(map(int,input().split()))
t = list(map(int,input().split()))
tot = 0

# 부족한 목표 수치
need = [max(0, t[i]-p[i]) for i in range(n)]
# i에서 소리친 횟수
cnt = [0] * n
# 외쳐서 얻은 추가 파워
power = 0
res = 0
for i in range(n):
    need[i] -= power

    if need[i] > 0:
        cnt[i] += math.ceil(need[i] / k)

    # 총외친횟수
    tot += cnt[i]
    if i > k - 1:
        tot -= cnt[i - k]
    power = power + cnt[i] * k - tot
    res += cnt[i]
print(res)