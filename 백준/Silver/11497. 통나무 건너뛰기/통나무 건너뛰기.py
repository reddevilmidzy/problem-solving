import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int,input().split())))
    res = [0]*n
    if nums[0]==nums[-1]: # 정렬했는데 앞뒤 같다면 모두 같다는 의미
        print(0)

    else:
        high = nums[-1]
        low = nums[0]
        res[0] = low
        if n%2==0: 
            res[n//2]=high
        else:
            res[n//2+1]=high
        idx = 1
        for i in range(1, n-1,2):
            res[idx] = nums[i]
            idx +=1
        idx += 1
        if i==n-2:
            i -=1
        elif i==n-3:
            i+=1
        for i in range(i,1,-2):
            res[idx] = nums[i]
            idx += 1

        ans = res[-1]-res[0]
        for i in range(1,n):
            ans = max(ans, abs(res[i]-res[i-1]))
        print(ans)