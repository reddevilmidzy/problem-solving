n=int(input())
nums=sorted(list(map(int,input().split())))
f_idx, b_idx=0,n-1
ans=[]

while f_idx<b_idx:
    solution=nums[f_idx]+nums[b_idx]
    ans.append([abs(solution),nums[f_idx],nums[b_idx]])
    if solution <0:
        f_idx+=1
    elif solution>0:
        b_idx-=1
    else:
        print(nums[f_idx], nums[b_idx])
        exit()
ans.sort()
print(ans[0][1],ans[0][2])