from heapq import heappush, heappop, heapify
from sys import stdin
input = stdin.readline

n,k = map(int,input().split())
nums = [list(map(int,input().split())) for _ in range(n)]

# k 개의 카운터
counter = [(0,i) for i in range(k)]
heapify(counter)

time = [0]*k
done = []

for i in range(n):
    t,x = heappop(counter)
    time[x] += nums[i][1] # 시간 추가
    heappush(counter, (time[x], x))
    done.append((time[x], -x, i))

print(sum(nums[val[2]][0]*i for i,val in enumerate(sorted(done), 1)))