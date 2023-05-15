import sys
input = sys.stdin.readline

def manachers(s: str, n: int):
    r,p = 0,0
    arr = [0]*n
    # 문자열 인덱스 0부터 n-1 까지 탐색
    for i in range(n):
        if i <= r:
            arr[i] = min(arr[2*p-i], r-i)
        else: # 팰린드롬이 아닌경우
            arr[i] = 0

        while i - arr[i] - 1 >= 0 and i + arr[i] + 1 < n and s[i-arr[i] - 1] == s[i+arr[i] + 1]:
            arr[i] += 1
        
        # 아마도 새로운 반지름을 찾은게 아닐까
        if r < i + arr[i]:
            r = i + arr[i]
            p = i
    # 반지름을 찾은 배열임 지름 계산
    # print(arr)
    return arr
    
# 짝수길이의 팰린드롬도 체크하기 위해 문자 삽입
n = int(input())*2+1
string = "#"+"#".join(input().rstrip())+"#"
# print(string)

arr = manachers(string, n)
res = n

for idx, val in enumerate(arr):
    # print(idx,val, "akakdk")
    if idx + val == n-1:
        res = min(res, (n-1)//2-val)

print(res)