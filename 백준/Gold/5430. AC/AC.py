import sys
input = sys.stdin.readline

for _ in range(int(input())):
    code = input().rstrip()
    n = int(input())
    nums = list(map(str,input().rstrip().split(',')))
    rev = 0
    left = 0
    right = 0
    for i in code: 
        if i == 'R':
            rev += 1
        else:
            if rev%2==0:
                left += 1
            else:
                right += 1
        if n < (left + right):
            print("error")
            break
    else:
        nums[0] = nums[0].replace('[','')
        nums[-1] = nums[-1].replace(']','')
        #print(nums, left, right,"rev: ",rev)
        #print(nums)
        #nums = list(map(int,nums))
        if rev%2 == 0:
            print('['+','.join(nums[left:n-right])+']')
        else:
            print('['+','.join(nums[left:n-right][::-1])+']')