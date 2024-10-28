import sys
input = sys.stdin.readline

n,s = map(int,input().split())
nums = list(map(int,input().split()))
pre_fix = [0]
for num in nums:
    pre_fix.append(num+pre_fix[-1])
st,ed = 0,1
ans = []
while ed <= n:
    tmp = pre_fix[ed] - pre_fix[st]
    if tmp == s:
        ans.append(ed-st)
        ed += 1
    elif tmp < s:
        ed += 1
    else:
        ans.append(ed-st)
        st += 1
print(min(ans) if ans else 0)