n=int(input())
nums=sorted(list(map(int,input().split())))
f_idx, b_idx=0,n-1
ans=[2000000000,0,0]

while f_idx<b_idx:
    solution=nums[f_idx]+nums[b_idx]
    if ans[0]>abs(solution):
        ans[0]=abs(solution)
        ans[1]=nums[f_idx]
        ans[2]=nums[b_idx]
    if solution <0:
        f_idx+=1
    elif solution>0:
        b_idx-=1
    else:
        print(nums[f_idx], nums[b_idx])
        exit()
print(ans[1],ans[2])