import sys
input = sys.stdin.readline

def div(k: int) -> dict:
    ans = 0
    for i in range(1, k+1):
        if i*i >= k: 
            ans += +(i*i==k)
            break
        if k%i==0:
            ans += 2
    return ans

n = int(input())
ans = []
for _ in range(n):
    u,v = map(int,input().split())
    
    res = 0
    for i in range(u, v+1):
        res = max(res, div(i))
    
    ans.append(res)
print(*ans,sep='\n')