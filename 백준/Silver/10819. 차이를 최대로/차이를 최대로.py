import sys
input =sys.stdin.readline

n = int(input())
nums = list(map(int,input().rstrip().split()))
visited = [False] *n
s = []
ans = []
sumlist = []
def bfs():
    if len(s) == n:
        ans.append(list(map(int,s)))
    flag = 0
    for num in range(n):
        if not visited[num] and flag != nums[num]:
            visited[num] =True
            s.append(nums[num])
            flag = nums[num]
            bfs()
            visited[num] = False
            s.pop()
bfs()
def plus(lis):
    sumvalue = 0
    for i in range(n-1):
        sumvalue += abs(lis[i] - lis[i+1])
    sumlist.append(sumvalue)
for a in ans:
    plus(a)
print(max(sumlist))