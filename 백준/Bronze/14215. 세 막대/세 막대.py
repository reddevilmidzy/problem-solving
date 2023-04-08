a,b,c = sorted(list(map(int,input().split())))
while a+b <= c:c-=1
print(a+b+c)