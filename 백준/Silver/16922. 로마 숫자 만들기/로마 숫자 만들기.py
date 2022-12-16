from itertools import combinations_with_replacement
n = int(input())
arr = [1,5,10,50]
res = set()

for i in combinations_with_replacement(arr, n):
    res.add(sum(list(i)))

print(len(res))