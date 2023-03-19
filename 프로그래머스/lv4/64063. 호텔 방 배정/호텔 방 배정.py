import sys
sys.setrecursionlimit(10**5)

def find(parent, x):
    if x in parent:
        parent[x] = find(parent, parent[x])
        return parent[x]
    parent[x] = x + 1
    return x

def solution(k, room_number):
    parent = dict()
    answer = [find(parent, num) for num in room_number]
    return answer