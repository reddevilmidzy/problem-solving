import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = []

def post_order(start, end):
    if start > end:
        return
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            mid = i
            break
    else:
        mid = end + 1
    
    post_order(start+1, mid-1)
    post_order(mid, end)
    print(tree[start])

while True: # 입력이 언제 끝길지 모름
    try:
        tree.append(int(input()))
    except:
        post_order(0, len(tree)-1)
        break