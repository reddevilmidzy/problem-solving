def is_same(left:str, right:str) -> bool:
    return left.lower() == q_dict[right.lower()] or left.lower() == q_dict[right.upper()] or left.upper() == q_dict[right.lower()] or left.upper() == q_dict[right.upper()]

def can_be_palin(string: str):
    for c in set(string):
        if q_dict[c.lower()] == "" and q_dict[c.upper()] == "":
            return False
    return True

def get_palin(val:str, center: str) -> str:
    m = len(val)
    left = [0]*m
    right = [0]*m
    cen = [c.upper() if q_dict[c.lower()] == "" else c.lower() for c in center]

    for i in range(m):
        if q_dict[val[i].lower()] != "":
            left[i] = val[i].lower()
            right[m-i-1] = q_dict[val[i].lower()]
        else:
            left[i] = val[i].upper()
            right[m-i-1] = q_dict[val[i].upper()]
    
    return "".join(left) + "".join(cen) + "".join(right)
def manacher(s:str, n:int):
    r,p = 0,0
    arr = [0]*n
    for i in range(n):
        if i <= r:
            arr[i] = min(arr[2*p-i], r-i)
        else:
            arr[i] = 0
        if not is_same(s[i], s[i]): continue
        while i-arr[i]-1>=0 and i+arr[i]+1 < n and is_same(s[i-arr[i]-1], s[i+arr[i]+1]):
            arr[i] += 1
        if r<i+arr[i]:
            r = i + arr[i]
            p = i
    return arr

q_dict = dict()
my_self = ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y", 
           "i", "l", "m", "n", "o", "u", "v", "w", "x", 
           "0", "1", "8",
           "#"]
couple = [("E", "3"), ("S", "2"), ("Z", "5"), ("b", "d"), ("p", "q"), ("r", "7")]

for i in range(65, 91):
    q_dict[chr(i)] = "" # 대문자
    q_dict[chr(i).lower()] = "" # 소문자
for i in range(10):
    q_dict[str(i)] = ""
for c in my_self:
    q_dict[c] = c
for b,d in couple:
    q_dict[b] = d
    q_dict[d] = b

origin = input()
if not can_be_palin(origin):
    print(-1)
    exit()

s = "#" + "#".join(origin) + "#"
n = len(s)
arr = manacher(s ,n)

result = []

for idx,val in enumerate(arr):
    if idx + val == n-1:
        idx = (idx-1)//2 
        val = (n-1)//2-val
        result.append(get_palin(origin[:val], origin[val:]))
        break

# 왼쪽에 새로운 문자 추가
origin = origin[::-1]
for idx, val in enumerate(arr[::-1]):
    if idx + val == n-1:
        idx = (idx-1)//2
        val = (n-1)//2-val
        result.append(get_palin(origin[:val], origin[val:])[::-1])
        break
print(sorted(result, key=lambda x:len(x))[0])