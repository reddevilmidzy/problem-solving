ans = []
def bt(s):
    if sum(s) == n:
        ans.append(s[::])
        return
    elif sum(s) > n:
        return
    for i in nums:
        s.append(i)
        bt(s)
        s.pop()

n,k = map(int,input().split())
nums = [1,2,3]

bt([])
if len(ans) < k:
    print(-1)
else:
    print("+".join(map(str,ans[k-1])))