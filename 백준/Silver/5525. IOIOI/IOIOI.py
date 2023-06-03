n = int(input())
m = int(input())
s = input()
ans = 0
check = 0
i = 0
while i < m-2:
    if s[i:i+3] == 'IOI':
        check += 1
        i += 1
        if check == n:
            ans += 1
            check -= 1
    else:
        check = 0
    i += 1
print(ans)