n =int(input())
for i in range(n-1, 0, -1):
    print("*"*(n-i)+" "*(i*2)+"*"*(n-i))
for i in range(n):
    print("*"*(n-i)+" "*(i*2)+"*"*(n-i))