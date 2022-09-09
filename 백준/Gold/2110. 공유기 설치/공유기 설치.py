import sys
input = sys.stdin.readline

n,c = map(int,input().split())
con = sorted([int(input()) for _ in range(n)])

low = 1
high = con[-1]-con[0]
ans = []

def check(dist):
    cnt = 1
    pre = con[0]
    for i in range(1,n):
        if con[i]-pre >= dist:
            cnt += 1
            pre = con[i]

    return cnt >= c

while low <= high:
    mid = (low+high)//2
    if check(mid):
        ans.append(mid)
        low = mid+1
    else:
        high = mid-1

print(max(ans))