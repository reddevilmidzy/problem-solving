from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input().rstrip())
n_lis = list(map(int, input().rstrip().split()))
n_lis.sort()

m = int(input().rstrip())
m_lis = list(map(int, input().rstrip().split()))

def count_by_range(a, l_val, r_val):
    r_inx = bisect_right(a, r_val)
    l_inx = bisect_left(a, l_val)
    return r_inx - l_inx

for i in range(m):
    print(count_by_range(n_lis, m_lis[i], m_lis[i]), end=" ")