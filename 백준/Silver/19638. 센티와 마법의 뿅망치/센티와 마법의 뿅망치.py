import sys, heapq
input = sys.stdin.readline

n,h,t = map(int,input().split())
hq = [-int(input()) for _ in range(n)]
heapq.heapify(hq)

# 키의 최대값이 이미 h보다 작은 경우 안자름
# h가 1인 경우 아무리 잘라도 못줄임 --> 그래도 일단 다 떄려야 함..ㅎㅎ

if -min(hq) < h:
    print("YES", 0, sep='\n')
else:
    cnt = 0
    while cnt < t:
        height = -heapq.heappop(hq)
        if height < h:
            print("YES", cnt, sep='\n')
            break
        else:
            if height == 1:
                heapq.heappush(hq, -1)
            else:
                heapq.heappush(hq, -(height//2))
        cnt += 1
    else:
        height = -heapq.heappop(hq)
        if height < h:
            print("YES", cnt, sep='\n')
        else:
            print("NO", height,sep='\n')