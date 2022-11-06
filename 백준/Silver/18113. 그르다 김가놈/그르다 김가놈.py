import sys
input = sys.stdin.readline

def bise():
    st = 1
    ed = max(cut_kimbab)
    ans = [-1]
    while st <= ed:
        mid = (st+ed)//2
        piece = 0
        for i in cut_kimbab:
            piece += i//mid
        
        if piece >= m:
            ans.append(mid)
            st = mid+1
        else:
            ed = mid-1
    return max(ans)

n,k,m = map(int,input().split())
length = [int(input()) for _ in range(n)]
cut_kimbab = []
for i in length:
    if i <= k:
        pass
    elif i < 2*k:
        cut_kimbab.append(i-k)
    else:
        cut_kimbab.append(i-2*k)

if len(cut_kimbab)==0:
    print(-1)
    exit()
    
cut_kimbab.sort()

print(bise())