n,m = map(int,input().split())
if n == 1 and m == 1:
    print("1\n1")
elif n == 1:
    print(2)
    print(*[i%2+1 for i in range(m)],sep='\n')
elif m == 1:
    print(2)
    print(*[i%2+1 for i in range(n)])
else:
    print(4)
    for i in range(n):
        if i%2==0:
            print(*[i%2+1 for i in range(m)])
        else:
            print(*[i%2+3 for i in range(m)])