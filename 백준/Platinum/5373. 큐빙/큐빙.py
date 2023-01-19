import sys
input = sys.stdin.readline

# white, yellow, red, orange, green, blue
# up_arr, down_arr, front_arr, back_arr, left_arr, right_arr
"""
+ 일때
U => up_arr 배열은 90도 회전, front_arr[0] = right_arr[0], right_arr[0] = back_arr[0], back_arr[0] = left_arr[0], left_arr[0] = front_arr[0]

D => down_arr 배열은 90도 회전, front_arr[2] = left_arr[2], left_arr[2] = back_arr[2], back_arr[2] = right_arr[2], right_arr[2] = front_arr[2]

F => front_arr 배열은 90도 회전, up_arr[2] = left_arr[I][2], left_arr[I][2] = down_arr[0], down_arr[0] = right_arr[I][0], right_arr[I][0] = up_arr[2]

B => back_arr 배열은 90도 회전, up_arr[0] = right_arr[I][2], right_arr[I][2] = down_arr[2], down_arr[2] = left_arr[I][0], left_arr[I][0] = up_arr[0]

R => right_arr 배열은 90도 회전, front_arr[I][2] = down_arr[I][2], down_arr[I][2] = back_arr[I][0], back_arr[I][0] = up_arr[I][2], up_arr[I][2] = front_arr[I][2]

L => left_arr 배열은 90도 회전, front_arr[I][0] = up_arr[I][0], up_arr[I][0] = back_arr[I][2], back_arr[I][2] = down_arr[I][0], down_arr[I][0] = front_arr[I][0]

이런 식으로 변함

총 여섯개의 2차원 배열을 만들고 각각의 값을 변경 해주면 될듯 ㅇㅇ 
"""

def turn_clockwise(arr):
    res = [[] for _ in range(3)]
    for i in range(3):
        for j in range(2, -1, -1):
            res[i].append(arr[j][i])

    return res

def turn_counterclockwise(arr):
    res = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            res[3-1-j][i] = arr[i][j]
    return res

def up(clockwise : bool) -> None:
    global up_arr, front_arr, right_arr, back_arr, left_arr
    """
    U => up_arr 배열은 90도 회전, front_arr[0] = right_arr[0], right_arr[0] = back_arr[0], back_arr[0] = left_arr[0], left_arr[0] = front_arr[0]
    """
    if clockwise:
        up_arr = turn_clockwise(up_arr)
        front_arr[0], right_arr[0], back_arr[0], left_arr[0] = right_arr[0], back_arr[0], left_arr[0], front_arr[0]
    else:
        up_arr = turn_counterclockwise(up_arr)
        right_arr[0], back_arr[0], left_arr[0], front_arr[0] = front_arr[0], right_arr[0], back_arr[0], left_arr[0]


def down(clockwise : bool) -> None:
    global down_arr, front_arr, left_arr, back_arr, right_arr
    """
    D => down_arr 배열은 90도 회전, front_arr[2] = left_arr[2], left_arr[2] = back_arr[2], back_arr[2] = right_arr[2], right_arr[2] = front_arr[2]
    """
    if clockwise:
        down_arr = turn_clockwise(down_arr)
        front_arr[2], left_arr[2], back_arr[2], right_arr[2] = left_arr[2], back_arr[2], right_arr[2], front_arr[2]
    else:
        down_arr = turn_counterclockwise(down_arr)
        left_arr[2], back_arr[2], right_arr[2], front_arr[2] = front_arr[2], left_arr[2], back_arr[2], right_arr[2]


def front(clockwise : bool) -> None:
    global front_arr, up_arr, left_arr, down_arr, right_arr
    """
    F => front_arr 배열은 90도 회전, up_arr[2] = left_arr[I][2], left_arr[I][2] = down_arr[0], down_arr[0] = right_arr[I][0], right_arr[I][0] = up_arr[2]
    """

    tmp_left_arr = [left_arr[i][2] for i in range(3)][::-1]
    tmp_right_arr = [right_arr[i][0] for i in range(3)][::-1]
    if clockwise:
        front_arr = turn_clockwise(front_arr)
        up_arr[2], tmp_left_arr, down_arr[0], tmp_right_arr = tmp_left_arr, down_arr[0], tmp_right_arr, up_arr[2]
    else:
        front_arr = turn_counterclockwise(front_arr)
        tmp_left_arr, down_arr[0], tmp_right_arr, up_arr[2] = up_arr[2][::-1], tmp_left_arr[::-1], down_arr[0][::-1], tmp_right_arr[::-1]

    for i in range(3):
        left_arr[i][2] = tmp_left_arr[i]
        right_arr[i][0] = tmp_right_arr[i]

