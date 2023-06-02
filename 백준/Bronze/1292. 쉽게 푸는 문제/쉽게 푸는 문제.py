arr = []
for i in range(1, 46):
    for u in range(1, i+1):
        arr.append(i)
a, b = map(int, input().split())
print(sum(arr[a-1:b]))

