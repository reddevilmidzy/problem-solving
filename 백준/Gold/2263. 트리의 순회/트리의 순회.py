import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def preorder(in_start, in_end, post_start, post_end):
    # 재귀 종료 조건 시작점 앞지르면
    if in_start > in_end or post_start > post_end:
        return
    
    # 후위 순휘 결과의 끝은 루트
    # 루트 출력
    parents = postorder[post_end]
    print(parents, end=' ')

    # 중위 순회에서 루트 기준으로 좌우로 갈라짐
    # 좌 우 선언
    left = position[parents] - in_start
    right = in_end - position[parents]

    # 좌 우로 트리를 추적하여 전위 순회를 찾음

    # 왼쪽서브트리
    preorder(in_start, in_start+left-1, post_start,post_start+left-1)
    # 오른쪽서브트리
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)


# 입력
n = int(input())

inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

# 후위 순회의 끝값이 중위 순회의 인덱스 위치를 확인하기 위해
# 중위 순회의 값들의 인덱스값을 저장

position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

# 탐색 시작
preorder(0,n-1,0,n-1)