def back(clockwise : bool) -> None:
    global back_arr, up_arr, right_arr, down_arr, left_arr
    """
    B => back_arr 배열은 90도 회전, up_arr[0] = right_arr[I][2], right_arr[I][2] = down_arr[2], down_arr[2] = left_arr[I][0], left_arr[I][0] = up_arr[0]
    """
    tmp_right_arr = [right_arr[i][2] for i in range(3)]
    tmp_left_arr = [left_arr[i][0] for i in range(3)]

    if clockwise:
        back_arr = turn_clockwise(back_arr)
        up_arr[0], tmp_right_arr, down_arr[2], tmp_left_arr = tmp_right_arr, down_arr[2][::-1], tmp_left_arr, up_arr[0][::-1]
    else:
        back_arr = turn_counterclockwise(back_arr)
        tmp_right_arr, down_arr[2], tmp_left_arr, up_arr[0] = up_arr[0], tmp_right_arr[::-1], down_arr[2], tmp_left_arr[::-1]

    for i in range(3):
        left_arr[i][0] = tmp_left_arr[i]
        right_arr[i][2] = tmp_right_arr[i]


def right(clockwise : bool) -> None:
    global right_arr, front_arr, down_arr, back_arr, up_arr
    """
    R => right_arr 배열은 90도 회전, front_arr[I][2] = down_arr[I][2], down_arr[I][2] = back_arr[I][0], back_arr[I][0] = up_arr[I][2], up_arr[I][2] = front_arr[I][2]
    """
    
    tmp_front_arr = [front_arr[i][2] for i in range(3)]
    tmp_back_arr = [back_arr[i][0] for i in range(3)][::-1]
    tmp_down_arr = [down_arr[i][2] for i in range(3)]
    tmp_up_arr = [up_arr[i][2] for i in range(3)]

    if clockwise:
        right_arr = turn_clockwise(right_arr)
        tmp_front_arr, tmp_down_arr, tmp_back_arr, tmp_up_arr = tmp_down_arr, tmp_back_arr, tmp_up_arr[::-1], tmp_front_arr
    else:
        right_arr = turn_counterclockwise(right_arr)
        tmp_down_arr, tmp_back_arr, tmp_up_arr, tmp_front_arr = tmp_front_arr, tmp_down_arr[::-1], tmp_back_arr, tmp_up_arr

    for i in range(3):
        front_arr[i][2] = tmp_front_arr[i]
        back_arr[i][0] = tmp_back_arr[i]
        down_arr[i][2] = tmp_down_arr[i]
        up_arr[i][2] = tmp_up_arr[i]


def left(clockwise : bool) -> None:
    global left_arr, front_arr, up_arr, back_arr, down_arr
    """
    L => left_arr 배열은 90도 회전, front_arr[I][0] = up_arr[I][0], up_arr[I][0] = back_arr[I][2], back_arr[I][2] = down_arr[I][0], down_arr[I][0] = front_arr[I][0]
    """
    tmp_front_arr = [front_arr[i][0] for i in range(3)]
    tmp_up_arr = [up_arr[i][0] for  i in range(3)]
    tmp_back_arr = [back_arr[i][2] for i in range(3)][::-1]
    tmp_down_arr = [down_arr[i][0] for i in range(3)]

    if clockwise:
        left_arr = turn_clockwise(left_arr)
        tmp_front_arr, tmp_up_arr, tmp_back_arr, tmp_down_arr = tmp_up_arr, tmp_back_arr, tmp_down_arr[::-1], tmp_front_arr
    else:
        left_arr = turn_counterclockwise(left_arr)
        tmp_up_arr, tmp_back_arr, tmp_down_arr, tmp_front_arr = tmp_front_arr, tmp_up_arr[::-1], tmp_back_arr, tmp_down_arr

    for i in range(3):
        front_arr[i][0] = tmp_front_arr[i]
        up_arr[i][0] = tmp_up_arr[i]
        down_arr[i][0] = tmp_down_arr[i]
        back_arr[i][2] = tmp_back_arr[i]


def is_clockwise(move : str) -> bool:
    if move == "+":
        return True
    return False

def get_direction(move : str) -> bool:
    if move == "U":
        return up
    if move == "D":
        return down
    if move == "F":
        return front
    if move == "B":
        return back
    if move == "L":
        return left
    if move == "R":
        return right

def move(n,moving):
    for i in moving:
        way, clockwise = get_direction(i[0]), is_clockwise(i[1])
        way(clockwise)


def print_arr(arr):
    for i in arr:
        print(*i, sep='')

"""
Front = red
Back = orange
Right = blue
Left = green
Up = White
Down = Yellow
"""

t = int(input())
for _ in range(t):
    up_arr = [['w']*3 for _ in range(3)]
    down_arr = [['y']*3 for _ in range(3)]
    front_arr = [['r']*3 for _ in range(3)]
    back_arr = [['o']*3 for _ in range(3)]
    left_arr = [['g']*3 for _ in range(3)]
    right_arr = [['b']*3 for _ in range(3)]

    n = int(input())
    moving = list(map(str,input().rstrip().split()))
    move(n, moving)
    print_arr(up_arr)