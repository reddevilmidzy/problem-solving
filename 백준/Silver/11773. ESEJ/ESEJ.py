from itertools import permutations
a,b = map(int,input().split())
cnt = max((b+1)//2, a)
for i in permutations("abcdefghi", 9):
    print("".join(i), end=' ')
    cnt -= 1
    if not cnt:break