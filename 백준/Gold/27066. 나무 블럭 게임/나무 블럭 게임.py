import sys
input = sys.stdin.readline

def index(k):
    return (k+1)//2 - 1
n = int(input())
nums = sorted(list(map(int,input().split())))
res = 0
pocket = [[] for _ in range(n)]
cnt = max(1, n-3)

while cnt <= n:
    idx = 0
    pocket = [[] for _ in range(n-cnt+1)]
    for i in range(len(pocket)):
        if i==0:
            for j in range(cnt):
                pocket[i].append(nums[idx])
                idx += 1
        else:
            pocket[i].append(nums[idx])
            idx += 1
    cnt += 1
    avg = []

    for q in range(len(pocket)):
        avg.append(sum(pocket[q])/len(pocket[q]))

    avg.sort()
    res = max(res, avg[index(len(pocket))])
print(res)