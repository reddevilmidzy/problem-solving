n = list(map(int,input()))
n_len = len(n)

if n_len==1:
    print("NO")
else:
    a = b = 1
    for i in range(n_len-1):
        a = b =1
        for j in range(i+1):
            a *= n[j]
        for k in range(i+1, n_len):
            b *= n[k]
        if a == b:
            break
    if a == b:
        print("YES")
    else:
        print("NO")