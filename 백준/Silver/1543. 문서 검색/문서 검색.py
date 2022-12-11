docs = input().rstrip()
search = input().rstrip()
n = len(search)
ans = 0
idx = 0
while idx < len(docs):
    if docs[idx:idx+n] == search:
        ans += 1
        idx += n
        continue
    idx += 1

print(ans)