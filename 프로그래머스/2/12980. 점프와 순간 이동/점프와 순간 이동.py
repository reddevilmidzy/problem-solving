def solution(n):
    res = 0
    while 0<n:
        if n%2:
            n-=1
            res+=1
        else:
            n >>= 1
    return res
