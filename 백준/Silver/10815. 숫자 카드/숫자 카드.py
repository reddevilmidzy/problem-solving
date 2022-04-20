import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input().rstrip())
n_lis = list(map(int, input().rstrip().split()))
n_lis.sort()


m = int(input().rstrip())
m_lis = list(map(int, input().rstrip().split()))
for i in m_lis:
    result = binary_search(n_lis, i, 0, n-1)
    if result == None:
        print(0, end=" ")
    else:
        print(1, end=" ")
