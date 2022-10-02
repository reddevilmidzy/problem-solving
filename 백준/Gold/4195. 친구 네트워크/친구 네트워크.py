import sys
input = sys.stdin.readline



def find_parent(x):
    if parent[x] ==x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    pre_sum = cnt[a]+cnt[b]
    if a>b:
        parent[a] = b
        cnt[a] = pre_sum
        cnt[b] = cnt[a]
    elif a<b:
        parent[b] = a
        cnt[b] = pre_sum
        cnt[a] = cnt[b]


for _ in range(int(input())):
    n = int(input())
    idx = 0
    cnt = dict()
    parent = dict()
    for i in range(n):
        user1, user2 = map(str,input().rstrip().split())
        
        if user1 not in parent:
            parent[user1] = user1
            cnt[user1] = 1
        if user2 not in parent:
            parent[user2] = user2
            cnt[user2] = 1
        
        union_parent(user1, user2)

        print(cnt[find_parent(user1)])