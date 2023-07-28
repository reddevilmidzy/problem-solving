n = int(input())
y,x = map(int,input().split())
ans = []
for _ in range(n-1):
    r,c = map(int,input().split())
    ans.append((((y-r)**2 + (x-c)**2)**0.5, r,c))

ans.sort()
print(y,x)
print(ans[0][1], ans[0][2])
print(round(ans[0][0],2))