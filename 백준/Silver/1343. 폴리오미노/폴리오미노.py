poli=input()
ans=[]
cnt=0
for i in poli:
    if i == 'X':
        cnt +=1
    else:
        if cnt%2!=0:
            print(-1)
            break
        else:
            if cnt:
                ans.append('AAAA'*(cnt//4))
                ans.append('B'*(cnt%4))
                cnt=0
            ans.append('.')
else:
    if cnt%2!=0:
        print(-1)
    else:
        ans.append('AAAA'*(cnt//4))
        ans.append('B'*(cnt%4))
        print(*ans,sep='')