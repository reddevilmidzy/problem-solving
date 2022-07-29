import sys
input = sys.stdin.readline

prime_list = [False, False] + [True]*999999
for i in range(2,1000001):
    if prime_list[i] == True:
        for j in range(i*2, 1000001, i):
            prime_list[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(n-1, n//2-1, -1):
            if prime_list[i] and prime_list[n-i]:
                print(f"{n} = {n-i} + {i}")
                break
        else:
            print("Goldbach's conjecture is wrong.")