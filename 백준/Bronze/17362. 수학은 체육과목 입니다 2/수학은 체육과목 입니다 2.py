n = int(input())
if n <= 5: print(n)
elif (n-1)%8==0:
    print(1)
elif (n-3)%4==0:
    print(3)
elif (n-5)%8==0:
    print(5)
elif ((n-1)%8)%7 < (n-3)%4 < (n-5)%8:
    print(2)
else:
    print(4)