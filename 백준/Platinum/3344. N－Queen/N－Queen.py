def pr1(st):
    for i in range(st,t+1):
        print(i*2)
def pr2(st,ed):
    for i in range(st,ed):
        print(i*2+1)
n = int(input())
t = n//2
if n%6==2:
    pr1(1)
    print(3)
    print(1)
    pr2(3,t)
    print(5)
elif n%6==3:
    pr1(2)
    print(2)
    pr2(2,t+1)
    print(1)
    print(3)
else:
    for i in range(2, n+1,2):
        print(i)
    for i in range(1, n+1, 2):
        print(i)