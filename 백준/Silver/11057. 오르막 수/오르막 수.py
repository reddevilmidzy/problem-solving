n=int(input())
li = [0,10,9,8,7,6,5,4,3,2,1]
a=[0]
if n == 1:
    print(10)
else:
    n-=2
    while n:
        val = sum(li)
        for i in range(1, 11):
            a.append((val-sum(li[:i]))%10007)

        li = a
        a = [0]
        n -= 1
    print(sum(li)%10007)