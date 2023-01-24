# 풀이
# 회전시켜서 맞다면 1, 틀리다면 0 ㄱㄱ
# 꼭 6개 12 일 필요 없을 듯(?)
nums = list(map(int,input().split()))
ans = 0
"""
U = D
U` = D`
F = B
F` = B`
R = L
R` = L`
"""

def same(arr):
    arr.sort()
    return 1 if arr[0] == arr[-1] else 0

def up_clock(clockwise : bool) -> None:
    if clockwise:
        front[:2],right[:2],back[:2],left[:2] = right[:2],back[:2],left[:2],front[:2]
    else:
        right[:2],back[:2],left[:2],front[:2] = front[:2],right[:2],back[:2],left[:2]

    return [same(up), same(front), same(down), same(left), same(right), same(back)]

def front_clock(clockwise : bool) -> None:
    tmp_left = [left[1],left[3]][::-1]
    tmp_right = [right[0], right[2]][::-1]
    if clockwise:
        up[2:4],tmp_left,down[:2],tmp_right = tmp_left,down[:2],tmp_right,up[2:4]
    else:
        tmp_left,down[:2],tmp_right,up[2:4] = up[2:4][::-1],tmp_left[::-1],down[:2][::-1],tmp_right[::-1]
        
    left[1],left[3] = tmp_left[0],tmp_left[1]
    right[0],right[2] = tmp_right[0], tmp_right[1]
    
    return [same(up), same(front), same(down), same(left), same(right), same(back)]


def right_clock(clockwise : bool) -> None:
    tmp_front = [front[1], front[3]]
    tmp_back = [back[0], back[2]][::-1]
    tmp_down = [down[1], down[3]]
    tmp_up = [up[1], up[3]]

    if clockwise:
        tmp_front,tmp_down,tmp_back,tmp_up = tmp_down,tmp_back,tmp_up[::-1],tmp_front
    else:
        tmp_down,tmp_back,tmp_up,tmp_front = tmp_front,tmp_down[::-1],tmp_back,tmp_up

    front[1], front[3]=  tmp_front[0], tmp_front[1]
    back[0],back[2] = tmp_back[0], tmp_back[1]
    down[1], down[3] = tmp_down[0], tmp_down[1]
    up[1], up[3] = tmp_up[0], tmp_up[1]
    
    return [same(up), same(front), same(down), same(left), same(right), same(back)]

up,front,down,left,right,back = nums[:4],nums[4:8],nums[8:12],nums[12:16],nums[16:20],nums[20:24]
if sum(up_clock(True)) == 6:
    ans = 1

up,front,down,left,right,back = nums[:4],nums[4:8],nums[8:12],nums[12:16],nums[16:20],nums[20:24]
if sum(up_clock(False)) == 6:
    ans = 1
up,front,down,left,right,back = nums[:4],nums[4:8],nums[8:12],nums[12:16],nums[16:20],nums[20:24]
if sum(front_clock(True)) == 6:
    ans = 1
up,front,down,left,right,back = nums[:4],nums[4:8],nums[8:12],nums[12:16],nums[16:20],nums[20:24]
if sum(front_clock(False)) == 6:
    ans = 1
up,front,down,left,right,back = nums[:4],nums[4:8],nums[8:12],nums[12:16],nums[16:20],nums[20:24]
if sum(right_clock(True)) == 6:
    ans = 1
up,front,down,left,right,back = nums[:4],nums[4:8],nums[8:12],nums[12:16],nums[16:20],nums[20:24]
if sum(right_clock(False)) == 6:
    ans = 1

print(ans)