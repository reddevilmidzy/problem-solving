import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = [i for i in range(1, n+1)]
pt = 0
ans = []
for i in range(n):
    pt += k-1
    pt %= len(arr)
    ans.append(arr.pop(pt))
print(f"<{', '.join(map(str, ans))}>")