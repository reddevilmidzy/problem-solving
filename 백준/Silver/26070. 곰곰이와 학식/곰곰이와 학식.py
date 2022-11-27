a,b,c = map(int,input().split())
x,y,z = map(int,input().split())
pre_ans = 0
ans = min(a,x) + min(b,y) + min(c,z)
ta = min(a,x)
tb = min(b,y)
tc = min(c,z)
a -= ta
b -= tb
c -= tc
x -= ta
y -= tb
z -= tc

while (x+y+z)>=0:
    if x>0:
        y += x//3
        x %= 3
        tmpy = min(b,y)
        ans, y, b = ans + tmpy, y-tmpy, b-tmpy

    if y>0:
        z += y//3
        y %= 3
        tmpz = min(c,z)
        ans, z, c = ans + tmpz, z-tmpz, c-tmpz

    if z>0:
        x += z//3
        z %= 3
        tmpx = min(a,x)
        ans, x, a = ans + tmpx, x-tmpx, a-tmpx

    if pre_ans == ans:
        break
    pre_ans = ans
    
print(ans)