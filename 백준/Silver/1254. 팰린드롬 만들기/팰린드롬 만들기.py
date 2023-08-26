import sys
input = sys.stdin.readline
 
def manachers(s: str, n: int):
    r,p = 0,0
    arr = [0]*n
    # 문자열 인덱스 0부터 n-1 까지 탐색
    for i in range(n):
        if i <= r:
            arr[i] = min(arr[2*p-i], r-i)
        else:
            arr[i] = 0
        while i - arr[i] - 1 >= 0 and i + arr[i] + 1 < n and s[i-arr[i] - 1] == s[i+arr[i] + 1]:
            arr[i] += 1
        
        if r < i + arr[i]:
            r = i + arr[i]
            p = i
    return arr
    
# 짝수길이의 팰린드롬도 체크하기 위해 문자 삽입
s = input()
# s = "abacaba"
n = len(s)*2-1
string = "#"+"#".join(s)+"#"
arr = manachers(string, n)
res = n-1

for idx, val in enumerate(arr):
    if idx + val == n-1: # 해당 팰린드롬이 문자열 끝까지 이어지는지
        res = min(res, (n-1)//2-val)

print(res+ len(s)-1)