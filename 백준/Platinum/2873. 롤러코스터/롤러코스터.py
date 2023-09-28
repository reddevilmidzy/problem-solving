import sys
input = sys.stdin.readline
 
def way(r:int, c:int, horizontal:bool, reversed:bool)->str:
    res = ""

    if horizontal:
        for i in range(r):
            if i%2:
                res += "L"*(c-1)
            else:
                res += "R"*(c-1)
            
            if i<r-1:
                if reversed:
                    res += "U"
                else:
                    res += "D"
    else:
        for j in range(c):
            if j%2:
                res += "U"*(r-1)
            else:
                res += "D"*(r-1)
            
            if j<c-1:
                if reversed:
                    res += "L"
                else:
                    res += "R"
    
    if reversed:
        return res[::-1]
    return res

def solve(n,m):
    if n%2:
        return way(n,m,True,False)
    if m%2:
        return way(n,m,False,False)

    r,c=-1,-1
    min_val = 1001

    for i in range(n):
        for j in range(m):
            if (i+j)%2 and min_val > a[i][j]:
                min_val = a[i][j]
                r,c = i,j

    if r%2:
        pre = way(n,c,False,False)
        suf = way(n-r-1,m-c,True,False)[::-1]
        mid1 = way(r-1, m-c, True, False)
        mid2 = way(2, m-c-1, False, False)

        one = "" if c == 0 else "R"
        two = "R" if r==1 else "DR"
        three = "" if r == n-1 else "D"
        
    else:
        pre = way(r,m,True,False)
        suf = way(n-r,m-c-1,False,False)[::-1]
        mid1 = way(n-r,c-1,False,False)
        mid2 = way(n-r-1, 2, True, False)

        one = "" if r == 0 else "D"
        two = "D" if c==1 else "RD"
        three = "" if c == m-1 else "R"

    return pre + one + mid1 + two + mid2 + three + suf


n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

print(solve(n,m))