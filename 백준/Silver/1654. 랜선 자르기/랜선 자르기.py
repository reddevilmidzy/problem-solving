n, k = map(int, input().split())
lan = [int(input()) for i in range(n)]
max_lan = max(lan)
res = []
def binary(k, start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in lan:
            cnt += i//mid
        if cnt < k:
            end = mid - 1
        else:
            res.append(mid)
            start = mid + 1
binary(k,1,max_lan)
print(max(res))           