nums = input()
n = len(nums)
max_val = 25000

def solve():
    idx = 0
    for i in range(1, max_val + 1):
        char = str(i)
        for j in range(len(char)):
            if nums[idx] == char[j]:
                idx += 1
            if idx == n:
                return i
print(solve())