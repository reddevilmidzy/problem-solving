n = int(input())
for i in range(1,n):
    print(" "*(i-1)+"*"*(n-i)+"*"+"*"*(n-i))
for i in range(n,0, -1):
    print(" "*(i-1)+"*"*(n-i)+"*"+"*"*(n-i))