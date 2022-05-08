import sys
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    a, b = map(int, input().rstrip().split())
    a_num = list(map(int, input().rstrip().split()))
    b_num = list(map(int, input().rstrip().split()))
    a_num.sort(reverse=True)
    b_num.sort(reverse=True)
    a_idx, b_idx = 0,0
    cnt = 0
    while a_idx < a and b_idx < b:
        if a_num[a_idx] > b_num[b_idx]:
            cnt += b-b_idx
            a_idx += 1
        else:
            b_idx += 1
    print(cnt)