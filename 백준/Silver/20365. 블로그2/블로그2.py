import sys
input = sys.stdin.readline

n=int(input())
word=input().rstrip()
pre = word[-1]
ans = 1

for i in range(n-2,-1,-1):
    if pre != word[i] and word[i]!=word[i+1]:
        ans += 1

print(ans)