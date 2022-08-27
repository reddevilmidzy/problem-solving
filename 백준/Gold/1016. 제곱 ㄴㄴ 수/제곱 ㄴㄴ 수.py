n,m = map(int,input().split())

sqrt_nums = [i**2 for i in range(2, int(m**0.5)+1)]
arr = [1]*(m-n+1)

for i in sqrt_nums:
    tmp = (n//i)*i # 시작값 변경 가능할 듯
    while tmp<=m:
        if n <= tmp and tmp <= m:
            arr[tmp-n] = 0
        tmp += i
print(sum(arr))