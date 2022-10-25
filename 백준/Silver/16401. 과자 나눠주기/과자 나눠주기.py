import sys
input = sys.stdin.readline

m,n = map(int,input().split())
nums = sorted(list(map(int,input().split())), reverse=True)

def binary_search():
    st = 1
    ed = nums[0]
    ans = [0]
    while st <= ed:
        mid = (st+ed)//2
        snack = 0
        for i in nums:
            if i>=mid:
                snack += i//mid
            else:
                break

            if snack>=m:
                ans.append(mid)
                st = mid+1
                break

        if snack<m:
            ed = mid-1
    return max(ans)

print(binary_search())