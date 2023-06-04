from collections import Counter

def bt(s:list[int], arr: list[int], is_left: bool, visited: list[bool]):
    if 0 < len(s) <= len(arr):
        if is_left: left.append(sum([arr[i] for i in s]))
        else: right.append(sum([arr[i] for i in s]))
        if len(s) == len(arr): return
    for i in range(len(arr)):
        if not visited[i] and (s and s[-1] < i) or (not s):
            s.append(i); visited[i] = True
            bt(s, arr, is_left, visited)
            visited[i] = False; s.pop()

n,s = map(int,input().split())
nums = list(map(int,input().split()))
left = [0]
right = [0]
ans = 0 if s else -1

bt([], nums[:n//2], True, [False]*((n+1)//2))
bt([], nums[n//2:], False, [False]*((n+1)//2))
left_cnt = Counter(left)
right_cnt = Counter(right)

for key, val in left_cnt.items():
    if s - key in right_cnt:
        ans += val*right_cnt[s-key]

print(ans)