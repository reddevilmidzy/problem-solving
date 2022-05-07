n = int(input())
sick = list(input())
hui = dict()
num = []
for i in sick:
    if 65 <= ord(i) <= 90:
        if i not in hui:
            hui[i] = input()

for j in sick:
    if 65 <= ord(j) <= 90:
        num.append(hui[j])
    else:
        a = str(num.pop())
        b = str(num.pop())
        num.append(eval(b+j+a))

print(f"{num[0]:.2f}")