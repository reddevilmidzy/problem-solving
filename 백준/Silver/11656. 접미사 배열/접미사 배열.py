s = input()
arr = []
for i in range(len(s)):
    arr.append(str(s[i:]))
print(*sorted(arr),sep='\n')