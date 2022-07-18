import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
tree = list(map(int,input().rstrip().split()))
def binary_search(start, end, cut):
    res = []
    while start <= end:
        ans = 0
        mid = (start+end)//2
        for i in tree:
            if i > mid:
                ans += i-mid
        if ans < m:
            end = mid-1
        elif ans >= m:
            res.append([ans,mid])
            start = mid+1
    return sorted(res)[0][1]
print(binary_search(0, max(tree), max(tree)))