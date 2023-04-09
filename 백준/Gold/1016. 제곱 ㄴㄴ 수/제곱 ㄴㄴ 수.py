n,m = map(int,input().split())
last = int(m**0.5)
arr = [1]*(m-n+1)
sqr = 2
while sqr <= last:
    i = sqr**2
    tmp = (n//i)*i
    while tmp<=m:
        if n <= tmp:
            arr[tmp-n] = 0
        tmp += i
    sqr += 1
print(sum(arr))