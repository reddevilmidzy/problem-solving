n = int(input())
nums = list(map(int,input().split()))
x = int(input())
unstable = nums.count(1)

if unstable > 2:
    print("NO")
elif unstable == 2:
    unstable_idx = nums.index(1)
    if unstable_idx + x <= n and nums[unstable_idx + x] == 1:
        print("YES")
        print(unstable_idx, unstable_idx + x)
    else: # 2개지만 도달 불가
        print("NO")
elif unstable == 1:
    unstable_idx = nums.index(1)
    if unstable_idx + x <= n and nums[unstable_idx + x] != 0:
        print("YES")
        print(unstable_idx, unstable_idx + x)
    elif unstable_idx - x >= 0 and nums[unstable_idx - x] > 2:
        print("YES")
        print(unstable_idx - x, unstable_idx)
    else:
        print("NO")
else: # 1인녀석이 빵개
    # 그렇다면 2는 건드리지 않고 이동할수 있는 놈이 있나 찾아봐야지
    for i in range(n - x+1): # n 까지 도는 이유는 마지막놈은 차피 이동 못함
        # 2가 아니고, x만큼 이동시 범위 안이고, 0이 아닌 경우
        if nums[i] > 2 and nums[i+x] != 0:
            print("YES")
            print(i, i+x)
            break
    else:
        print("NO")