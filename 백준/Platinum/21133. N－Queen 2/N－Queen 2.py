n = int(input())
t = n//2
if n%6==2:
    for i in range(1, t+1):
        print(i*2)
    print(3)
    print(1)
    for i in range(3, t):
        print(i*2+1)
    print(5)
elif n%6==3:
    for i in range(2, t+1):
        print(i*2)
    print(2)
    for i in range(2, t+1):
        print(i*2+1)
    print(1)
    print(3)
else:
    for i in range(2, n+1,2):
        print(i)
    for i in range(1, n+1, 2):
        print(i)