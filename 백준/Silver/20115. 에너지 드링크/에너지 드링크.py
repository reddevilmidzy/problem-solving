import sys
input = sys.stdin.readline

n=  int(input())
nums= sorted(list(map(int,input().split())))
ans = 0
sum_ans = sum(nums[:n-1])
if sum_ans%2==0:
    print(sum_ans//2+nums[n-1])
else:
    print(sum_ans/2+nums[n-1])
