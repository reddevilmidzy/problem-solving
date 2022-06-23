p,k = map(int,input().split())
for i in range(2, int(p**0.5)+1):
    if p%i == 0:
        if i < k or p//i < k:
            print('BAD',min(i,p//i))
            break
        else:
            print('GOOD')
            break
    if i > k:
        print('GOOD')
        break