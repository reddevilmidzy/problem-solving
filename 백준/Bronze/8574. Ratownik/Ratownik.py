import sys
input = sys.stdin.readline

def get_dist(y:int,x:int,r:int,c:int) -> int:
    return ((y-r)**2 + (x-c)**2)**0.5

n,k,y,x = map(int,input().split())
ans = 0

for _ in range(n):
    r,c = map(int,input().split())
    ans += get_dist(y,x,r,c) > k
print(ans)