n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]
tmp = [a-b for a,b in nums]
tmp.sort()
if n%2==1:print(1)
else:print(tmp[n//2]-tmp[n//2-1]+1)