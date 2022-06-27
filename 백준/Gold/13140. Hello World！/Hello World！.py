import itertools, sys
input = sys.stdin.readline

nums = [1,2,3,4,5,6,7,8,9,0]
n = int(input().rstrip())
for s in itertools.permutations(nums, 7):
    h,e,l,o,w,r,d = s
    if h == 0 or w == 0:
        continue
    hello = 10000*h + 1000*e + 100*l + 10*l + o
    world = 10000*w + 1000*o + 100*r + 10*l + d
    
    if hello + world == n:
        print(f"  {hello}")
        print(f"+ {world}")
        print('-'*7)
        print(str(n).rjust(7))
        exit()

print("No Answer")