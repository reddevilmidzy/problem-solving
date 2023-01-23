import sys, math
input = sys.stdin.readline

MOD = 10**9+7
def solve():
    t = int(input())
    for _ in range(t):
        i = int(input())
        if not i%2:
            i //= 2
            print((math.factorial(2*i) // (math.factorial(i) * math.factorial(i+1))) % MOD)
        else:
            print(0)

solve()