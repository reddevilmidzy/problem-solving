x_group, y_group = [], []

for i in range(3):
    x, y = map(int, input().split())
    x_group.append(x)
    y_group.append(y)
for j in x_group:
    if x_group.count(j) == 1:
        a = j
for k in y_group:
    if y_group.count(k) == 1:
        b = k
print(a, b)