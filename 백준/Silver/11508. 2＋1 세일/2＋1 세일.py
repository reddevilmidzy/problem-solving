import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = []
ans = 0
for i in range(n):
    pricetag = int(input().rstrip())
    arr.append(pricetag)

arr.sort(reverse=True)

for j in range(n):
    if (j+1)%3 == 0:
        pass
    else:
        ans += arr[j]
print(ans)
