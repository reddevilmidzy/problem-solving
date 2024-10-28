n,k=map(int,input().split())
m=sorted(list(map(int,input().split())))
l,r=0,n-1
a=0
while l<=r:
    if m[r]>=k:
        a+=1
        r-=1
    elif m[l]+m[r]>=k and l!=r:
        a+=1
        l+=1
        r-=1
    else:l+=1
print([-1,a][a!=0])