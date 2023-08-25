while True:
    n = int(input())
    if n<0:break

    nums = []
    for i in range(1, n):
        if n%i==0:
            nums.append(i)
    if sum(nums) == n:
        print(n,"=",end=' ')
        print(*nums,sep=" + ")
    else:
        print(f"{n} is NOT perfect.")