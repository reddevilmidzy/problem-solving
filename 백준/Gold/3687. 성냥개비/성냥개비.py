import sys
input = sys.stdin.readline

def formatted(arr:int, num:int, maxable:bool) -> int:
    if arr != 0 and arr != sys.maxsize:
        arr = list(str(arr)) + [str(num)]
        arr.sort(reverse=maxable)
    else:
        arr = [str(num)]
        arr.sort(reverse=maxable)
    while arr[0] == "0":
        for i in range(len(arr)):
            if arr[i] != "0":
                arr[0],arr[i] = arr[i],arr[0]
                break
        else: # 전부 0임
            if maxable:
                return 0
            return sys.maxsize
    return int("".join(arr))

t = int(input())
nums = {2:["1"], 3:["7"], 4:["4"], 5:["2","3","5"], 6:["0","6","9"], 7:["8"]}

for _ in range(t):
    n = int(input())
    dp = [False] * (n+1)
    dp[0] = True

    min_num_dp = [sys.maxsize] * (n+1)
    max_num_dp = [0] * (n+1)

    for i in range(n+1):
        for j in [2,3,4,5,6,7]:
            if dp[i] and i + j <= n:
                dp[i+j] = True
                for k in nums[j]:
                    min_num_dp[i+j] = min(formatted(min_num_dp[i], k, False), min_num_dp[i+j])
                    max_num_dp[i+j] = max(formatted(max_num_dp[i], k, True) , max_num_dp[i+j])

    print(min_num_dp[n], max_num_dp[n])