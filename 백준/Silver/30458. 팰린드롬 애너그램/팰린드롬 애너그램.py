from collections import Counter
n = int(input())
s = input().rstrip()
l = Counter(s[:n//2])
r = Counter(s[(n+1)//2:])
l.update(r)
print(["No","Yes"][all(v%2==0 for v in l.values())])
