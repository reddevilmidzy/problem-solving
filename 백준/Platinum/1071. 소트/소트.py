import sys
input = sys.stdin.readline

n = int(input())
csort = [0 for i in range(1002)]
nums = list(map(int,input().rstrip().split()))

for i in range(n):
    csort[nums[i]] += 1

ans = ''
while True:
    tof = False
    for i in range(1001):
        if csort[i]:
            tof=True
            if csort[i+1]:
                k =- 1
                for j in range(i+2, 1001):
                    if csort[j]:
                        k=j
                        break
                if k != -1:
                    while csort[i]:
                        ans+= str(i)+' '
                        csort[i]-=1
                    ans +=str(k)+' '
                    csort[k] -=1
                    break
                else:
                    ans += str(i+1)+' '
                    csort[i+1] -=1
                    break
            else:
                while csort[i]:
                    ans+= str(i)+' '
                    csort[i] -= 1
                break
    if not tof:
        break
print(ans)