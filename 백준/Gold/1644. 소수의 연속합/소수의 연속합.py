n = int(input())

def era(n):
    prime = [True]*(n+1)
    lis = []
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    for i in range(2, n+1):
        if prime[i]:
            lis.append(i)
    return lis

def two_point(lis,n):
    one = 0
    two = 0
    res = 0
    while one <= n and two <= n:
        tmp = sum(lis[one:two+1])
        if tmp > n:
            one += 1
        elif tmp < n:
            two += 1
        else:
            one += 1
            res += 1
    return res

prime = era(n)
print(two_point(prime, n))