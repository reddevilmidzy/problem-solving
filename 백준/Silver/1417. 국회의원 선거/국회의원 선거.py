n = int(input())
dasom = int(input())
candi = []
cnt = 0
for i in range(n-1):
    masu = int(input())
    candi.append(masu)
if n == 1:
    pass
else:
    while dasom <= max(candi):
        dasom += 1
        cnt += 1
        candi[candi.index(max(candi))] -= 1
print(cnt)