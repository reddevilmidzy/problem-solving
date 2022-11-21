import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))
INF = int(1e7)

ans = INF
doll = 0
st_dis = 0
ed_dis = 0
queue = deque()

for idx,i in enumerate(nums):
    if i==1:
        doll += 1
        queue.append(idx)
        if doll==0:
            st_dis = idx
        elif doll == k:
            ed_dis = idx
            st_dis = queue.popleft()
            ans = min(ans, max(ed_dis-st_dis+1,1))
            doll -= 1

print(ans if ans != INF else -1)
