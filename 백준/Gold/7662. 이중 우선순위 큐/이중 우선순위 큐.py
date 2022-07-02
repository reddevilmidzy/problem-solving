import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    num_dict = defaultdict(int)
    maxh = []
    minh = []
    for i in range(n):
        code, num = map(str,input().rstrip().split())
        num = int(num)
        if code == 'I':
            num_dict[num] += 1
            heapq.heappush(maxh, -num)
            heapq.heappush(minh, num)
        else:
            if num == 1:
                while(maxh):
                    max_num = -heapq.heappop(maxh)
                    if num_dict[max_num] != 0:
                        num_dict[max_num] -= 1
                        break
            else:
                while(minh):
                    min_num = heapq.heappop(minh)
                    if num_dict[min_num] != 0:
                        num_dict[min_num] -= 1
                        break
        
    while maxh and num_dict[-maxh[0]] == 0:
        heapq.heappop(maxh)
    while minh and num_dict[minh[0]] == 0:
        heapq.heappop(minh)

    if not maxh:
        print('EMPTY')
    else:
        print(-maxh[0], minh[0])