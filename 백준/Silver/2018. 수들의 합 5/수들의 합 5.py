n=int(input())
tot = 0
res = 0
for i in range(1, n+1):
    tot += i
    if (n-tot >= 0 and not (n-tot)%i):
        res += 1
print(res)