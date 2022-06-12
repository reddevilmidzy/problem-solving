coord = [False] * 1001
n,l = map(int,input().split())
for i in map(int,input().split()):
    coord[i] = True

ans = 0
x = 0
while x <= 1000:
    if coord[x]:
        ans += 1
        x += l
    else:
        x +=1 
print(ans)