def multi(nums:list[int]) -> int:
    res = 1
    for num in nums:
        res *= num
    return res

n,q = map(int,input().split())
nums = list(map(int,input().split()))
query = list(map(int,input().split()))
nums.extend(nums[:3])
arr = []
for i in range(n):
    arr.append(multi(nums[i:i+4]))

tot = sum(arr)
tmp = 0

for k in query:
    for i in range(k-4, k):
        tmp -= 2*arr[i]
        arr[i] *= -1
    print(tot + tmp)