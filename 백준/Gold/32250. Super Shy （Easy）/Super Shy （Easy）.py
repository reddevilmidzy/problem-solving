import sys
input = sys.stdin.readline

n = int(input())
g=[((2<<i+1)-1, 1<<i) for i in range(20)]
def bi(n: int) -> int:
    res = 0
    for end,length in g:
        if end<n:
            res += length
        elif end-length<n:
            res +=n-end+length
        else:
            break
    return res

def si(n: int) -> int:
    if n<2:
        return 0
    return 1+bi(n-1)

def f(k: int) -> int:
    if n-k-1<0:
        return 0
    return 1+si(k)+si(n-k-1)
print(max(f(n//2),f(1<<n.bit_length()-1)))
