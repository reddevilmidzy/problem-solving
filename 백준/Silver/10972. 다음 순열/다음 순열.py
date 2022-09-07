import sys
input = sys.stdin.readline

n = int(input())
k = list(map(int,input().rstrip().split()))
nums = [i for i in range(1,n+1)]
ans= []
if k == sorted(k)[::-1]:
    print(-1)
else:
    for i in range(n-1, 0, -1):
        #print(i)
        if k[i] > k[i-1]:
            # print(k[i], k[i-1])
            #if k[:i-1] != []:
            ans.extend(k[:i-1])
            #print(k[:i-1],end=' ')
            #else:

            tmp = k[i:]
            check = sorted(k[i:])

            for j in range(len(check)):
                if check[j] > k[i-1]:
                    ans.append(check[j])
                    # print(check[j],end=' ')
                    tmp.remove(check[j])
                    break
            tmp.append(k[i-1])
            ans.extend(sorted(tmp))
            # print(sorted(tmp))
            break
    print(*ans)