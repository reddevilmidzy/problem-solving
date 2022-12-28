import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
now = 100
candi = [abs(n-now)]
if n == 100:
    if m != 0:
        map(int,input().rstrip().split())
    candi.append(0)
elif m == 0:
    candi.append(len(str(n)))
elif m == 10:
    map(int,input().rstrip().split())

else:
    breakup = set(map(int,input().split()))
    if len(str(n)) == 1 and n not in breakup:
        candi.append(1)
    else:
        left = False
        right = False
        for i in range(500001):
            plus = set(map(int,str(n+i)))
            if len(plus) == len(plus-breakup) and not right:
                candi.append(len(str(n+i))+i)
                right = True
            if 0 <= n-i and not left:
                minus = set(map(int,str(n-i)))
                if len(minus) == len(minus-breakup):
                    candi.append(len(str(n-i))+i)
                    left = True
            if left and right:
                break         

print(min(candi))