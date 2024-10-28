from collections import defaultdict
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
mall = [defaultdict(int) for _ in range(m + 1)]
mv = [0] * (m + 1)
own = [set() for _ in range(n + 1)]
people = [0] * (m + 1)
king_cnt = [0] * (n + 1)
for i in range(1, n + 1):
    nums = list(map(int,input().split()))
    for j in range(0, len(nums), 2):
        u,v = nums[j], nums[j+1]
        own[i].add(u)
        mall[u][i] = v # u번째 매장에서 i번째 직원의 초기 매출액
        if v > mv[u]:
            mv[u] = v
            # u매장의 매출왕은 i직원
            people[u] = i

res = set()
for i in range(1, n + 1):
    for shop in own[i]:
        if mall[shop][i] == mv[shop]:
            king_cnt[i] += 1
    if king_cnt[i] == k:
        res.add(i)

# print('res', res)
q = int(input())
for _ in range(q):
    u,v,w = map(int,input().split())
    # 직원번호, 매장번호, 증가액
    mall[v][u] += w

    # 증가했는데 이전에 mall의 최고매출액보다 큰경우
    # 1. 1등이 쭉 1등 유지

    # 2. 새로운 강자 등장.
    # 2-1. 새로운 자리 차지했지만 아직 매출왕은 못함
    # 2-2. 새로운 자리 차지하고 매출왕 등극
    if mv[v] < mall[v][u]:
        mv[v] = mall[v][u]

        if people[v] != u: 
        # 기존의 강자 제거
            if people[v] in res:
                res.remove(people[v])
            
            king_cnt[people[v]] -= 1
            people[v] = u
            
            # 새로운 킹자리 추가
            king_cnt[u] += 1

            if king_cnt[u] == k:
                res.add(u)

    print(len(res))
