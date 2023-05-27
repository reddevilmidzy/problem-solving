import sys
input = sys.stdin.readline
n = int(input())
a,b,c,d,e,f = map(int,input().split())
center = min(a,b,c,d,e,f)
edge = min(a+b, a+c, a+e, a+d, f+c, f+e, f+d, f+b, c+b, b+d, d+e, e+c)
coner = min(a+c+e, a+b+c, a+b+d, a+d+e, f+b+c, f+b+d, f+d+e, f+e+c)
if n == 1:
    print(a+b+c+d+e+f-max(a,b,c,d,e,f))
else:
    n -= 2
    print((center*(n**2)*5)+4*(n*center)+coner*4+edge*(n*8+4))