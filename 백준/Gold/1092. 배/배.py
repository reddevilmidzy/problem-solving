n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
res = 0
if max(a) < max(b):
    res = -1
else:
    while b:
        res += 1
        for i in range(n):
            for j in range(len(b)):
                if a[i] >= b[j]:
                    b.pop(j)
                    break
    
print(res)