D, K = map(int, input().split())

d = [0] * 31

d[1] = (1,0)
d[2] = (0,1)
for i in range(3, D+1):
    d[i] = (d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1])

a = d[D][0]
b = d[D][1]
n,m = 1,1
while True:
    if a*n + b*m == K:
        print(n,m,sep='\n')
        break
    elif a*n + b*m < K:
        m += 1
    else:
        n += 1
        m = 1