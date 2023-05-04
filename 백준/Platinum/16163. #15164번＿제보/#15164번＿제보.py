def manachers(s:str, n:int) -> list[int]:
    r,p = 0,0
    arr = [0]*n
    for i in range(n):
        if i <= r:
            arr[i] = min(arr[2*p-i], r-i)
        else:
            arr[i] = 0
            
        while i-arr[i]-1 >= 0 and i+arr[i]+1 < n and s[i-arr[i]-1] == s[i+arr[i]+1]:
            arr[i] += 1

        if r < i + arr[i]:
            r = i + arr[i]
            p = i
    return arr
s = "#"+"#".join(input())+"#"
ans = sum([(i+1)//2 if i else 0 for i in manachers(s, len(s))])
print(ans)