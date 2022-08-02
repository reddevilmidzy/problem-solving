def solve(a,b,c):
    if b == 1:
        return a%c
    else:
        k = solve(a, b//2, c)
        if b%2 == 0:
            return k*k%c
        else:
            return k*k*a%c
a,b,c = map(int, input().split())
print(solve(a,b,c))