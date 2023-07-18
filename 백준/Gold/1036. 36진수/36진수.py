from collections import defaultdict
bit = 36

def format_num(num:str) -> int:
    res = 0
    for c in num:
        if c.isnumeric():
            res += int(c)
        else:
            res += ord(c) - 55    
    return res

n = int(input())
dd = defaultdict(int)
nums = []

for _ in range(n):
    tmp = list(map(format_num, input().rstrip()))
    for i in range(len(tmp)):
        dd[tmp[i]] += bit**(len(tmp)-i-1)
    nums.append(tmp)

k = int(input())

res = 0
convert = [False]*(bit)
for num,cnt in sorted(dd.items(), key=lambda x:(-(35-x[0])*x[1])):
    if k:
        k -= 1
        convert[num] = True
    else:
        break

for num in nums:
    for i in range(len(num)):
        if convert[num[i]]: # Z 로 바꿀놈
            res += (bit**(len(num)-i-1)) * 35
        else:
            res += (bit**(len(num)-i-1)) * num[i]

ans = []
if not res: ans.append("0")
while res:
    ans.append(str(res%bit) if res%bit < 10 else chr(res%bit+55))
    res //= bit
print("".join(reversed(ans)))