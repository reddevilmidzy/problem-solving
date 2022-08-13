import sys
input = sys.stdin.readline

l,c = map(int,input().split())
alp = sorted(list(map(str,input().split())))
tmp = []
mom = ['a','e','i','o','u']
def dfs():
    if len(tmp)==l:
        mom_cnt = 0
        son_cnt = 0
        for j in tmp:
            if j in mom:
                mom_cnt +=1
            else:
                son_cnt += 1
        if mom_cnt>0 and son_cnt>1:
            print(*tmp,sep='')
        return
    for i in alp:
        if i not in tmp:
            if len(tmp) == 0:
                tmp.append(i)
                dfs()
                tmp.pop()
            else:
                if ord(tmp[-1]) < ord(i):
                    tmp.append(i)
                    dfs()
                    tmp.pop()    
dfs()