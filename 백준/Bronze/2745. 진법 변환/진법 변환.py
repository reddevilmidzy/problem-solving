n,b = map(str,input().split())
b = int(b)
number = dict()
for i in range(10):
    number[str(i)] = i

for i in range(26):
    number[chr(i+65)] = i+10
num = 0
idx = 0

for i in range(len(n)-1, -1, -1):
    num += number[n[i]] * (b**idx)
    idx += 1
print(num)