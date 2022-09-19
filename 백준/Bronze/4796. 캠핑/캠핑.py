import sys
input = sys.stdin.readline
idx = 0
while True:
    idx += 1
    l,p,v = map(int,input().split())
    if l*p*v==0:
        break
    tmp = (v//p)*l
    if v%p>l:
        tmp += l
    else:
        tmp += v%p
    #ans = tmp+v%p
    print(f'Case {idx}: {tmp}')
