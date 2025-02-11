import sys
input = sys.stdin.readline

def get_manachers(s: str):
    r,p = 0,0
    n = len(s)
    arr = [0]*n
    for i in range(n):
        if i <= r:
            arr[i] = min(arr[2*p-i], r-i)

        while i - arr[i] - 1 >= 0 and i + arr[i] + 1 < n and s[i-arr[i] - 1] == s[i+arr[i] + 1]:
            arr[i] += 1
        
        if r < i + arr[i]:
            r = i + arr[i]
            p = i
    return arr

def solve(s: str) -> str:
    if s == s[::-1]:
        return s

    string = "#"+"#".join(s)+"#"
    n = len(string)
    manacher = get_manachers(string)

    go = n
    back = n

    for idx, val in enumerate(manacher):
        if idx + val == n-1:
            go = min(go, (n-1)//2 - val)
        
        if (n - idx - 1) + val == n-1:
            back = min(back, (n-1)//2 - val)

    if go < back:
        return s + s[:go][::-1]
    else:
        return s[-back:][::-1] + s

s = input().rstrip()
print(solve(s))