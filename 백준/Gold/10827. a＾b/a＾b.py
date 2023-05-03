def multi(n:int, k:int) -> int:
    if k == 1:
        return n
    if k%2==0:
        val = multi(n, k//2)
        return val*val
    return multi(n, k-1) * n

a,b = map(str, input().split())
n = int(a.replace(".", ""))
k = int(b)
len_float_point = len(a[a.index("."):]) - 1
ans = str(multi(n,k))
if len(ans) < len_float_point*k:
    ans = "0"*(len_float_point*k -  len(ans)+1) + ans
print(ans[:-len_float_point*k], ans[-len_float_point*k:], sep='.')