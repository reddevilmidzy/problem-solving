import sys
input = sys.stdin.readline

n = int(input())
k = 12
m = 0
apple = 0
for _ in range(n):
    t,w,h,l = input().rstrip().split()
    w,h,l = int(w),int(h),int(l)
    if t == "A":
        cnt = (w//12)*(h//12)*(l//12)
        apple += cnt
        m += 1000 + (cnt*500)
    else:
        m += 6000

print(m)
print(apple*4000)