def manachers(s,n):
    r,p = 0,0
    arr = [0]*n
    for i in range(n):
        arr[i] = 0 if i>r else min(arr[2*p-i], r-i)            
        while i-arr[i]-1 >= 0 and i+arr[i]+1 < n and s[i-arr[i]-1] == s[i+arr[i]+1]:
            arr[i] += 1
        if r < i + arr[i]:
            r = i + arr[i]
            p = i
    return sum([(i+1)//2 if i else 0 for i in arr])
s = "#"+"#".join(input())+"#"
print(manachers(s, len(s)))