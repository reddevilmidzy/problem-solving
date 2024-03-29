import sys
input = sys.stdin.readline
def solve():
    n,k,y,x = map(int,input().split())
    k *= k
    ans = 0

    for _ in range(n):
        r,c = map(int,input().split())
        ans += ((y-r)**2 + (x-c)**2) > k
    return ans
print(solve())