import sys
input = sys.stdin.readline

def binary(arr, target, start, end):
    while start <= end:        
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0 
    
for i in range(int(input().rstrip())):
    n = int(input().rstrip())
    num1 = list(map(int, input().rstrip().split()))
    num1.sort()
    m = int(input().rstrip())
    num2 = list(map(int, input().rstrip().split()))
    for j in num2:
        print(binary(num1, j, 0, n-1))