import sys
input = sys.stdin.readline

ans = []

a, z = input().strip().split('=')
x, y = a.split('+')
# x, y는 반응물, z는 생성물
cho = {'C':0, 'H':1, 'O':2}

def cnt(m):
    result = [0]*3
    before = None
    for i in m:
        if i in ['C', 'H', 'O']:
            result[cho[i]] += 1
            before = i
        else:
            result[cho[before]] += int(i)-1
    return result

x = cnt(x)
y = cnt(y)
z = cnt(z)

for j in range(1, 11):
    for k in range(1, 11):
        for l in range(1, 11):
            if x[0]*j + y[0]*k == z[0]*l and \
               x[1]*j + y[1]*k == z[1]*l and \
               x[2]*j + y[2]*k == z[2]*l:
                ans.append([j,k,l])

print(*ans[0])