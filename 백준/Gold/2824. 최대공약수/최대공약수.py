import sys,math
input = sys.stdin.readline

n = int(input())
a_nums = list(map(int,input().rstrip().split()))
m = int(input())
b_nums = list(map(int,input().rstrip().split()))
a=1
b=1
for i in a_nums:
    a*=i
for i in b_nums:
    b*=i
ans = math.gcd(a,b)
print(ans) if len(str(ans)) < 10 else print(str(ans)[-9:])