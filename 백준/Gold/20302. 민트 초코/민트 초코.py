from collections import defaultdict
import sys
input = sys.stdin.readline 

def era():
    global cnt
    m = 100000
    primes = [False, False] + [True]*(m-1)
    res = []
    for i in range(2, int(m**0.5)+1):
        if primes[i]:
            res.append(i)
            for j in range(i+i, m+1, i):
                primes[j] = False
    return res

cnt = defaultdict(int)
primes = era()

def factors(num:int, val:int) -> None:
    for p in primes:
        if p > num:
            break
        while not num%p:
            num //= p
            cnt[p] += val

    if num!=1:
        cnt[num] += val

n = int(input())
s = input().rstrip().split()

num = abs(int(s[0]))
if num == 0:
    print("mint chocolate")
    exit()
elif num == 1:
    pass
else:
    factors(num, 1)

for i in range(1, 2*n-1, 2):
    num = abs(int(s[i+1]))
    if num == 1:
        continue
    elif not num:
        print("mint chocolate")
        break
    if s[i] == '*':
        factors(num, 1)
    else:
        factors(num,-1)

else:
    for i in cnt.values():
        if i<0:
            print("toothpaste")
            break
    else:
        print("mint chocolate")
