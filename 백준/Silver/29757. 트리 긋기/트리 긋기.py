import sys,math
input = sys.stdin.readline

N =int(input())
co = []
for i in range(1,N+1):
    x,y = map(int,input().split())
    co.append((y,x,i))
    
co.sort()
dd = []

for i in range(N-1):
    y1,x1,t1 = co[i]
    y2,x2,t2 = co[i+1]

    if x2-x1:
        dd.append((y2-y1)/(x2-x1))
    else:
        dd.append(0)

if len(set(dd)) == 1:
    co.sort(key=lambda x:(x[0], x[1]))
    # print("같음")
    for i in range(N-1):
        print(co[i][2], co[i+1][2])
    exit()


y0,x0,n0 = co[0]
stk = []
for i in range(1,N):
    y,x,n = co[i]
    d = math.sqrt((x-x0)**2+(y-y0)**2)
    stk.append((int((x0-x)/d*1e12),int(d*1e12),n))
stk.sort()
cos = stk[-1][0]

for i in range(N-1):
    if stk[-i-1][0]!=cos:
        break
stk = stk[:-i]+sorted(stk[-i:],reverse=True)
print(n0, stk[0][2])
for i in range(len(stk)-1):
    print(stk[i][2], stk[i+1][2])
