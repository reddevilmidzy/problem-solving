sick = list(map(str, input().rstrip()))
num = ''
nums = []
for s in sick:
    if s != '-' and s != '+':
        num += s
    else:
        nums.append(int(num))
        num = ''
        nums.append(s)
else:
    nums.append(int(num))
plus = []
minus = False
#print(nums)
for n in nums:
    if type(n) == int and not minus:
        plus.append(n)
    elif type(n) == int and minus:
        plus.append(-n)
    elif n == '+':
        pass
    elif n == '-':
        minus = True
print(sum(plus))