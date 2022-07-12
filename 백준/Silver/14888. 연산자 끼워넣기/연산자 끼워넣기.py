def back_tracking(index, sum):
    global min_ans
    global max_ans
    if index==n-1:
        if min_ans > sum:min_ans = sum
        if max_ans < sum:max_ans = sum
        return
    for i in range(4):
        tmp = sum
        if operator[i]==0: continue # 연산자가 없다면 건너띔
        if i==0:sum+=nums[index+1] # +
        elif i==1:sum-=nums[index+1] # -
        elif i==2:sum*=nums[index+1] # *
        else:
            if sum<=0:sum = abs(sum)//nums[index+1]*-1
            else:sum //=nums[index+1]
        operator[i] -=1
        back_tracking(index+1, sum)
        operator[i] +=1
        sum = tmp

n = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
operator = list(map(int,input().rstrip().split()))
min_ans = float('Inf')
max_ans = float('-Inf')

back_tracking(0, nums[0])
print(max_ans,min_ans,sep='\n')