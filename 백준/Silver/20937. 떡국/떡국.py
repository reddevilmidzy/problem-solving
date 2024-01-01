from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = Counter(nums)
print(cnt.most_common(1)[0][1])